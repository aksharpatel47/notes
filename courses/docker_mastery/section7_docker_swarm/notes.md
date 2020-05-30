# Docker Swarm Node

Built-in orchestration tool. There are two types of nodes:

1. Manager Node
2. Worker Node

## Initialize Swarm

Run `docker swarm init` to create a swarm. This will output

`
Swarm initialized: current node (bvz81updecsj6wjz393c09vti) is now a manager.

To add a worker to this swarm, run the following command:

    docker swarm join \
    --token SWMTKN-1-3pu6hszjas19xyp7ghgosyx9k8atbfcr8p2is99znpy26u2lkl-1awxwuwd3z9j1z3puu7rcgdbx \
    172.17.0.2:2377

To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.
`

It creates a new node on the system and marks it as a leader. See nodes using `docker node ls` command.

## Docker Service

`docker container run` more geared towards a single container running on a single machine.

To run a container as a service on more than one node, create a service using `docker service create` command.

By default the service will run on a single node.

To update a running service to have multiple replicas, use the `docker service update --replicas` command. If multiple nodes are added to the system, the docker service will use those nodes to run the service. Otherwise, it will create replicas locally.

Update docker configuration options using `docker update` command.

To get the join-token for the swarm, run `docker swarm join-token` command.

Initially nodes join in the role of workers. They can be updated to the role of managers.