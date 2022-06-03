const Ajv2020 = require("ajv/dist/2020");
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
        validate_schema(schema, files[i], validity, dependent_on);
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
 * validate_schema creates an ajv instance and validates the provided test_file
 * against the JAAL schema provided to determine whether it is valid JAAL.
 * @param schema is the schema file.
 * @param test_file is the file to be verified if it is valid JAAL.
 * @param validity takes the values "invalid" or "valid",
 * to check if a file is valid or invalid. This is also the folder
 * in which the test_file is found.
 * @param dependencies is a list of dependencies of the schema.
 * If empty, schema has no dependencies.
 *
 * Increases global variables:
 * - Increase tests_passed if:
 *   - a test expected passing passed validation;
 *   - a test expected failing fails validation with the expected error
 *     location and error message.
 * - Increase tests_failed if:
 *   - a test expected passing fails validation;
 *   - a test expected failing passes validation;
 *   - a test expected failing fails validation, but either the error location
 *     or message differs from the expected one.
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

    const validation_passed = validate(test_case);

    if (validation_passed) {
        if (validity === "valid") { // Expect valid, validation passed
          tests_passed++;
        } else {                    // Expect valid, validation failed
            const file = "/" + validity + "/" + test_file;
            console.log("Test", filename, "should not pass validation!");
            tests_failed++;
        }
    } else {
        if (validity === "valid") { // Expect invalid, validation passed
            console.log("Test", file, "should not fail validation!.");
            console.log(validate.errors);
            tests_failed++;
        } else {                    // Expect invalid, validation failed
            /* Expected error location and message */
            const expected_path = test_case.errorInstancePath;
            const expected_msg  = test_case.errorMessage;
            /* ajv-produced error location and message */
            const found_path = validate.errors[0].instancePath;
            const found_msg = validate.errors[0].message;

            if (expected_path === found_path && expected_msg === found_msg) {
                tests_passed++;
            } else {
                console.log("Test ", filename, ":");
                console.log("  Expected error:", expected_path, expected_msg);
                console.log("  Found error   :", found_path, found_msg)
                tests_failed++;
            }
        }
    }
};


const valid_edge_tests = () => {
    create_tests("edge", "valid");
};


const valid_event_tests = () => {
    create_tests("event", "valid");
};


const valid_definitions_tests = () => {
    create_tests("definitions", "valid", ["event"]);
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
                "keyvalue", "matrix", "metadata", "node"]);
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


const invalid_definitions_tests = () => {
    create_tests("definitions", "invalid", ["event"]);
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
                "keyvalue", "matrix", "metadata", "node"]);
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


function main() {
    const test_time = "Tests run in";
    console.time(test_time);

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

    console.timeEnd(test_time);

    console.log(String(tests_passed), "tests passed,",
                String(tests_failed), "tests failed");
}


if (require.main === module) {
    main();
}
