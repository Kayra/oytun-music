#!/usr/bin/env bash
psql -c "create user oytun_music with password 'development_password_only'"
createdb -O oytun_music oytun_music;
