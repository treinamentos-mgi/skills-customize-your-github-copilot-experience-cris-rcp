# 📘 Assignment: Persisting FastAPI Data with SQLite

## 🎯 Objective

Use the built-in `sqlite3` library to save API data in a local database instead of keeping it only in memory. Você vai adaptar uma API FastAPI conhecida para que as tarefas continuem disponíveis após reiniciar o servidor.

## 📝 Tasks

### 🛠️ Create the SQLite Tasks Table

#### Descrição
Complete `initialize_database()` no código inicial para criar a tabela `tasks` quando ela ainda não existir. Use SQLite local; não é necessário instalar ou configurar um serviço de banco de dados.

#### Requisitos
O programa concluído deve:

- Criar uma tabela `tasks` com `id`, `title`, `description` e `completed`.
- Definir `id` como chave primária autoincremental e `title` como obrigatório.
- Usar `CREATE TABLE IF NOT EXISTS` para evitar apagar dados ao iniciar a API novamente.
- Iniciar a API com `uvicorn starter-code:app --reload`.

### 🛠️ Store and List Tasks Through the API

#### Descrição
Implemente `GET /tasks` e `POST /tasks` usando consultas SQL parametrizadas. Os dados devem ser lidos e gravados na tabela, em vez de uma lista Python em memória.

#### Requisitos
O programa concluído deve:

- Retornar as tarefas salvas em `GET /tasks` como uma lista JSON.
- Inserir título, descrição e estado de conclusão recebidos em `POST /tasks`.
- Usar placeholders `?` e parâmetros separados para enviar valores às consultas SQL.
- Retornar a tarefa criada com status HTTP `201` e seu ID gerado pelo SQLite.

### 🛠️ Finish CRUD and Verify Persistence

#### Descrição
Implemente a consulta, atualização e remoção de uma tarefa pelo ID. Teste as rotas pela documentação interativa e reinicie o servidor para confirmar que os dados continuam no banco local.

#### Requisitos
O programa concluído deve:

- Implementar `GET /tasks/{task_id}`, `PUT /tasks/{task_id}` e `DELETE /tasks/{task_id}` usando SQLite.
- Retornar status HTTP `404` quando uma tarefa com o ID solicitado não existir.
- Retornar status HTTP `204` ao remover uma tarefa existente.
- Manter as tarefas salvas após parar e iniciar novamente o servidor.