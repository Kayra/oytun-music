#!/usr/bin/env bash

export PGPASSWORD=development_password_only
psql -h localhost -d oytun_music -U oytun_music -p 5432 -a -w -f scripts/seed_db.sql