#!/bin/bash

check_root(){

if [ $EUID -ne 0 ]; then

echo "Ошибка! Скрипт должен быть запущен от имени суперпользователя"

fi
}
