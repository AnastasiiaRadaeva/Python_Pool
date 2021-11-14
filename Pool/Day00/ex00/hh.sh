#!/bin/bash
vacancy=${1/ /+} #change " " to "+" for request
curl "https://api.hh.ru/vacancies?text=$vacancy" | jq '.items[0:20]' > hh.json #take the first 20 objects from response
