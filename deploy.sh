#!/usr/bin/env bash
# prod: ./deploy.sh 

PROJECT=ubuntu

# build docker images
docker build -t $PROJECT:20.04 . -f Dockerfile.prod

echo "Listings docker images from project $PROJECT"
docker images $PROJECT

if [[ $? == '0' ]]; then
    echo "Deployment was done sucesfully.."
fi
