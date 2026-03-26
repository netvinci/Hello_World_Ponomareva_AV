#!/bin/bash
read -p "Введите вес в кг (целое число): " WEIGHT
read -p "Введите рост в м (целое число):" HEIGHT

BMI=$(($WEIGHT/ ($HEIGHT * $HEIGHT)))

echo "Ваш индекс массы тела: $BMI"
