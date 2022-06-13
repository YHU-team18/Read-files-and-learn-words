cd  docker_dir
docker build . -t yhu
docker run -it --rm -v ~/development/13_hacku/Read-files-and-learn-words/src:/code yhu
