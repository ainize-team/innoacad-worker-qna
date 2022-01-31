#!/bin/bash

dockerize -wait tcp://database:3306 -timeout 10s

echo "Apply Database Migration"
alembic upgrade head