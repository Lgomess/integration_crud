from core.asana import create_asana_subtask, create_asana_section, create_asana_task
from core.trello import get_trello_lists, get_trello_cards, get_trello_checklists


def sync_trello_to_asana():
    """Sincroniza as listas e cartões do Trello com o Asana."""
    lists = get_trello_lists()
    
    for trello_list in lists:
        section_id = create_asana_section(trello_list["name"])
        if not section_id:
            continue

        cards = get_trello_cards(trello_list["id"])
        for card in cards:
            task_id = create_asana_task(card["name"], card.get("desc", ""), section_id)
            if task_id:
                subtasks = get_trello_checklists(card["id"])
                for subtask in subtasks:
                    create_asana_subtask(task_id, subtask)

if __name__ == "__main__":
    sync_trello_to_asana()
    print("Sincronização concluída!")
