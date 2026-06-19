# Importaçao do cliente do supabase para consumo dos dados
# Importaçao das variaveis de ambiente para acesso no supabase
from supabase import create_client
from conf.settings import (
    SUPABASE_URL,
    SUPABASE_KEY
)

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)
# funçao de query busca de clientes
def searchCustomer():
    return (
        supabase
        .table("clientes")
        .select("*")
        .execute()
        .data
    )