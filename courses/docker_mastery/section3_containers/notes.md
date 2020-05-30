# Section 3 Notes

## Initial Commands

`$ docker version`

Check if docker is installed and working properly

`$ docker info`

See config values of the engine

### Docker new command line structure

`$ docker <command> <sub-command> (options)`

## Images and Containers

* Image is the application we want to run.
* Container is an instance of an image running as a process

### Running Nginx on Port 80

`$ docker container run --publish 80:80 nginx`

The above command does the following:

* Downloads the latest nginx image or picks it up from local cache 
if its available
* Starts a new container using the nginx image
* Binds the port 80 of the host to the port 80 of the container

If you go to `localhost` from the browser, you'll see the landing 
page of nginx.

### Container Commands

`$ docker container ls`

Shows running containers

`$docker container ls -a`

Shows running as well as stopped containers

`run --detach`

Runs the container in the background in detached mode

`$ docker container logs <container_name>`

Shows the logs of the container

`$ docker container top <container_name>`

Shows the processes running inside the container

**TIP**: Use the --help command to learn more about individual 
docker commands / sub-commands

`$ docker container stats <container_name>?`

Shows the CPU/Memory/Disk space utilized by the different 
containers.

#### Run container with interactive terminal

`$ docker container run -it <image_name> bash`

This starts a new container and gives us access to the bash 
command line.

To restart such a container with command line access:

`$ docker container start -ai <container_name>`

**Note**: `bash` should be available in the image for this to 
work. If `bash` is not available, use `sh`.

#### Execute a command on a running container

`$ docker container exec -it <container_name> <command>`

## Container Networking

**TIP**: Create a new network for each app

Containers on the same network are able to talk to each other 
without publishing the ports.

`$ docker container port <container_name>`

Use the above to list the port mappings

`$ docker container inspect --format '<format_template> <container_name>`

Use the above to read a specific setting from the json returned by 
the inspect command. To see the entire json, skip the format 
argument.

#### Show all networks present

`$ docker network ls`

#### Inspect properties of a network

`$ docker network inspect <network_name>`

#### Create a new network

`$ docker network create <new_network_name>`

This will create a new network with `bridge` driver.

When creating a new container the network to connect the container 
to can be specified using --network argument.

#### Connect a running container to a network

`$ docker network connect <network_name> <container_name>`

#### Disconnect a running container from the network

`$ docker network disconnect <network_name> <container_name>`

**TIP**: Use container name instead of IP addresse to refer to
a container from other containers.

**Note**: Learn the basics of Linux networking. (Subnets, DNS)

**Note**: The default bridge network does not have DNS built in.
Linking containers need to be done manually when containers are
run.

New networks created have DNS build in and can refer a container
using its name instead of its IP address.

### Implement DNS Round Robin

`$ docker container run -d --network {network_name} --network-alias {alias_name} {container_name}`

This command runs the container on a particular network and gives the 
container an alias that can be looked up from other containers.

Create multiple containers with same alias to create a round robin system.

`$ docker container run --rm --network {network_name} alpine nslookup {alias_name}`

This command will gives us dns lookup of a particular alias from a contianer on the same network