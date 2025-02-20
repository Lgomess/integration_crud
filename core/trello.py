from core.constants import TRELLO_API_URL, TRELLO_BOARD_ID, TRELLO_KEY, TRELLO_TOKEN
import requests

def get_trello_lists():
    """Obtém todas as listas do Trello."""
    url = f"{TRELLO_API_URL}/boards/{TRELLO_BOARD_ID}/lists?key={TRELLO_KEY}&token={TRELLO_TOKEN}"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else []

def get_trello_cards(list_id):
    """Obtém todos os cards de uma lista do Trello."""
    url = f"{TRELLO_API_URL}/lists/{list_id}/cards?key={TRELLO_KEY}&token={TRELLO_TOKEN}"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else []

def get_trello_checklists(card_id):
    """Obtém todas as tarefas (checklists) de um card do Trello."""
    url = f"{TRELLO_API_URL}/cards/{card_id}/checklists?key={TRELLO_KEY}&token={TRELLO_TOKEN}"
    response = requests.get(url)
    
    if response.status_code == 200:
        checklists = response.json()
        return [item["name"] for clist in checklists for item in clist.get("checkItems", [])]
    
    return []