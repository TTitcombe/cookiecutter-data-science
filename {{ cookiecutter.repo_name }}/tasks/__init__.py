from invoke import Collection

from . import docker
from . import internal


ns = Collection(docker)
ns.configure({"run": {"shell": internal.shell, "pty": internal.pty}})
