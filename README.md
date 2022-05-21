# Sliding Puzzle

A 4x4 board of numbered tiles has one missing space and is randomly set up. To win the game, the player must slide tiles over to put the tiles back in order.

This is one of my "Weekend Game" projects.
A "Weekend Game" is a small game idea that I implement in a single weekend using latest Python and Kivy framework.
Goal is to keep my software design & development skills up to date.

# Using

## Setting Up
    git clone git@github.com:jnmbk/wg-slidepuzzle.git
    cd wg-slidepuzzle
    pip install -e .

## Running
    python -m game.main

## Building for Android
    pip install buildozer cython
    buildozer android debug deploy run

![Tests](https://github.com/jnmbk/wg-slidepuzzle/actions/workflows/tests.yml/badge.svg)
