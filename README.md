# pyzipper

pyzipper is a Python library for working with ZIP archives with improved encryption support, including AES encryption compatible with common ZIP tools.

Features
- Create and extract ZIP archives.
- Read and write encrypted ZIP archives (traditional and AES).
- Stream files into/out of ZIP archives.
- Simple, Pythonic API compatible with the stdlib zipfile where possible.

Installation

Install from PyPI:

pip install pyzipper

Usage

Basic modern AES-encrypted write:

```py
import pyzipper

with pyzipper.AESZipFile('secret.zip', 'w', compression=pyzipper.ZIP_DEFLATED,
                         encryption=pyzipper.WZ_AES) as zf:
    zf.setpassword(b'my-password')
    zf.writestr('hello.txt', 'Hello, world!')
```

Extracting:

```py
import pyzipper

with pyzipper.AESZipFile('secret.zip') as zf:
    zf.setpassword(b'my-password')
    print(zf.read('hello.txt').decode())
```

Compatibility

pyzipper aims to be a drop-in replacement for the standard library zipfile where feasible, while adding support for AES-encrypted ZIPs and a few convenience helpers.

Contributing

Contributions are welcome — please open issues or pull requests. When contributing, include tests and follow existing code style.

License

Include your project license here (e.g., MIT).