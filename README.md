# B2B Flow - Automação WhatsApp + Supabase

## Descrição

Automação para envio de mensagens via WhatsApp utilizando Z-API e Supabase como banco de dados.

---

## Estrutura da Tabela

Execute o SQL abaixo no Supabase:

```sql
create table clientes (
    id uuid primary key default gen_random_uuid(),
    nome text not null,
    telefone text not null
);
```

---

## Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
SUPABASE_URL=https://seu-projeto.supabase.co
SUPABASE_KEY=sua-chave-supabase

ZAPI_INSTANCE_ID=sua-instancia
ZAPI_TOKEN=seu-token
ZAPI_CLIENT_TOKEN=seu-client-token
```

---

## Instalação

Criar ambiente virtual:

```bash
python -m venv .venv
```

Ativar ambiente virtual:

Windows:

```bash
.venv\Scripts\activate
```

Instalar dependências:

```bash
pip install -r requirements.txt
```

---

## Executar Projeto

```bash
python main.py
```

---

## Fluxo

1. Busca clientes cadastrados no Supabase.
2. Gera mensagem personalizada.
3. Envia mensagem via Z-API.
4. Registra logs da execução.
