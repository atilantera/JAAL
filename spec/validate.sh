#!/bin/sh
echo "--- Valid schemas -----------------------------"
ajv --spec=draft2020 -s jaal-1.1.json -d "test/valid/*.json"
echo "--- Invalid schemas -----------------------------"
ajv --spec=draft2020 -s jaal-1.1.json -d "test/invalid/*.json"
