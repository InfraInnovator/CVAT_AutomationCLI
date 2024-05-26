# cvat_api.py

import requests
import os
import glob
import logging
from src.config import CVAT_API_URL

class CVATAPI:
    def __init__(self, token):
        self.base_url = CVAT_API_URL
        self.session = requests.Session()
        if token:
            self.authenticate_with_token(token)

    def authenticate_with_token(self, token):
        """ Authenticate to CVAT using an API token. """
        self.session.headers.update({'Authorization': f'Token {token}'})
        logging.info("Authentication with API token successful")

    def check_health(self):
        try:
            response = self.session.get(f"{self.base_url}/server/about")
            response.raise_for_status()
            logging.debug("CVAT API is healthy")
            return True, response.json()
        except requests.RequestException as e:
            logging.error(f"Failed to connect to CVAT API: {str(e)}")
            if logging.getLogger().level == logging.DEBUG:
                logging.debug(f"Full response: {e.response.text}")
            return False, str(e)

    def create_project(self, name):
        """Create a new project."""
        url = f"{self.base_url}/projects"
        data = {'name': name}
        response = self.session.post(url, json=data)
        if response.status_code == 201:
            project = response.json()
            return project['id']
        else:
            logging.error(f"Failed to create project: {response.text}")
            return None

    def create_task(self, name, project_id=None, labels=None):
        """Create a new task, optionally within a project."""
        url = f"{self.base_url}/tasks"
        data = {
            'name': name,
            'project_id': project_id,
            'labels': labels if labels else []
        }
        response = self.session.post(url, json=data)
        if response.status_code == 201:
            task = response.json()
            logging.info(f"Task {name} created successfully with ID: {task['id']}")
            return task['id']
        else:
            logging.error(f"Failed to create task: {response.status_code} - {response.text}")
            return None

    def list_projects(self):
        """List all projects available."""
        url = f"{self.base_url}/projects"
        response = self.session.get(url)
        if response.status_code == 200:
            return response.json().get('results', [])
        else:
            logging.error(f"Failed to retrieve projects: {response.status_code} - {response.text}")
            return []

    def list_tasks(self, project_id=None):
        """List all tasks or tasks in a specific project."""
        url = f"{self.base_url}/tasks"
        params = {'project_id': project_id} if project_id else {}
        response = self.session.get(url, params=params)
        if response.status_code == 200:
            return response.json().get('results', [])
        else:
            logging.error(f"Failed to retrieve tasks: {response.status_code} - {response.text}")
            return []

    def list_images_in_task(self, task_id):
        """List all images in a task."""
        url = f"{self.base_url}/tasks/{task_id}/images"
        response = self.session.get(url)
        if response.status_code == 200:
            return response.json().get('results', [])
        else:
            logging.error(f"Failed to retrieve images for task {task_id}: {response.status_code} - {response.text}")
            return []


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
