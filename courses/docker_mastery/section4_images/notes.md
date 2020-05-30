# Section 4 Notes

### Repository for Docker Images

`hub.docker.com`

### Pull an image from docker hub

`$ docker image pull {image_name}:{tag}`

**Tip**: Use the alpine based images to have a lightweight base image
to work on.

### Check the history of the docker image

`$ docker image history {image_name}:{tag}`

### Giving a new tag to an exisitng image

`$ docker image tag {source_image}:{tag_name} {new_source_image_name}:{tag_name}`

To publish this image to the docker hub

`$ docker image push {new_source_image_name}:{tag_name}`

### To create an image from a Dockerfile

`$ docker image build -t {image_name} .`