#!/bin/bash

df -h | awk 'NR>1 {print $1, $5}'
df -h | awk 'NR>1 && $5+0 > 90 {print "ВНИМАНИЕ:", $1, $5}'

