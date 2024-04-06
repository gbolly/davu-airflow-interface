import json
import requests
from typing import Union


class AirflowDagInterface:
    def __init__(self, airflow_host: str):
        self.airflow_host = airflow_host
        self.headers = {
            "Cache-Control": "no-cache",
            "Content-Type": "application/json"
        }

    def create_dag(self, dag_id: str, conf: dict = {}) -> dict:
        """
        Creates a DAG run in Airflow.

        Args:
            dag_id (str): ID of the DAG.
            conf (dict): Dictionary describing additional configuration.
        """
        create_dag_run_url = f"{self.airflow_host}/api/experimental/dags/{dag_id}/dag_runs"
        created_dag_data = self._send_dag_data(
            create_dag_run_url, json.dumps({"conf": conf}))

        if type(created_dag_data) is str:
            created_dag_data = {
                "details": created_dag_data, "error": "Creation failed!"}
        return created_dag_data

    def _send_dag_data(self, url: str, data: dict) -> Union[dict, str]:
        """
        Sends the DAG run data to the Airflow API.

        Args:
            url (str): Create dag run endpoint url.
            data (dict): Dictionary containing the DAG conf.
        """
        response = requests.post(url, headers=self.headers, data=data)
        if response.status_code == 200:
            return response.json()
        else:
            print("Request failed with status code:", response.status_code)
            return response.text
