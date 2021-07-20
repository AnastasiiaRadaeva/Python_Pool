#!/bin/sh

jq -r '.|{id, created_at, name, has_test, alternate_url}' ../ex00/hh.json > hh.csv