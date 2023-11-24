# JAAL - JSON-based Algorithm Animation Language

## Introduction

**What** | The JSON-based Algorithm Animation Language (JAAL) is a data format
for representing students' solutions to algorithm visualization exercises.
In practice, it has been designed to record students' answers to interactive
exercises made with the [JSAV framework](http://jsav.io) that are included in
[OpenDSA electronic textbook](https://opendsa-server.cs.vt.edu/) . JAAL has a
formal specification in [JSON Schema](https://json-schema.org/).

**Why** | JAAL is intended to support [learning analytics](https://en.wikipedia.org/wiki/Learning_analytics) for
[algorithm visualization](https://dl.acm.org/doi/10.1145/1821996.1821997).

*Algorithm visualization* (or visual algorithm simulation) exercises are 
computerized exercises to teach data structures and algorithms at 
university-level computing education. An algorithm visualization exercise
displays the student a data structure, like array containing integers. The
student interacts with the visualization by changing the state of the data
structure, e.g. clicking array elements to swap their values. This way the
student simulates the steps of an algorithm, e.g. insertion sort.

*Learning analytics* means collecting data on students' actions in an
electronic learning environment for students and instructors to understand
learning. JAAL has two use cases. First, after a student has 
attempted to solve an algorithm visualization exercise, they could compare
their solution steps to the model answer to verify which in steps they
succeeded. Second, the course instructor or a researcher may study
students' incorrect solutions to an exercise to understand the mistakes
that students often make. This analysis supports improving the learning 
material and finding misconceptions related to a particular topic.

For more information, see the section [Scientific literature](#references).

**This git repository**

This repository contains technical documentation, specification and examples
for JSON-based Algorithm Animation Language (JAAL).


## Features

- Specification in [JSON Schema](https://json-schema.org/)
- Semantic data
  - Data structures: arrays (1D, 2D), lists, trees, graphs
  - Exercise instance (input to algorithm to be simulated)
  - Student's solution and Model solution events
    - click a data structure
    - undo    
    - event timing
- Graphical data
  - Embedded [SVG images](https://developer.mozilla.org/en-US/docs/Web/SVG):
    exercise instance, student's solution steps, model solution steps
- Extendable
    
- Flexible
  - Custom fields can be added (e.g. priority queue operations)
  - Recursive nesting of data structures
  - Format design is independent of JSAV

## Overview of schema

This section gives an overview of JAAL 2.0 JSON Schema structure along with
basic design principles of JAAL.

![SVG image of schema](doc/versions/2.0/JAAL-2.0-schema.svg)

The figure above is a top-level map of JAAL 2.0 JSON Schema. Each
yellow box with titles such as **initialState**, **animation**, e.g. are 
*subschemas*. The box with title **JAAL** is the top level schema.
Each subschema has *properties* (dictionary keys). The **JAAL** schema has
property `metadata` which has a *JSON Schema reference* to subschema
**metadata**.

The subschema **metadata** itself has properties such as `jaalVersion` and
`browser`. These may be numbers or string values. The `exercise` property
of the **metadata** subschema is a dictionary itself with keys `name`,
`collection`, and `runningLocation`.

The **initialState** subschema contains data structures represented in
algorithm visualization exercises. It is actually a list of data structures,
and each data structure must have the format of one of the subschemas
**node**, **graph**, or **matrix**.

The **event** subschema has property `object` which also refers to five
subschemas representing data structures (edge, node, graph, keyvalue, matrix).
However, here the arrow line is dashed, meaning it is a *JAAL id reference*.
Each JAAL data structure object has an `id` property which is a string.
This way instances of subschemas can refer to each other without having to
nest them: by default, an **event** refers to an existing data structure
defined in the **initialState** schema. 

(The C programming language analogy between a JSON Schema reference
and a JAAL id reference are structs and pointers.)

The JAAL 2.0 JSON Schema has five data structure schemas. The most atomic
data structure subschema is **node** which may either a graph node or a cell
in an array or matrix. Subschema **matrix** represents both one- and
two-dimensional arrays.

Subschema **graph** represents all kinds of linked,
expandable data structures: lists, trees, and graphs. Each graph contains a
set of **node**s and a set of **edge**s. Each edge is a pair of nodes.
Because directed graphs may have some bidirectional edges, it is conventional
to define separately the set of nodes and then refer to them by their `id`
properties in edges; this is why the `node` property of the **edge**
subschema is a JAAL ID reference and not a JSON Schema reference.

## Data Examples

See [examples/README.md](examples/README.md) for a full example on what kind of
exercises JAAL can record and what the data looks like.

See the subdirectory [spec/test/valid/](spec/test/valid/) for JAAL examples of
different data structures typically occurring in algorithm visualization
exercises. This test data has examples of:
- [linked list](spec/test/valid/graph-linkedlist-bidirectional.json)
- [binary search tree](spec/test/valid/graph-binary-search-tree.json)
- [red-black tree](spec/test/valid/graph-red-black-tree.json)
- [weighted graph](spec/test/valid/graph-undirected-weighted.json)
- [directed graph](spec/test/valid/graph-directed.json)
- [array](spec/test/valid/matrix-1d-vertical.json)
- [2D array](spec/test/valid/matrix-2d.json)

## Specification

The current version for JAAL is 2.0.

JAAL 2.0 has a formal specification in [JSON Schema](https://json-schema.org/).
The JSON Schema for JAAL is in the subdirectory `spec`.

JAAL 1.0 has no formal specification; it is implicitly specified by its
model implementation.

### Demonstrations

JAAL 2.0 can be tested with the testbench of
[JSAV Exercise Recorder](https://github.com/Aalto-LeTech/jsav-exercise-recorder/blob/jaal2.0/README.md#introduction-with-testbench).

[A demo of JAAL 1.0](https://jsav-player-test-app.web.app) features the
following exercises: Insertion Sort, Heap Build, Dijkstra's algorithm,
Evaluating Postfix Expression, and search in a Binary Search Tree.

### Software

#### JAAL 2.0

* [JSAV Exercise
  Recorder 2.0](https://github.com/Aalto-LeTech/jsav-exercise-recorder/tree/jaal2.0)
  (git branch `jaal2.0`) records at least Prim's and Dijkstra's JSAV exercises.
  See [Introduction with testbench](https://github.com/Aalto-LeTech/jsav-exercise-recorder/blob/jaal2.0/README.md#introduction-with-testbench) in the main README of the Exercise Recorder's repository.

* [JSAV Exercise Player
  2.0](https://github.com/Aalto-LeTech/jsav-exercise-player/tree/jaal2.0) (git
  branch `jaal2.0`) is designed to play JAAL 2.0 recordings. However, it is not
  under active development.

#### JAAL 1.0

* [JSAV Exercise Recorder](https://github.com/MarianiGiacomo/jsav-exercise-recorder/)
saves student's solution for a [JSAV](http://jsav.io)/[OpenDSA](https://opendsa-server.cs.vt.edu/) exercise as JAAL 1.0.

* [JSAV Exercise Player](https://github.com/MarianiGiacomo/jsav-exercise-player/)
plays a JAAL 1.0 recording.

* [JSAV Player Application Server](https://github.com/MarianiGiacomo/jsav-player-application-test-server) is the backend of the demonstration application. It implements an
exercise service which provides JSAV/OpenDSA exercises and stores JAAL 1.0
recordings.

* [JSAV Player Application Test App](https://github.com/MarianiGiacomo/jsav-player-application-test-app) is the frontend of the demonstration application.

## Scientific literature {#references}

### Algorithm visualization

Clifford A. Shaffer, Matthew L. Cooper, Alexander Joel D. Alon, Monika Akbar,
Michael Stewart, Sean Ponce, and Stephen H. Edwards. 2010. *Algorithm
Visualization: The State of the Field*. ACM Trans. Comput. Educ. 10, 3,
Article 9 (August 2010), 22 pages. https://doi.org/10.1145/1821996.1821997

### Students' errors in algorithm visualization

Otto Seppälä, Lauri Malmi, and Ari Korhonen. 2006. *Observations on student misconceptions—A case study of the Build – Heap Algorithm*. Computer Science Education, 16:3, 241-255. https://doi.org/10.1080/08993400600913523

Ville Karavirta, Ari Korhonen, and Otto Seppälä. 2013. *Misconceptions in Visual Algorithm Simulation Revisited: On UI's Effect on Student Performance, Attitudes and Misconceptions*. 2013 Learning and Teaching in Computing and Engineering, Macau, Macao, 2013, pp. 62-69, https://doi.org/10.1109/LaTiCE.2013.35

### JSAV and OpenDSA

Ville Karavirta and Clifford. A. Shaffer. 2016. *Creating Engaging Online
Learning Material with the JSAV JavaScript Algorithm Visualization Library*. In
IEEE Transactions on Learning Technologies, vol. 9, no. 2, pp. 171-183, 1
April-June 2016. https://doi.org/10.1109/TLT.2015.2490673

Ville Karavirta and Clifford A. Shaffer. 2013. *JSAV: the JavaScript algorithm visualization library*. In Proceedings of the 18th ACM conference 
on Innovation and technology in computer science education (ITiCSE '13). Association for Computing Machinery, New York, NY, USA, 159–164. https://doi.org/10.1145/2462476.2462487

Eric Fouh, Ville Karavirta, Daniel A. Breakiron, Sally Hamouda, Simin Hall,
Thomas L. Naps, Clifford A. Shaffer. 2014. *Design and architecture of an
interactive eTextbook – The OpenDSA system*. Science of Computer Programming,
Volume 88, 2014, Pages 22-40, ISSN 0167-6423.
https://doi.org/10.1016/j.scico.2013.11.040     



### Design and purpose of JAAL

To read more about the design and purpose of JAAL, see the following
publication.

Artturi Tilanterä, Giacomo Mariani, Ari Korhonen, Otto Seppälä. 2021. 
*Towards a JSON-based Algorithm Animation Language*. 2021 Working Conference 
on Software Visualization (VISSOFT), Luxembourg, 2021, pp. 135-139. https://doi.org/10.1109/VISSOFT52517.2021.00026

The first prototype of JAAL was originally developed as a master's thesis at
Aalto University.

Giacomo Mariani. 2020. *Design of an Application to Collect Data and Create
Animations from Visual Algorithm Simulation Exercises*. School of
Science, Aalto University. http://urn.fi/URN:NBN:fi:aalto-202005313418