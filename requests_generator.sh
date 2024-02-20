#!/bin/bash

while true;
do
  sleep 3;
  curl localhost:5001/health;
  curl localhost:5001/alive;
  curl localhost:5001/alive;
  curl localhost:5001/bad;
done;