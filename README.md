# TD7A4

This repository contains a flask app that will be used in order to try docker for the CC course at ESILV in A4 CCC.

This app creates a simple web page that will display the content of the file ***file.txt*** in the root directory of the project and an element of the collection in the database linked. this element is created in the ***app.py*** file.

In order to run this container it is necessary to have docker installed on your machine.

## To install docker
-> https://docs.docker.com/engine/install/

## To run the container

In order to run the container you need to run the following command:

```bash
docker-compose up -d --build
```

this command will build the image and run the two containers with the different information provided in the docker-compose.yml file.


