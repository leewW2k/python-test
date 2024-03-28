.. _getting-started:

Getting started
===============

This chapter introduces some the use of Syncpos FastAPI back end.

Syncpos requires Python 3.11 or later to run.


Virtual Environment
*******************

Setting up a new virtual environment is recommended:

[For Windows]

Go to the root folder of your project and run:

.. code-block:: shell

    $ python -m venv venv

After a venv folder is created, activate the virtual environment:

.. code-block:: shell

    $ mypy program.py
    $ activate

Setting up dependencies
***********************

Set up dependencies by running:

.. code-block:: shell

    $ pip install -r requirements/dev.txt

Running FASTAPI server locally
******************************

To run the server locally:

.. code-block:: shell

    $ uvicorn src.main:ApiClient --reload --host localhost --port 8888

The ``--reload`` flag reloads the server when changes are saved.

After running the server, you can check the SWAGGER API Documentation through ``/api/v1/docs`` .

Running test locally
********************

We will be using the following tools for testing:

- `pytest <https://docs.pytest.org/>`_
- `tox <https://tox.wiki/>`_
- `coverage <https://coverage.readthedocs.io/>`_
- `mypy <https://mypy.readthedocs.io/>`_


.. code-block:: shell

    $ pip install tox
    $ tox

Ensure test has 100% coverage or it will fail.

Generating Spinx documentation
******************************

Run the following:

.. code-block:: shell

    $ cd docs
    $ sphinx-apidoc -e -f -o source/ ../src
    $ make html
