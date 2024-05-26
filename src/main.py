# main.py

import argparse
import logging
from src.cvat_api import CVATAPI
from src.utils import setup_logging
from src.config import CVAT_API_URL, API_TOKEN

def main():
    parser = argparse.ArgumentParser(description='CVAT CLI for interacting with the CVAT API.')
    parser.add_argument('--token', help='API token for authentication', default=API_TOKEN)
    parser.add_argument('--check-health', action='store_true', help='Check health of the CVAT API')
    parser.add_argument('--create-project', type=str, help='Create a new project with the specified name')
    parser.add_argument('--create-task', type=str, help='Create a new task with the specified name in a project')
    parser.add_argument('--list-projects', action='store_true', help='List all projects')
    parser.add_argument('--list-tasks', action='store_true', help='List all tasks in a project')
    parser.add_argument('--project-id', type=int, help='Project ID to list tasks')
    parser.add_argument('--task-id', type=int, help='Task ID to export data')
    parser.add_argument('--log-level', type=str, help='Logging level', default='INFO')

    args = parser.parse_args()
    setup_logging(args.log_level)

    if not args.token:
        logging.error("No API token provided. Please provide a token via command line or config.py.")
        return

    api = CVATAPI(args.token)

    if args.check_health:
        healthy, result = api.check_health()
        if healthy:
            logging.debug(f"Full response: {result}")
        else:
            logging.error(f"CVAT API is not healthy: {result}")

    if args.list_projects:
        projects = api.list_projects()
        for project in projects:
            logging.info(f"Project ID: {project['id']}, Name: {project['name']}")

    if args.list_tasks and args.project_id is None:
        logging.error("Please provide a project ID to list tasks")
    elif args.list_tasks:
        tasks = api.list_tasks(args.project_id)
        for task in tasks:
            logging.info(f"Task ID: {task['id']}, Name: {task['name']}")

    if args.create_project:
        project_id = api.create_project(args.create_project)
        logging.info(f"New project created with ID: {project_id}")

    if args.create_task and args.project_id:
        task_id = api.create_task(args.create_task, args.project_id)
        logging.info(f"New task created with ID: {task_id} in project {args.project_id}")


if __name__ == "__main__":
    main()
