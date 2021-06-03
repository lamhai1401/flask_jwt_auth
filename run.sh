#!/bin/bash

sudo docker stop $(sudo docker ps -a -q)
sudo docker rm $(sudo docker ps -a -q)

export APP_SETTINGS="project.server.config.DevelopmentConfig"

docker run --name jwt_auth -e POSTGRES_PASSWORD=mypassword -p 5432:5432 -d postgres:12.3-alpine

psql -h localhost -p 5432 --username=postgres --password

# create database flask_jwt_auth;
# CREATE DATABASE
# create database flask_jwt_auth_test;
# CREATE DATABASE
# \q