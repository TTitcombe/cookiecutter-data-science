# Use jupyter/scipy base image.
# See https://hub.docker.com/u/jupyter for other available images
FROM jupyter/scipy-notebook:latest


# ---------- Install additional python requirements --------------------------------------------------------------------
# Move the requirements file into the image
COPY ./binder/requirements.txt /tmp/

# Install the python requirements on the image
RUN pip install --trusted-host pypi.python.org -r /tmp/requirements.txt

# Get root permissions
USER root

# Remove the requirements file - this is no longer needed
RUN rm /tmp/requirements.txt


# ---------- Setup project structure -----------------------------------------------------------------------------------
# Create a directory for our work and set it as the working directory
RUN mkdir /home/work
WORKDIR /home/work


# ---------- Final setup -----------------------------------------------------------------------------------------------
# jupyter base image exposes port 8888 for notebooks, so we don't need to do this here

# Enter the container into a jupyter notebook by default. This is included in jupyter/base-notebook.
CMD ["/usr/local/bin/start-notebook.sh"]

# Set the correct user
USER $NB_UID