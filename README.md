# Wossname

Thing with name.

[![Build Status on Travis](https://travis-ci.org/aptivate/wossname.svg?branch=master)](https://travis-ci.org/aptivate/wossname)

## Purpose

An app for things with names.

## Contents

The Github project contains the following files and directories:

* wossname: the app which you can add to `INSTALLED_APPS` in Django.
  * models.py: Contains a named item model.

* tests: A test project which includes the wossname app, some models and tests.

## Usage

### With DYE

To add `wossname` to your DYE project:

* add this line to `deploy/pip_packages.txt`:
    -e git+https://github.com/aptivate/wossname.git
* run `deploy/bootstrap.py`

### Manual Installation

If you're not using DYE, then install `wossname` in your global Python
environment or virtualenv:

    pip install wossname

Or if it's not available on PyPI, or you need a newer version:

    pip install -e git+https://github.com/aptivate/wossname.git

Of course you need [Django](https://www.djangoproject.com/)
(1.5 or higher)

### Using the Model

To use the model in your project:

    from wossname.models import Wossname 

Then make a ForeignKey eg Catagories or Types, that points to Wossname:

    types = models.ForeignKey(Wossname)

### Add to `INSTALLED_APPS`

Add `wossname` to `INSTALLED_APPS` in your project's `settings.py` file:

    INSTALLED_APPS = (
        ...
        'wossname',
    )

### Running the tests

You can clone the project from GitHub and run the tests manually with the
`tox` command, which installs all the test dependencies for you:

    tox

This will test with Python 2.6 and 2.7, so you'll need both installed. If
you just want to test one environment (which is faster and doesn't require
two Pythons to be installed) you can do this:

    tox -e py27-django16
