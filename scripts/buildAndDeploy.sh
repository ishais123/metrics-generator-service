#!/bin/bash

VERSION=$1

docker build -t metrics-generator:"$VERSION" .
docker tag metrics-generator:"$VERSION" ishais/metrics-generator:"$VERSION"
docker push ishais/metrics-generator:"$VERSION"

helm upgrade --install \
metrics-generator metrics-generator \
--set image.tag="$VERSION" \
--create-namespace -nmetrics-generator