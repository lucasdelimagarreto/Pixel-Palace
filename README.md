# Pixel Palace

Pixel Palace é um projeto de uma loja de jogos fictícia desenvolvida como parte de um exercício de programação.

## Descrição

Pixel Palace é uma loja de jogos fictícia, onde os usuários podem navegar e comprar uma variedade de jogos eletrônicos. A loja oferece uma seleção de jogos para diferentes plataformas e gêneros, incluindo jogos para PC, consoles e dispositivos móveis.

## Funcionalidades

- Navegação intuitiva: os usuários podem explorar facilmente os jogos disponíveis na loja.
- Filtragem por plataforma e gênero: os usuários podem filtrar os jogos por plataforma (PC, console, móvel) e gênero (ação, aventura, quebra-cabeça, etc.).
- Detalhes do jogo: os usuários podem visualizar informações detalhadas sobre cada jogo, incluindo descrição, avaliações dos usuários e preço.
- Adicionar ao carrinho: os usuários podem adicionar jogos ao carrinho de compras e prosseguir para o checkout.
- Checkout: os usuários podem revisar os itens no carrinho, inserir informações de pagamento e concluir a compra.

## Tecnologias Utilizadas

- Frontend: HTML, CSS, JavaScript, Nextjs
- Backend: Node.js, Express.js, Flask, Python
- Banco de Dados: Postgres

## Instalação

1. Faça um fork do projeto

2. Clone o repositório:

```git clone https://github.com/seu-usuario/pixel-palace.git```

3. Instale as dependências:

```cd pixel-palace```

```npm install``` (client)

4. Configure as variáveis de ambiente:

Crie um arquivo `.env` dentro da pasta server do projeto e defina as variáveis de ambiente necessárias, como a URI do banco de dados Postgres.

5. Execute o projeto:

```npm run dev``` (client)
```python manage.py``` (server)


6. Acesse a aplicação em `http://localhost:3000` no seu navegador.

## Banco de Dados

Para construir um banco de dados para o Pixel Palace siga os seguintes passos:

1. criar e rodar o container postgres pelo Docker:

```docker run --name Pixel-Palace -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=123456 -p 5432:5432 -d postgres```

2. criar e rodar o container pgadim4 pelo docker com o postgres conectado:

```docker run --name PG4-Pixel-Palace -p 5050:80 -e PGADMIN_DEFAULT_EMAIL=seuemail -e PGADMIN_DEFAULT_PASSWORD=postgres -d dpage/pgadmin4```

3. Após inicializar o postgres e pgadmin4 no Docker, acesse o pgadmin pelo navegador e crie um banco de dados chamado pixel_palace para dar continuidade. Para preencher o banco de dados com as tabelas necessárias para o Pixel Palace siga os seguintes passos:

- entre na pasta server caso não esteja:

```cd server```

4. Inicialize sua .venv e rode os seguintes comandos em sequência:

```flask db init```

```flask db migrate -m "Initial migration."```

```flask db upgrade```

5. Utilize o Postman ou Insomnia para realizar requisições GET e preencher seu banco de dados. Abaixo se encontra a estrutura JSON de jogos para o sistema. 

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Este projeto é licenciado sob a [MIT License](LICENSE).