# JAAL - JSON-based Algorithm Animation Language

## Introduction

This repository contains technical documentation and other resources for JAAL,
the JSON-based Algorithm Animation Language. The language was developed as a
data format to store students' answers for Visual Algorithm Simulation
exercises, an interactive computer software to teach data structures and
algorithms.

JAAL has two versions: 1.0 (initial) and 1.1 (current).

For a quick demonstration, see the working [JSAV Player Test Application](https://jsav-player-test-app.web.app).

## JAAL 1.1

### Literature

Artturi Tilanterä, Giacomo Mariani, Ari Korhonen, Otto Seppälä. [Towards a JSON-based Algorithm Animation Language](https://doi.org/10.1109/VISSOFT52517.2021.00026) In *2021 Working Conference on Software Visualization (VISSOFT)*. IEEE, 2021.

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

Giacomo Mariani. [Design of an Application to Collect Data and Create Animations
from Visual Algorithm Simulation Exercises.](http://urn.fi/URN:NBN:fi:aalto-202005313418) Master's thesis, Aalto University School of Science, 2020.

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
