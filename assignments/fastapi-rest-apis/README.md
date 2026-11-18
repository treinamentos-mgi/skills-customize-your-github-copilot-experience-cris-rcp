# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Aprenda a criar uma API REST com FastAPI, definindo rotas, validando dados com modelos Pydantic e retornando respostas HTTP apropriadas. Ao final, você terá uma API de tarefas com operações CRUD e documentação interativa.

## 📝 Tasks

### 🛠️ Create the FastAPI App and Read Routes

#### Descrição
Instale FastAPI e execute a aplicação inicial. Implemente as rotas `GET /tasks` para listar as tarefas em memória e `GET /` para retornar uma mensagem indicando que a API está ativa.

#### Requisitos
O programa concluído deve:

- Instalar as dependências com `python -m pip install "fastapi[standard]"`.
- Iniciar a aplicação com `uvicorn starter-code:app --reload`.
- Retornar uma resposta JSON nas rotas `GET /` e `GET /tasks`.
- Permitir explorar e testar as rotas pela documentação interativa em `/docs`.

### 🛠️ Add Task Creation and Data Validation

#### Descrição
Use os modelos Pydantic fornecidos no código inicial para criar tarefas por meio de `POST /tasks`. A API deve gerar o ID da tarefa e validar os dados recebidos.

#### Requisitos
O programa concluído deve:

- Receber título, descrição e estado de conclusão no corpo da requisição.
- Rejeitar títulos vazios e retornar os erros de validação do FastAPI.
- Adicionar a nova tarefa à lista em memória e retornar a tarefa criada com status HTTP `201`.
- Retornar a tarefa criada com um ID único entre as tarefas atuais.

### 🛠️ Complete the Task CRUD Routes

#### Descrição
Implemente as rotas para consultar, atualizar e remover uma tarefa específica usando seu ID. A API mantém os dados apenas em memória, então eles são perdidos quando o servidor é reiniciado.

#### Requisitos
O programa concluído deve:

- Implementar `GET /tasks/{task_id}` para retornar uma tarefa existente.
- Implementar `PUT /tasks/{task_id}` para atualizar uma tarefa existente.
- Implementar `DELETE /tasks/{task_id}` para remover uma tarefa e retornar status HTTP `204`.
- Retornar status HTTP `404` quando o ID solicitado não existir.