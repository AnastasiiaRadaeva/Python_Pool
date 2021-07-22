#!/bin/sh
vacancy=${1/ /+}
curl "https://api.hh.ru/vacancies?text=$vacancy" | jq > hh.json
