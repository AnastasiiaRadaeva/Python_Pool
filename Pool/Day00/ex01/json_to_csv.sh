#!/bin/bash
jq -r -f filter.jq ../ex00/hh.json > hh.csv
#-r - if the filter's result is a string then it will be written directly to standard output rather than being formatted as a JSON string