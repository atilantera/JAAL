# JAAL - JSON-based Algorithm Animation Language

## Introduction

This repository contains technical documentation, specification and examples
for JSON-based Algorithm Animation Language (JAAL). The language is intended
to support computing education research in universities. JAAL is a JSON-based
data format to store students' answers to visual algorithm simulation /
algorithm visualization exercises. In practice, it has been designed to
record students' answers to interactive exercises made with
[http://jsav.io](JSAV) that are included in
[https://opendsa-server.cs.vt.edu/](OpenDSA) .

## Features

- Specification in [JSON Schema](https://json-schema.org/)
- Semantic data
  - Data structures: arrays (1D, 2D), lists, trees, graps
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

## Data Examples

See [examples/README.md](examples/README.md) for a full example on what kind of
exercises JAAL can record and what the data looks like.


## Scientific Literature

To read more about the design and purpose of JAAL, see the following
publication.

Artturi Tilanterä, Giacomo Mariani, Ari Korhonen, Otto Seppälä. [Towards a JSON-based Algorithm Animation Language](https://doi.org/10.1109/VISSOFT52517.2021.00026) In *2021 Working Conference on Software Visualization (VISSOFT)*. IEEE, 2021.

The first prototype of JAAL was originally developed as a master's thesis at
Aalto University: Giacomo Mariani. [Design of an Application to Collect Data and Create Animations
from Visual Algorithm Simulation Exercises.](http://urn.fi/URN:NBN:fi:aalto-202005313418) Master's thesis, Aalto University School of Science, 2020.

## Specification

The current version (year 2023) for JAAL is 2.0.

Features



### Specification

This Github repository contains the specification and design documents for
JAAL 1.1, the JSON-based Algorithm Animation Language.

### Software

Currently there is no software supporting JAAL 1.1.

## JAAL 1.0



### Demonstration

[A demo of JAAL 1.0](https://jsav-player-test-app.web.app) features the
following exercises: Insertion Sort, Heap Build, Dijkstra's algorithm,
Evaluating Postfix Expression, and search in a Binary Search Tree. The

### Literature



### Specification

JAAL 1.0 has no formal specification; it is implicitly specified by its
model implementation (software).

### Source Code

* [JSAV Exercise Recorder](https://github.com/MarianiGiacomo/jsav-exercise-recorder/)
saves student's solution for a [JSAV](http://jsav.io)/[OpenDSA](https://opendsa-server.cs.vt.edu/) exercise as JAAL 1.0.

* [JSAV Exercise Player](https://github.com/MarianiGiacomo/jsav-exercise-player/)
plays a JAAL 1.0 recording.

* [JSAV Player Application Server](https://github.com/MarianiGiacomo/jsav-player-application-test-server) is the backend of the demonstration application. It implements an
exercise service which provides JSAV/OpenDSA exercises and stores JAAL 1.0
recordings.

* [JSAV Player Application Test App](https://github.com/MarianiGiacomo/jsav-player-application-test-app) is the frontend of the demonstration application.
