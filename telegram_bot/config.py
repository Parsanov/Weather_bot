import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
admin_id_row = int(os.getenv('ADMIN_ID'))

if not admin_id_row:
    print("Admin id doesn't exist")
    ADMIN_ID = None
ADMIN_ID = int(admin_id_row)


API_URL = os.getenv('API_SERVICE_URL')