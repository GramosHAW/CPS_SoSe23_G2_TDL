#!/usr/bin/env bash

BASE_DIR="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )/../src/"

echo "Starting auto rebuild..."
docker stop auto
docker rm auto
docker rmi auto:0.1

docker build ${BASE_DIR}auto -t auto:0.1
echo -e "\n\n"

echo "Starting auto..."
docker run -d --net=cps-net --name auto auto:0.1