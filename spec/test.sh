#!/bin/bash

# ajv option -s: jaal.json is the main schema
# ajv option -r: files *.json but not jaal.json are part of the schema
# ajv option -d: directory for test data
echo "--- Valid schemas -----------------------------"

ajv test --spec=draft2020 -s schemas/attributeList.json \
  -d "test/valid/attributeList*.json" --valid

ajv test --spec=draft2020 -s schemas/edge.json \
  -r "schemas/attributeList.json" -d "test/valid/edge*.json" --valid

ajv test --spec=draft2020 -s schemas/graph.json \
  -r "schemas/{attributeList,edge,matrix,node}.json" -d "test/valid/graph*.json" --valid

ajv test --spec=draft2020 -s schemas/jaal.json -r schemas/metadata.json \
  -d "test/valid/jaal*.json" --valid

ajv test --spec=draft2020 -s schemas/matrix.json \
 -r "schemas/{attributeList,edge,graph,node}.json" \
 -d "test/valid/matrix*.json" --valid

ajv test --spec=draft2020 -s schemas/metadata.json -d "test/valid/metadata*.json" --valid

ajv test --spec=draft2020 -s schemas/node.json \
-r "schemas/{attributeList,edge,graph,matrix}.json" -d "test/valid/node*.json" --valid


echo "--- Invalid schemas -----------------------------"

ajv test --spec=draft2020 -s schemas/attributeList.json \
-d "test/invalid/attributeList*.json" --invalid --errors=text

ajv test --spec=draft2020 -s schemas/edge.json \
-r "schemas/attributeList.json" -d "test/invalid/edge*.json" --invalid

ajv test --spec=draft2020 -s schemas/jaal.json -r schemas/metadata.json \
-d "test/invalid/jaal*.json" --invalid --errors=text

ajv test --spec=draft2020 -s schemas/matrix.json \
 -r "schemas/{attributeList,edge,graph,node}.json" \
 -d "test/invalid/matrix*.json" --invalid

ajv test --spec=draft2020 -s schemas/metadata.json -d "test/invalid/metadata*" --invalid --errors=text

ajv test --spec=draft2020 -s schemas/node.json \
-r "schemas/{attributeList,edge,graph,matrix}.json" -d "test/invalid/node*.json" --invalid


# Bundle
#ajv test --spec=draft2020 -s bundle/jaal.json -d "test/valid/*.json" --valid
#ajv test --spec=draft2020 -s bundle/jaal.json -d "test/invalid/*.json" --invalid
