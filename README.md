# msbio.py
## Description
A module for reading/writing 'settings.bin' from Mindustry Server.

## Installation
```shell
pip install msbio
```

## Using
```python
import msbio

with open('settings.bin', 'rb') as file:
    data = msbio.load(file)
```