# REMLA Team 6's Version Library
This is the implementation of the library-version repository for CS4295 Release Engineering for Machine Learning Applications (Team 6) at TU Delft (Q4, 2024). This is a simple version aware library that can be queried to return it's current version. The package release workflow is automatically triggered when a new Git tag is pushed. We follow semantic versioning for the library in the format `v<major>.<minor>.<patch>`.
The package repository (PyPi) can be found [here](https://pypi.org/project/versioning-remla/).


# Installation
```console
pip install versioning-remla
```

# Usage
To get the current version using this package, execute the following lines in Python -
```python 
from versioning_remla.versioning import VersionUtil
util = VersionUtil()
print(util.get_version())
```