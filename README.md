# DEMO PACKAGE

Minimum example of conda-build and GitHub actions for pure Python demos.
The project is motivated by the need to build self-contained visual
examples using `numpy`, `numba`, `matplotlib`, `pygame`, `opencv`.

Demo can be invoked in several ways:

1. Cloning Github repo and running `python demo.py`
2. Running `python -m demo_module`
3. Installing conda package and invoking executable
   * `conda install -c pycoddiy/label/dev demo_pkg`
   * `demo_entry`

## Project structure

The demo project is composed as follows

```commandline
  conda-bld-example  # Project root directory
    conda-recipe  # Files required for conda-build
      conda_build_config.yaml  # Specifies build variants
      meta.yaml  # Specifies build/test/run steps, dependencies, and package meta-data
    demo_module  # Python module being wrapped into package demo_pkg
      tests  # Tests to be run with pytest
        test1.py
        ...
      impl  # Implementations sub-module
        __init__.py  # Required for each (sub-)module
        arg_parse.py  # Argument parsing
        compute.py  # Computation
        visualize.py  # Visualization implementation
      __init__.py  # Required for each (sub-)module
      __main__.py  # Required to run as python -m demo_module
      main_demo.py  # Main script containing main() function
    demo.py  # Script that imports demo_module for execution
    LICENSE  # License file required by conda-build
    README.md  # Readme file containing these instructions
    setup.py  # Required by conda-build
```
It is recommended that you will follow similar project structure
to simplify creation of new demos.

Good luck!