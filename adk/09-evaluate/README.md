# Evaluation Examples (ADK)

## Example Overview
This folder demonstrates how to evaluate ADK agents using the built-in evaluation tools and pytest.

- `agent_eval/`: Contains evaluation data and configuration for agent testing.

## Environment Setting
Set any required environment variables in your `.env` file. Refer to the main project `.env` for examples.

## How to Run
- To run ADK evaluation:
  ```bash
  adk eval agent_eval \
      agent_eval/data/conversation.test.json \
      --config_file_path=agent_eval/data/test_config.json \
      --print_detailed_results
  ```
- To run pytest-based tests:
  ```bash
  uv run pytest -m agent_eval
  ```
  (Note: Additional pytest plugins may be required.)

## License
This project is licensed under the Apache License 2.0. See the [LICENSE](../LICENSE) file for details.