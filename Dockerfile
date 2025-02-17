# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
ARG WORKDIR=/wd
ARG USER=user

WORKDIR ${WORKDIR}

RUN useradd --system ${USER} && \
    chown --recursive ${USER} ${WORKDIR}

# Copy the requirements file to the working directory
COPY requirements.txt .

RUN apt update && apt upgrade -y

# Install the Python dependencies
RUN pip install --upgrade pip && \
    pip install --requirement requirements.txt

COPY --chown=${USER} ./Makefile Makefile

# For application
COPY --chown=${USER} templates /wd/templates
COPY --chown=${USER} static /wd/static
COPY --chown=${USER} app.py app.py

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose the Flask default port
#EXPOSE 5000

# Start Gunicorn with the Flask app
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]