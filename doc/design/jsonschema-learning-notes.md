# Artturi's personal notes about JSON Schema
29.6.2021

## Basic understanding of JSON schema

Notes from https://json-schema.org/understanding-json-schema/

- `uri`: URI (URL)  (draft 6)
- `pattern`: regular expressions
- `title` and `description` are optional, but recommended
- `examples` provide example data for documentation
- `enum`: enumerated values
- `contentMediaType`: XML inside JSON
- `$ref` allows referring to a sub-schema in the same file, e.g.
       `"$ref": "#/definitions/address"`

Do not use these at least for now:
- `dependencies`: one property may require others. Let's not put restrictions
before the specification is mature. This might be future stuff:  when it is
declrated that the *interpretation* of some data structure represented in
JAAL is a, e.g. binary tree, one could require at most two children for each
node.

- `allOf`, `anyOf`, `not`, `if`-`then`-`else`: other advanced rules for
  structure; let's not use them for now.

JAALin JSON-skeema yhdessä tiedostossa vs. useammassa

## One or many schema files?

One file
--------
+ faster to retrieve with a single HTTP request

Many files
----------------
+ git show which subschemas (modules) have changed
+ smaller file size -> easier to navigate
+ module-based testing
  + each test data file contains only the essential data, not a whole
    mockup JAAL recording
  + ideally, modifying one module should not change the unit tests of
    other modules
+ multiple schema files can be combined to a single one with a JSON
  Schema bundler euch as    
   https://www.npmjs.com/package/gulp-jsonschema-bundle
