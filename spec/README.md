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
3. Install [json-schema-ref-parser](https://github.com/APIDevTools/json-schema-ref-parser)
   (e.g. from command line `npm install @apidevtools/json-schema-ref-parser`)

## Running tests

`./test.sh` tests the JAAL JSON Schema in individual JSON files against JSON
data in directory `test/`.

## Bundling

`./build.sh` uses *json-schema-ref-parser* to combine individual JAAL JSON
Schema files into a single file `bundle/jaal-bundle.json`.
