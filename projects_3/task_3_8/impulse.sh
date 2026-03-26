#!/bin/bash

read -p "Введите имя гена: " GENE_NAME

read -p "Введите экспрессию гена: " GENE_EXPRESSION

if [ -z "$GENE_NAME" ] || [ -z "$GENE_EXPRESSION" ]; then echo "Ошибка! Оба поля должны быть заполнены"; exit 1; fi

echo "Экспрессия гена $GENE_NAME составляет $GENE_EXPRESSION  единиц"
