# CVAT CLI Tool

CVAT CLI is a command-line interface tool designed to interact with the CVAT API. This tool enables users to manage projects and tasks within CVAT and to import data efficiently.

## Features

- Check API health
- List all projects
- Create new projects
- Create new tasks within projects

## Future planned features

- Import images into a task
- Export images based on a project, task, and filter by tags/attributes
- Ability to perform dry run and not perform actual imports/exports/project creation/etc
- Ability to add tags and attributes
- List images associated with a task
- Functionality to remove tasks and projects

## Prerequisites

- Python 3.x
- Access to CVAT API with a valid API token

## Setup

Before you begin, ensure you have set up the necessary configurations in src/config.py, including your CVAT_API_URL and API_TOKEN.

## Usage

Below are the commands available in CVAT CLI:

### Check API Health

Purpose: Verifies that the CVAT API is accessible and responding correctly.

Command:

```bash
python -m src.main --check-health --log-level DEBUG
```

### List All Projects

Purpose: Retrieves and displays a list of all existing projects in the CVAT.

Command:

```bash
python -m src.main --list-projects --log-level INFO
```

### Create a New Project

Purpose: Creates a new project in CVAT with a specified name.

Command:

```bash
python -m src.main --create-project "Your_Project_Name"
```

### Create a New Task

Purpose: Creates a new task within a specified project and optionally imports data into this task.

Command:

```bash
python -m src.main --create-task "Your_Task_Name" --project-id 123
```

### List the tasks

Purpose: Retrieves and displays a list of tasks in the CVAT.

```bash
python -m src.main --list-tasks --project-id 123
```

### Contributing

Contributions to this project are welcome!
