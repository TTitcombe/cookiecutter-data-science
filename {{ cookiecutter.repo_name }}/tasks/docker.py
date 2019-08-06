import os

from invoke import task

from .internal import os_name


@task
def pull(ctx, image_name):
    ctx.run('docker pull {}'.format(image_name))


@task
def push(ctx):
    print("Add commands to push new Docker image!")


@task
def build_image(ctx, image_name):
    if not os.path.isfile("docker/Dockerfile"):
        raise RuntimeError("You must invoke this command from the top level of the project")

    ctx.run('docker build --tag={} -f docker/Dockerfile .'.format(image_name))


def _run_container(ctx, image_name, use_volume=False, use_jupyter=False, name=None, cmd=None):
    cmd_string = 'docker run -it '
    if use_volume:
        cwd = '%CD%' if os_name == "nt" else '$(pwd)'
        cmd_string += '-v {}:/home/work '.format(cwd)
    if use_jupyter:
        cmd_string += '-p 8888:8888 '
    if name:
        cmd_string += '--name={} '.format(name)

    cmd_string += image_name

    if cmd:
        cmd_string += cmd

    ctx.run(cmd_string)


@task
def run_jupyter(ctx, image_name, name=None):
    _run_container(ctx, image_name, use_volume=True, use_jupyter=True, name=name)


@task
def run_python(ctx, image_name, name=None):
    _run_container(ctx, image_name, use_volume=True, name=name, cmd="python")


@task
def run(ctx, image_name, name=None):
    _run_container(ctx, image_name, use_volume=True, use_jupyter=True, name=name, cmd="/bin/bash")
