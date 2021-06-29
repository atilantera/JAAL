#!/bin/bash

# ajv option -s: jaal.json is the main schema
# ajv option -r: files *.json but not jaal.json are part of the schema
# ajv option -d: directory for test data
echo "--- Valid schemas -----------------------------"
ajv test --spec=draft2020 -s jaal.json -r "!(jaal).json" \
-d "test/valid/*.json" --valid

echo "--- Invalid schemas -----------------------------"
ajv test --spec=draft2020 -s jaal.json -r "!(jaal).json" \
-d "test/invalid/*.json" --invalid
