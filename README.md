Creating a new Virtual Environment (In the current folder):

```python -m venv venv```

```cd venv/Scripts```

```activate```

To run server locally: 

```uvicorn src.main:ApiClient --reload --host localhost --port 8888```

Check [Swagger](http://localhost:8888/docs) for API documentation.

Run with tox (recommended):

```pip install tox```

```tox```

To import: 

```pip install -r requirements.txt```

To run individual tests:

```pytest {file to tests, from tests/}```
