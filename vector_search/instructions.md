
docker pull qdrant/qdrant

docker run -p 6333:6333 -p 6334:6334 -v "/tmp/qdrant_storage:/qdrant/storage:z" qdrant/qdrant

The second line in the docker run command mounts local storage to keep your data persistent. So even if you restart or delete the container, your data will still be stored locally.


6333 – REST API port
6334 – gRPC API port


$ uv venv
$ source .venv/bin/activate
(first_version) $ uv add qdrant-client[fastembed]>=1.14.2


$ import requests


