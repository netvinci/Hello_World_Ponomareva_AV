#!/bin/bash

for i in {1..10}; do

> test$i.txt
echo "+ test$i.txt"

done

i=10
while (( i>=1 )); do

if [ -e "test$i.txt" ]; then
rm test$i.txt
echo "- test$i.txt"
fi

((i--))

done
