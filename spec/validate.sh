#!/bin/sh
ajv --spec=draft2020 -s jaal.json -d test/valid/*.json
