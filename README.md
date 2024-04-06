# davu-airflow-interface
### Prerequisites:

Python >=3.11

### Setup Project
You can setup a virtual environment for the project using `virtualenv` or `pyenv`. To use `vitualenv`;
- Install the package
    ```bash
    pip install virtualenv
- Run command to create a virtual env;
    ```bash
    python3.11 -m venv <virtual-environment-name>
- Activate the created env;
    ```bash
    source <virtual-environment-name>/bin/activate
    ```

Next, install the project's dependencies;
```bash
pip install -r requirements.txt
```

## Creating a DAG Run

- Import the `AirflowDagInterface` class

    ```python
    from create_dag import AirflowDagInterface
    ```
- Create an instance of the interface and initialize it with your Airflow instance URL
    ```python
    airflow_host = "http://<your-host-instance>.com"
    dag_interface = AirflowDagInterface(airflow_host)
    ```
- Call the `create_dag` method with the DAG ID and optional `conf` to create a dag
    ```python
    dag_id = "<dag_id>"
    conf = {"key1": "value1", "key2": 2} #optional
    create_dag_response = dag_interface.create_dag(dag_id, conf)
    print(create_dag_response)
    ```
### Expected Output
```bash
{
  "dag_run_id": 145,
  "execution_date": "2024-04-06T04:35:42.000000+00:00"
}  // For successful creation

// OR

{
  "details": "Error message from Airflow",
  "error": "Creation failed!"
}  // For failure
```

To run the test that mocks the `create_dag` run:
```bash
pytest
