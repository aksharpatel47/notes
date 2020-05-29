# How To Get Started With Docker

**By: Peter Mckee**

[Youtube link](https://www.youtube.com/watch?v=iqqDU2crIEQ)

## Docker Commands

* To build an image: `docker image build`
* To run a container: `docker container run`
* To see running containers: `docker container ls`
* To see all containers (even the ones that are stopped): `docker container ls -a`
* To remove a container: `docker container rm`
* To see all images: `docker image ls`
* Argument to add port mapping from host to container: `-p {host_port}:{container_port}`
* Argument to run a container in background: `-d or --detach`
* To stop a container: `docker container stop`
* To see logs of a container: `docker container logs`

## Docker Hub

* A place to store and, access public and, private images. Our image can be stored in a repository on docker hub.
* Tag a local image using `docker tag` command.
* Push the newly tagged image to a docker hub repository using: `docker push` command. The name of the tag of the local image and the repository name on Dockerhub should be the same.
* Pull an image from docker hub to local machine using `docker pull` command.

## Docker Compose

A tool for composing a system made up of multiple containers.

Write a `docker-compose.yml` file and use the `docker-compose up` command to start the system as defined using the yml file.

To stop the running system, use the `docker-compose down` command.

For usecases of databases, use volumes to store persistent data.

Use `-d` argument to run the system in detached state.
