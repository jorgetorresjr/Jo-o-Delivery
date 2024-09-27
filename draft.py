from functions.insert_rows import insert_one_row
from functions.create_table import create_table
from functions.drop_table import drop_table
drop_table(
    database="mydatabase",
    table_name="produtos"
)

create_table(
    database='mydatabase',
    table_name='cliente',
    columns_desc="""
        id_cliente INTEGER PRIMARY KEY,
        rg CHAR NOT NULL,
        nome CHAR NOT NULL,
        cep CHAR NOT NULL,
        logradouro CHAR NOT NULL,
        rua CHAR NOT NULL,
        numero CHAR NOT NULL,
        complemento CHAR NOT NULL,
        telefone CHAR NOT NULL,
        cartao_cadastrado CHAR NOT NULL
    """
)
create_table(
    database='mydatabase',
    table_name='fornecedor',
    columns_desc="""
        id_fornecedor INTEGER PRIMARY KEY,
        cnpj CHAR NOT NULL,
        razao_social CHAR NOT NULL,
        cep CHAR NOT NULL,
        logradouro CHAR NOT NULL,
        rua CHAR NOT NULL,
        numero CHAR NOT NULL,
        complemento CHAR NOT NULL,
        horario DATE NOT NULL,
        representante CHAR NOT NULL
    """
)

create_table(
    database='mydatabase',
    table_name='entregador',
    columns_desc="""
        id_entregador INTEGER PRIMARY KEY,
        rg CHAR NOT NULL,
        nome CHAR NOT NULL,
        sobrenome CHAR NOT NULL,
        cpf CHAR NOT NULL,
        cep CHAR NOT NULL,
        logradouro CHAR NOT NULL,
        rua CHAR NOT NULL,
        numero CHAR NOT NULL,
        complemento CHAR NOT NULL,
        telefone CHAR NOT NULL,
        pagamento float NOT NULL,
        quantidade INTEGER NOT NULL,
        avaliacao INTEGER NOT NULL
    """
)
create_table(
    database='mydatabase',
    table_name='produto',
    columns_desc="""
        id_produto INTEGER PRIMARY KEY,
        categoria CHAR NOT NULL,
        descricao CHAR NOT NULL,
        preco REAL NOT NULL,
        quantidade INT NOT NULL,
        avaliacao INT NOT NULL
    """
)
create_table(
    database='mydatabase',
    table_name='compra',
    columns_desc="""
        id_compra INTEGER PRIMARY KEY,
        horario DATE NOT NULL,
        valor_total FLOAT NOT NULL,
        forma_pagamento CHAR NOT NULL,
        id_cliente INT, 
        id_produto INT,
        id_fornecedor INT,
        FOREIGN KEY(id_cliente) REFERENCES cliente(id_cliente),
        FOREIGN KEY(id_produto) REFERENCES produto(id_produto),
        FOREIGN KEY(id_fornecedor) REFERENCES fornecedor(id_fornecedor)
    """
)
create_table(
    database='mydatabase',
    table_name='entrega',
    columns_desc="""
        id_entrega INTEGER PRIMARY KEY,
        tempo_entrega DATE NOT NULL,
        id_cliente INT, 
        id_produto INT,
        id_entregador INT,
        FOREIGN KEY(id_cliente) REFERENCES cliente(id_cliente),
        FOREIGN KEY(id_produto) REFERENCES produto(id_produto),
        FOREIGN KEY(id_entregador) REFERENCES entregador(id_entregador)
    """
)

insert_one_row(
   database_name='mydatabase',
    table_name='entregador',
    columns_name='rg, nome, cpf, cep, ',
    values="'Xbox', 90"
)

