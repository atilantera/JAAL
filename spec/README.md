# JAAL specification

## Directory contents

This directory contains the specification for JAAL as
[JSON schema](https://json-schema.org).

- test/     : test data to validate against the schema
- jaal.json : The JSON schema of JAAL
- README.md : this file

## Software requirements

JAAL is specified with [JSON schema](https://json-schema.org).
The schemas can be easily validated with the command-line tool *ajv-cli*.

1. Install [node.js](https://nodejs.org).
2. Install [ajv-cli](https://www.npmjs.com/package/ajv-cli)
   (e.g. from command line `npm install -g ajv-cli`)
3. Validate from command line:
   - `ajv -s jaal.json -d test/valid/*.json`
   - `ajv -s jaal.json -d test/invalid/*.json`
