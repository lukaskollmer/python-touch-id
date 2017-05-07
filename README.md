# python-touch-id [![PEP8](https://img.shields.io/badge/PEP8-compliant-brightgreen.svg)](https://www.python.org/dev/peps/pep-0008/)

> Access the Touch ID sensor from Python

## Install

```bash
$ pip install touchid
```


## Usage

```python
import touchid

success = touchid.authenticate()
```

## API

#### `touchid.is_available()`
Check whether Touch ID is available on the current machine


#### `touchid.authenticate(reason='authenticate via Touch ID')`
Authenticate via Touch ID.  
This method returns a `bool` determining whether the Touch ID authentication completed successfully.
If the user cancels the authentication, this method will raise an Exception

## License

MIT © [Lukas Kollmer](https://lukas.vip)
