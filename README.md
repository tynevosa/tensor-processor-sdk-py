# Tensor Processor SDK - Python

## Requirements

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/tynevosa/tensor-processor-sdk-py.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/tynevosa/tensor-processor-sdk-py.git`)

Then import the package:
```python
import tensor_processor 
```

### setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools)

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import tensor_processor
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from tensor_processor import Tpu

client = Tpu(apiKey=YOUR_TPU_API_KEY)

output = client.prediction(
  model="Stable Lightning",
  input={
    "prompt": "a panda eating bamboo"
  }
)

print(output)
```
