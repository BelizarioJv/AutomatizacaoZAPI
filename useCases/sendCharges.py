from services.supabaseService import searchCustomer
from services.whatsAppService import sendMensage

def executar():

    clientes = searchCustomer()

    for cliente in clientes:

        mensagem = f"""
        Olá {cliente['nome']}

        Seu pagamento está disponível.
        """

        sendMensage(
            cliente["telefone"],
            mensagem
        )