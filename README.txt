docker build -t hot .
docker run -ti --rm -v ${PWD}:/hotel hot
