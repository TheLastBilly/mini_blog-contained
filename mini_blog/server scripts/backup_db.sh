#!/bin/sh

BACKUPS="/mnt/db-backups/"
BACKUP_NAME="mini_blog"
IMAGE_NAME_WEB="mini_blog_web"
IMAGE_NAME_DB="mini_blog_db"

final_dir="$BACKUPS$BACKUP_NAME"
date=$(date +"%Y%m%d%H%M")

if [ -z ${BACKUPS+x} ]
then 
    echo "BACKUPS system variable not specified"
    exit 1
elif [ -z ${BACKUP_NAME+x} ]
then
    echo "BACKUP system variable not specified"
    exit 1
elif [ ! -d "$BACKUPS" ]
then
    mkdir -p "$final_dir"
fi

web=$(docker create "$IMAGE_NAME_WEB")
db=$(docker create "$IMAGE_NAME_DB")

mkdir -p "$final_dir"/"$date"/media
mkdir -p "$final_dir"/"$date"/postgresql/data

docker cp "$db":/var/lib/postgresql/data/ "$final_dir"/"$date"/postgresql/
docker cp "$web":/usr/src/app/media/ "$final_dir"/"$date"/

docker rm -v $web
docker rm -v $db

echo "Database backup ($date) completed successfully"
