# Dockerizing Flask with Mysql, and Traefik by using docker-compose

## Want to use this project?



Build the images and spin up the containers:

we created new volume (dump-sql), and new network (private-flask) and connect the flask-app and 
the DB with the same network
```sh
$ docker-compose up -d --build
```

Test it out:

1. [http://localhost:8080/](http://localhost:8080/)
1. [http://localhost:8081/](http://localhost:8081/)



