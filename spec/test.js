const Ajv2020 = require("ajv/dist/2020");
const { assert } = require("console");
const fs = require("fs");
var tests_passed = 0;
var tests_failed = 0;

/**
 * create_tests finds the test cases for the schema as located in 
 * /tests/valid and /tests/invalid. For each of the test cases, 
 * it calls validate_schema with the required parameters, and 
 * asserts that the expected outcome is met. 
 * @param schema_name takes the name of the root schema. 
 * @param validity takes "valid" or "invalid", 
 * to check if a file is valid or invalid. This is also the folder
 * in which the test files are found.
 * @param dependencies takes a list of strings, on which the root 
 * schema is dependant. This is just the filenames, without extension. 
 * If the schema is dependent on jaal.json, dependencies = ["jaal"].
 */

const create_tests = (schema_name, validity, dependencies) => {
    const schema = require("./schemas/"+schema_name+".json");
    const files = fs.readdirSync("./test/" + validity)
                    .filter(fn => fn.startsWith(schema_name));
    if (dependencies === undefined) {
        dependent_on = [];
    } else {
        dependent_on = expand_dependencies(dependencies);
    }
    for (var i = 0; i < files.length; i++) {
        if (validity === "valid") {
            assert(validate_schema(schema, files[i], validity, dependent_on));
        } else {
            assert(!validate_schema(schema, files[i], validity, dependent_on));
        }
    }
}

/**
 * expand_dependencies takes a list of partial file names, 
 * and expands this into the full path of the file:
 * schemas/{file_name}.json, where {file_name}
 * is the name of a partial file name.
 * @param dependencies takes a list of file names.
 * @returns a list of expanded file names.
 */

const expand_dependencies = (dependencies = []) => {
    var deps = [];
    for (var i = 0; i < dependencies.length; i++) {
        const dependency = "./schemas/" + dependencies[i] +".json";
        deps.push(require(dependency));
    }
    return deps;
}


/**
 * validate_schema creates an ajv instance and validates the provided
 * test_file against the JAAL schema provided to determine whether 
 * it is valid JAAL. 
 * @param schema is the schema file. 
 * @param test_file is the file to be verified if it is valid JAAL.
 * @param validity takes the values "invalid" or "valid",
 * to check if a file is valid or invalid. This is also the folder
 * in which the test_file is found.
 * @param dependencies is a list of dependencies of the schema.
 * If empty, schema has no dependencies.
 * @returns a boolean of whether test_file is valid JAAL. 
 */

const validate_schema = (schema, test_file, validity, dependencies = []) => {
    const ajv = new Ajv2020();
    var validate;
    if (dependencies.length > 0) {
        validate = ajv.addSchema(dependencies).compile(schema);
    } else {
        validate = ajv.compile(schema);
    }
        
    filename = "./test/" + validity + "/" + test_file;
    test_case = require(filename);
    
    const valid = validate(test_case);

    if (valid) {
        if (validity === "valid") {
            tests_passed++;
        } else {
            const file = "/" + validity + "/" + test_file;
            console.log("Test", file, 
                        "passed validation although it should not.");
            tests_failed++;
        }
    } else {
        const file = "/" + validity + "/" + test_file;
        if (validity === "valid") {
            console.log("Test", file, 
                        "failed validation although it should not.");
            console.log(validate.errors); 
            tests_failed++;   
        } else {
            console.log("Test " + file +  ":");
            console.log(validate.errors);
            tests_passed++;
        }
        
    }
    return valid;
};


const valid_edge_tests = () => {
    create_tests("edge", "valid");
};


const valid_event_tests = () => {
    create_tests("event", "valid"); 
};


const valid_definitions_tests = () => {
    create_tests("definitions", "valid", ["event", "style"]);
}

const valid_graph_tests = () => {
    create_tests("graph", "valid", ["edge", "keyvalue", "matrix", "node"]);
}


const valid_initialState_tests = () => {
    create_tests("initialState", "valid", 
                ["edge", "keyvalue", "graph", "matrix", "node"]);
}


const valid_jaal_tests = () => {
    create_tests("jaal", "valid", 
                ["definitions", "edge", "event", "graph", "initialState", 
                "keyvalue", "matrix", "metadata", "node", "style"]);
}


const valid_keyvalue_tests = () => {
    create_tests("keyvalue", "valid", ["edge", "graph", "matrix", "node"]);
}

const valid_matrix_tests = () => {
    create_tests("matrix", "valid", ["edge", "keyvalue", "graph", "node"]);
}

const valid_metadata_tests = () => {
    create_tests("metadata", "valid");
}

const valid_node_tests = () => {
    create_tests("node", "valid", ["edge", "graph", "keyvalue", "matrix"]);
}


const valid_style_tests = () => {
    create_tests("style", "valid");
}


const invalid_definitions_tests = () => {
    create_tests("definitions", "invalid", ["event", "style"]);
}


const invalid_edge_tests = () => {
    create_tests("edge", "invalid");
}


const invalid_event_tests = () => {
    create_tests("event", "invalid");
}


const invalid_graph_tests = () => {
    create_tests("graph", "invalid", ["edge", "keyvalue", "matrix", "node"]);
}

const invalid_initialState_tests = () => {
    create_tests("initialState", "invalid", 
                ["edge", "keyvalue", "graph", "matrix", "node"]);
}

const invalid_jaal_tests = () => {
    create_tests("jaal", "invalid", 
                ["definitions", "edge", "event", "graph", "initialState", 
                "keyvalue", "matrix", "metadata", "node", "style"]);
}


const invalid_keyvalue_tests = () => {
    create_tests("keyvalue", "invalid", ["edge", "graph", "matrix", "node"]);
}


const invalid_matrix_tests = () => {
    create_tests("matrix", "invalid", ["edge", "graph", "keyvalue", "node"]);
}


const invalid_metadata_tests = () => {
    create_tests("metadata", "invalid");
}


const invalid_node_tests = () => {
    create_tests("node", "invalid", ["edge", "graph", "keyvalue", "matrix"]);
}


const invalid_style_tests = () => {
    create_tests("style", "invalid");
}


function main() {
    valid_edge_tests();
    valid_event_tests();
    valid_definitions_tests();
    valid_graph_tests();
    valid_initialState_tests();
    valid_jaal_tests();
    valid_keyvalue_tests();
    valid_matrix_tests();
    valid_metadata_tests();
    valid_node_tests();
    valid_style_tests();

    invalid_definitions_tests();
    invalid_edge_tests();
    invalid_event_tests();
    invalid_graph_tests();
    invalid_initialState_tests();
    invalid_jaal_tests();
    invalid_keyvalue_tests();
    invalid_matrix_tests();
    invalid_metadata_tests();
    invalid_node_tests();
    invalid_style_tests();
    
    console.log(String(tests_passed), "tests passed,", 
                String(tests_failed), "tests failed");
}


if (require.main === module) {
    main();
}
