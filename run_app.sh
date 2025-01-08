#!/bin/bash
image="caesaraimusicstreamyt"
latest="latest"
# Test application
docker build -t palondomus/$image:$latest .
docker run -it -p 8080:8080 palondomus/$image:$latest