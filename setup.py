from setuptools import setup

setup(
    name="touchid",
    py_modules=["touchid"],
    version="1.0.0",
    description="Access the Touch-ID sensor",
    long_description="`touchid` provides an easy to use API for accessing the Touch-ID sensor via Apple's LocalAuthentication framework",
    keywords=["touch-id", "LocalAuthentication", "LAContext"],
    license="MIT",
    author="Lukas Kollmer",
    author_email="lukas.kollmer@gmail.com",
    url="https://github.com/lukaskollmer/py-touch-id/",
    install_requires=["pyobjc"]
)