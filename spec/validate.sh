#!/bin/sh
echo "--- Valid schemas -----------------------------"
ajv test --spec=draft2020 -s jaal-1.1.json -d "test/valid/*.json" --valid
#ajv --spec=draft2020 --errors=text -s jaal-1.1.json -d "test/valid/*.json"
echo "--- Invalid schemas -----------------------------"
ajv test --spec=draft2020 -s jaal-1.1.json -d "test/invalid/*.json" --invalid
#ajv --spec=draft2020 --errors=text -s jaal-1.1.json -d "test/invalid/*.json"
