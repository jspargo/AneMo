#!/usr/bin/env bash

name=AneMoSkill

zip -r $name.zip .
aws lambda update-function-code --function-name $name --zip-file fileb://$name.zip
