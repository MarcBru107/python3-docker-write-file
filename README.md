# python3-docker-write-file


### writing a file in the host system using a python script in a Docker container

Build:
docker build -t py-write .

Run:
docker run -v ${PWD}/data:/data py-write
