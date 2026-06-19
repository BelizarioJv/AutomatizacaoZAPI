from dotenv import load_dotenv
import os

load_dotenv()

# Variaveis de ambiente da aplicaçao (SUPABASE e Z-API)
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

ZAPI_URL = os.getenv("ZAPI_URL")
ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")