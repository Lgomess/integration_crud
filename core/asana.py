from core.constants import ASANA_API_URL, ASANA_TOKEN, ASANA_PROJECT_ID
import requests

def get_asana_sections():
    """Obtém todas as seções do projeto no Asana."""
    url = f"{ASANA_API_URL}/projects/{ASANA_PROJECT_ID}/sections"
    headers = {"Authorization": f"Bearer {ASANA_TOKEN}"}
    response = requests.get(url, headers=headers)
    return {section["name"]: section["gid"] for section in response.json()["data"]} if response.status_code == 200 else {}

def create_asana_section(name):
    """Cria uma seção no Asana apenas se ela ainda não existir."""
    sections = get_asana_sections()
    if name in sections:
        return sections[name]

    url = f"{ASANA_API_URL}/sections"
    headers = {"Authorization": f"Bearer {ASANA_TOKEN}", "Content-Type": "application/json"}
    data = {"data": {"name": name, "project": ASANA_PROJECT_ID}}

    response = requests.post(url, json=data, headers=headers)
    return response.json()["data"]["gid"] if response.status_code == 201 else None

def create_asana_task(name, notes, section_id):
    """Cria uma tarefa no Asana dentro de uma seção específica."""
    url = f"{ASANA_API_URL}/tasks"
    headers = {"Authorization": f"Bearer {ASANA_TOKEN}", "Content-Type": "application/json"}
    data = {
        "data": {
            "name": name,
            "notes": notes,
            "projects": [ASANA_PROJECT_ID],
            "memberships": [{"section": section_id, "project": ASANA_PROJECT_ID}]
        }
    }
    response = requests.post(url, json=data, headers=headers)
    return response.json()["data"]["gid"] if response.status_code == 201 else None

def create_asana_subtask(parent_task_id, name):
    """Cria uma subtarefa no Asana."""
    url = f"{ASANA_API_URL}/tasks"
    headers = {"Authorization": f"Bearer {ASANA_TOKEN}", "Content-Type": "application/json"}
    data = {
        "data": {
            "name": name,
            "parent": parent_task_id
        }
    }
    response = requests.post(url, json=data, headers=headers)
    return response.status_code == 201