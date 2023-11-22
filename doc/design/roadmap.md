# JAAL roadmap

This file discusses JAAL + JSAV Exercise Recorder + JSAV Exercise Player
versions and their planned features.

## Version 1.1

- development: May-June 2022

- Incompatible with JAAL 1.0
- specification  
  - major JAAL redesign
  - JSON Schema: formal specification, test data
  - Recorder: automatic validation of generated JAAL data against JSON Schema
- semantics
  - compact, purely semantic representation of data structures
- graphics
  - compact, purely graphic representation of student's answer and model answer
    as SVG
- supported JSAV exercises
  - Dijkstra's algorithm

## Version 2.0

- development: June-July 2022

- Continues from JAAL 1.1
- semantics
  - nested steps
    - model answer: save JSAV gradeable-step as major step, other steps
      as minor steps, each inside one major step
    - player: match gradeable-step major steps
- graphics
  - SVG compression: save only changing SVG data between steps
- reintegrate Recorder and Player into A+ LMS
- supported JSAV exercises
  - Prim's algorithm

## Version 2.1

- development: July-August 2022

- supported JSAV exercises
  - Depth-first search
  - Breadh-first search
  - Kruskal's algorithm
- user interface
  - player: vertical timeline view
    - diverging point between student's answer and model answer
    - matching major steps (JSAV gradeable-step)
      - display minor steps in timeline

## Version 2.2

- supported JSAV exercises
  - Evaluating Postfix Expression
  - Infix to Postfix
