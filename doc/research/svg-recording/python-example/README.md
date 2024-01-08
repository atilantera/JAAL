# Python example of creating an SVG image

## Purpose

This code is a proof of concept to show that recording JSAV-produced
HTML + CSS + SVG code as pure SVG should result in rather compact data,
in order of kilobytes.

## Files

`example1.png` is a screen from the research version of Dijkstra's algorithm
exercise. It only contains a graph with 16 nodes and 19 edges produced with
JSAV.

`createsvg.py` is a Python program with utilizes the
[svgwrite library](https://pypi.org/project/svgwrite/) to produce a SVG
reconstruction of `example1.png`.

`example1.svg` is the SVG reconstruction of `example1.png`.

## Further information

This code was further developed here:
https://version.aalto.fi/gitlab/atilante/dijkstra-misconceptions/-/blob/main/data/jaalhtmlparser.py

