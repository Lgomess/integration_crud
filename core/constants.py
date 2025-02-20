from dotenv import load_dotenv
import os

# Carregar variáveis do .env
load_dotenv()

# Credenciais do Trello
TRELLO_KEY = os.getenv("TRELLO_KEY")
TRELLO_TOKEN = os.getenv("TRELLO_TOKEN")
TRELLO_BOARD_ID = os.getenv("TRELLO_BOARD_ID")

# Credenciais do Asana
ASANA_TOKEN = os.getenv("ASANA_TOKEN")
ASANA_PROJECT_ID = os.getenv("ASANA_PROJECT_ID")

TRELLO_API_URL = "https://api.trello.com/1"
ASANA_API_URL = "https://app.asana.com/api/1.0"

