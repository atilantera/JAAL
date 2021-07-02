# JAAL specification

## Directory contents

This directory contains the specification for JAAL as
[JSON schema](https://json-schema.org).

- bundle/jaal.json: The JSON Schema of JAAL in a single file (bundle)
- schemas/ : The JSON schema of JAAL as separate modules
- test/     : test data to validate against the schema
- bundle.js: compiles *.json into bundle/jaal.json
- *.sh: convenience scripts
- README.md : this file

## Software requirements

### Installation

JAAL is specified with [JSON schema](https://json-schema.org).
The schemas can be easily validated with the command-line tool *ajv-cli*.

1. Install [node.js](https://nodejs.org).
2. Install [ajv-cli](https://www.npmjs.com/package/ajv-cli)
   (e.g. from command line `npm install -g ajv-cli`)
3. Install [json-schema-ref-parser](https://github.com/APIDevTools/json-schema-ref-parser)
   (e.g. from command line `npm install @apidevtools/json-schema-ref-parser`)

The convenience scripts *test.sh* and *build.sh* require
[Bash](https://www.gnu.org/software/bash/), but one can easily do without it;
see the contents of those files.

### Versions

The schemas have been tested with the following software.

node.js 12.16.3
ajv-cli 5.0.0
json-schema-ref-parser 9.0.9

## Running tests

`./test.sh` tests the JAAL JSON Schema in individual JSON files against JSON
data in directory `test/`.

## Bundling

`./build.sh` uses *json-schema-ref-parser* to combine individual JAAL JSON
Schema files into a single file `bundle/jaal-bundle.json`.

## Running tests

Do the bundling first. Then `./test.sh` tests the JAAL JSON Schema in
individual JSON files against JSON data in directory `test/`.
