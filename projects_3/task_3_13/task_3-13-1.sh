#!/bin/bash

sudo sed -i 's|/var/lib/mysql/data|/mnt/ssd/mysql|g' settings.php
