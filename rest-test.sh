#!/bin/bash

#curl -H "Accept: application/json" -H "Content-Type: application/json" -X POST "http://localhost:5000/sentiment"   -d '{ "workload": ["Jag älskar denna produkt", "Jag hatar denna produkt"]}'
curl -H "Accept: application/json" -H "Content-Type: application/json" -X POST "http://localhost:8092/encoding"   -d '{ "workload": "Jag älskar denna produkt"}'
