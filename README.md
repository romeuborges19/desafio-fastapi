## PokéAPI com FastAPI 

Camada de API desenvolvida com FastAPI, com armazenamento de pesquisas em cache em uma instância do Redis, autenticação e permissão de usuários e controle de Rate Limit.

---

### Detalhes do projeto

Como requisitado, o projeto permite que sejam realizadas buscas sobre informações de Pokémons pela PokéAPI e os resultados dessas pesquisas são armazenados em cache para tornar pesquisas futuras mais rápidas. 

As permissões nos endpoints foram configuradas de modo que apenas usuários autenticados podem realizar pesquisas. Também foi adicionado um middleware para o processo de Rate Limiting, limitando a 10 requisições por usuário, como sugerido.

#### 1. FastAPI

Foi utilizada em grande parte a arquitetura proposta em um outro projeto:

https://github.com/igorbenav/FastAPI-boilerplate

Todo o processo de autenticação de usuários foi realizado utilizando tokens JWT, devido à minha familiaridade com o processo.

#### 2. Redis

Foram utilizadas três instâncias do Redis:
 
- Uma para armazenamento de estruturas de dados, voltada para salvar as informações dos usuários
- Uma para armazenamento de dados em cache.
- E outra para controle do processo de rate limiting.


O processo de cache foi organizado na camada de serviços e é utilizado pelas funções do serviço responsável por consumir a PokéAPI.

Durante o processo, percebi a necessidade de serem utilizados os recursos de busca do Redis Stack, o que me levou a organizar o projeto em uma imagem no Docker para facilitar o desenvolvimento na minha máquina.

---

### Rodar o projeto

#### 1. Através de uma imagem no docker (RECOMENDADO)

O ambiente de desenvolvimento foi configurado em uma imagem no docker, que carrega as instâncias do Redis e o FastAPI. 

É o método recomendado, por facilitar a configuração das variáveis de ambiente necessárias aos servidores Redis e possibilitar o uso dos recursos do Redis Stack em qualquer sistema operacional.

Rode os seguintes comandos no terminal:

```
git clone git@github.com:romeuborges19/desafio-fastapi.git
cd desafio-fastapi
sudo docker-compose up --build
```

É possível rodar os testes através do comando:
```
sudo docker exec poke-api pytest
```

#### 2. Manualmente

Método mais dificultoso. Podem haver problemas.

Para configurar o ambiente manualmente, é necessário ter na sua máquina:

- Python 3.11 ou superior
- Redis Stack

Atendendo os requisitos listados, basta fazer o seguinte:

1. Clonar o repositório
```
git@github.com:romeuborges19/desafio-fastapi.git
cd desafio-fastapi
```

2. Criar um ambiente virtual.
```
python -m venv venv
```

3. Inicializar o ambiente virtual. No Windows:
```
venv\Scripts\activate
```
No MacOS e Linux:
```
source venv/bin/activate
```

4. Instale as dependências do projeto
```
pip install -r requirements.txt
```

5. Inicialize as instâncias do Redis
```
redis-stack-server --port 6380 
redis-stack-server --port 6379
redis-stack-server --port 6378
```

6. Inicialize o servidor uvicorn:
```
uvicorn app.main:app --reload 
```

Desta forma, o projeto deve rodar tranquilamente.

Para testar o programa, basta utilizar o comando:
```
pytest
```
