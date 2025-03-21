#!/bin/bash

# Run Python setup.py to create source distribution and wheel
python setup.py sdist bdist_wheel
twine upload dist/*