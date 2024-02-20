#!/bin/bash

VERSION=$1

helm upgrade --install \
metrics-generator metrics-generator \
--set image.tag="$VERSION" \
--create-namespace -nmetrics-generator