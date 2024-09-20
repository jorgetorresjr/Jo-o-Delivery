# João Delivery - Banco de Dados

Este repositório contém o esquema do banco de dados para o aplicativo de entrega de bebidas **João Delivery**. O banco de dados foi projetado para gerenciar clientes, fornecedores, entregadores, produtos, compras e entregas de forma eficiente.

## Estrutura do Banco de Dados

O banco de dados é dividido em várias tabelas, cada uma com seu propósito e interconectada através de chaves estrangeiras. As principais tabelas e suas descrições estão listadas abaixo.

## Tabelas do Banco de Dados

### 1. **cliente**
Armazena as informações dos clientes que utilizam o sistema de entrega.

| Campo             | Tipo         | Descrição                                      |
|-------------------|--------------|-----------------------------------------------|
| id_cliente        | INTEGER      | Chave primária do cliente                     |
| rg                | CHAR         | Documento de identidade (RG) do cliente       |
| nome              | CHAR         | Nome completo do cliente                      |
| cep               | CHAR         | Código postal do cliente                      |
| logradouro        | CHAR         | Logradouro do endereço                        |
| rua               | CHAR         | Nome da rua                                   |
| numero            | CHAR         | Número da residência                          |
| complemento       | CHAR         | Complemento do endereço                       |
| telefone          | CHAR         | Número de telefone do cliente                 |
| cartao_cadastrado | CHAR         | Informações sobre o cartão cadastrado         |

### 2. **fornecedor**
Armazena as informações dos fornecedores que fornecem os produtos.

| Campo             | Tipo         | Descrição                                      |
|-------------------|--------------|-----------------------------------------------|
| id_fornecedor     | INTEGER      | Chave primária do fornecedor                  |
| cnpj              | CHAR         | CNPJ do fornecedor                            |
| razao_social      | CHAR         | Razão social do fornecedor                    |
| cep               | CHAR         | Código postal do fornecedor                   |
| logradouro        | CHAR         | Logradouro do endereço do fornecedor          |
| rua               | CHAR         | Nome da rua                                   |
| numero            | CHAR         | Número da sede do fornecedor                  |
| complemento       | CHAR         | Complemento do endereço                       |
| horario           | DATE         | Horário de funcionamento do fornecedor        |
| representante     | CHAR         | Nome do representante do fornecedor           |

### 3. **entregador**
Armazena as informações dos entregadores que realizam as entregas.

| Campo             | Tipo         | Descrição                                      |
|-------------------|--------------|-----------------------------------------------|
| id_entregador     | INTEGER      | Chave primária do entregador                  |
| rg                | CHAR         | Documento de identidade (RG) do entregador    |
| nome              | CHAR         | Nome completo do entregador                   |
| sobrenome         | CHAR         | Sobrenome do entregador                       |
| cpf               | CHAR         | CPF do entregador                             |
| cep               | CHAR         | Código postal do entregador                   |
| logradouro        | CHAR         | Logradouro do endereço                        |
| rua               | CHAR         | Nome da rua                                   |
| numero            | CHAR         | Número da residência                          |
| complemento       | CHAR         | Complemento do endereço                       |
| telefone          | CHAR         | Número de telefone do entregador              |
| pagamento         | FLOAT        | Pagamento por entrega                         |
| quantidade        | INTEGER      | Quantidade de entregas realizadas             |
| avaliacao         | INTEGER      | Avaliação do entregador                       |

### 4. **produto**
Armazena as informações dos produtos disponíveis para compra.

| Campo             | Tipo         | Descrição                                      |
|-------------------|--------------|-----------------------------------------------|
| id_produto        | INTEGER      | Chave primária do produto                     |
| categoria         | CHAR         | Categoria do produto                          |
| descricao         | CHAR         | Descrição do produto                          |
| preco             | REAL         | Preço do produto                              |
| quantidade        | INTEGER      | Quantidade em estoque                         |
| avaliacao         | INTEGER      | Avaliação do produto                          |

### 5. **compra**
Armazena as informações das compras realizadas pelos clientes.

| Campo             | Tipo         | Descrição                                      |
|-------------------|--------------|-----------------------------------------------|
| id_compra         | INTEGER      | Chave primária da compra                      |
| horario           | DATE         | Horário da compra                             |
| valor_total       | FLOAT        | Valor total da compra                         |
| forma_pagamento   | CHAR         | Forma de pagamento                            |
| id_cliente        | INTEGER      | Chave estrangeira referente ao cliente        |
| id_produto        | INTEGER      | Chave estrangeira referente ao produto        |
| id_fornecedor     | INTEGER      | Chave estrangeira referente ao fornecedor     |
| FOREIGN KEY       |              | Relaciona com a tabela `cliente`, `produto` e `fornecedor` |

### 6. **entrega**
Armazena as informações das entregas associadas a uma compra.

| Campo             | Tipo         | Descrição                                      |
|-------------------|--------------|-----------------------------------------------|
| id_entrega        | INTEGER      | Chave primária da entrega                     |
| tempo_entrega     | DATE         | Tempo estimado da entrega                     |
| id_cliente        | INTEGER      | Chave estrangeira referente ao cliente        |
| id_produto        | INTEGER      | Chave estrangeira referente ao produto        |
| id_entregador     | INTEGER      | Chave estrangeira referente ao entregador     |
| FOREIGN KEY       |              | Relaciona com a tabela `cliente`, `produto` e `entregador` |

## Requisitos

- **MySQL** ou **PostgreSQL** (ou outro banco de dados relacional).
- Ferramentas de gerenciamento de banco de dados como **phpMyAdmin** ou **pgAdmin** são recomendadas.

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/joao-delivery-db.git
2. Execute os scripts SQL no seu sistema de banco de dados.
3. Configure o seu aplicativo para conectar ao banco de dados.

## Contribuições
Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões de melhorias, sinta-se à vontade para abrir um issue ou enviar um pull request.

## Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais informações.   
