# Representation of exercise data structures in JAAL

This document describes how exercise-bound generic data structures
should be represented in JAAL.

## Lists

Lists are implemented with the Graph schema.

## Trees

Trees are implemented with the Graph schema.

### Search trees

Search trees have one node as the root. This is determined by the **root**
property.

Each node may have children. Each node has order for its children: in a binary
search tree, there are left and right child. This is determined by the
**relation** property. Example: [graph-binary-search-tree.json](../spec/test/valid/graph-binary-search-tree.json)
