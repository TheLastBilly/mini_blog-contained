#!/bin/sh

BUILD_DIR="/mnt/bb-build/mini_blog"
repo_source="git@github.com:TheLastBilly/mini_blog.git"

if [ -d "$BUILD_DIR" ]
then
    docker stop $(docker ps -a -q)
    rm -rf "$BUILD_DIR"
    mkdir "$BUILD_DIR"
else
    mkdir -p "$BUILD_DIR"
fi

ls "$BUILD_DIR"
git clone "$repo_source" "$BUILD_DIR"
docker-compose -f "$BUILD_DIR"/docker-compose.yml up -d --build
