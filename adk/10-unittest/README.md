# Unit Test Examples (ADK)

## Example Overview
This folder contains unit test examples for ADK agents and components, including asynchronous and REST-based tests.

- `async.py`: Demonstrates async task execution and result gathering in Python.
- `stock_REST.py`: (If present) Example of REST API-based testing for agent logic.

## Environment Setting
Set any required environment variables in your `.env` file. Refer to the main project `.env` for examples.

## How to Run
Run a test file using:

```bash
uv run python async.py
```

Or use pytest for all tests:

```bash
uv run pytest
```

## License
This project is licensed under the Apache License 2.0. See the [LICENSE](../LICENSE) file for details.
