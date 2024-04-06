import json
import unittest
from unittest.mock import patch

from create_dag import AirflowDagInterface


@patch.object(AirflowDagInterface, "_send_dag_data")
def test_create_dag_success(mock_send_data):
    """
    Tests successful DAG run creation without conf data.
    """
    mock_send_data.return_value = {"dag_run_id": 123}
    airflow_host = "http://host.com"
    dag_interface = AirflowDagInterface(airflow_host)

    created_dag_data = dag_interface.create_dag("my_dag")

    assert created_dag_data["dag_run_id"] == 123
    mock_send_data.assert_called_once_with(
        f"{airflow_host}/api/experimental/dags/my_dag/dag_runs",
        json.dumps({"conf": {}})
    )


@patch.object(AirflowDagInterface, "_send_dag_data")
def test_create_dag_success_with_conf(mock_send_data):
    """
    Tests successful DAG run creation with conf data.
    """
    mock_send_data.return_value = {"dag_run_id": 123}
    airflow_host = "http://host.com"
    dag_interface = AirflowDagInterface(airflow_host)

    created_dag_data = dag_interface.create_dag("my_dag", {"key": "value"})

    assert created_dag_data["dag_run_id"] == 123
    mock_send_data.assert_called_once_with(
        f"{airflow_host}/api/experimental/dags/my_dag/dag_runs",
        json.dumps({"conf": {"key": "value"}})
    )
