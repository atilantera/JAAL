const $RefParser = require("@apidevtools/json-schema-ref-parser");

async function bundle(mainSchema) {
  let schema = await $RefParser.dereference(mainSchema);
  let bundled = await $RefParser.bundle(schema);
  console.log(JSON.stringify(bundled));
}

bundle("jaal.json");
