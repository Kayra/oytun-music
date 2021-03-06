#!/usr/bin/env bash

USER="test"
PASS="test"
MAIL="test@test.com"

script="
from django.contrib.auth.models import User;

username = '$USER';
password = '$PASS';
email = '$MAIL';

if User.objects.filter(username=username).count()==0:
    User.objects.create_superuser(username, email, password);
    print('Superuser created.');
else:
    print('Superuser creation skipped.');
"

printf "$script" | python oytun_music/manage.py shell
