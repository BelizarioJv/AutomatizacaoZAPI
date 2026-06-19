
-- query de criaçao da tabela de cleintes
create table clientes (
    id uuid primary key default gen_random_uuid(),
    nome text not null,
    telefone text not null
);