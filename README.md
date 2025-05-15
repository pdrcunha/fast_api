
## 🎯 **Objetivo do Projeto**

**Construir uma API REST de gerenciamento de livros e empréstimos para uma pequena biblioteca comunitária.**

----------

## 📚 Tema: Biblioteca Comunitária

### Funcionalidades principais:

1.  **Cadastro de livros**
    
2.  **Cadastro de usuários**
    
3.  **Empréstimo e devolução de livros**
    
4.  **Histórico de empréstimos**
    
5.  **Consulta de disponibilidade de livros**
    

----------

## 🧩 Stack sugerida:

-   **Linguagem**: Python 3.11+
    
-   **Framework**: FastAPI
    
-   **Banco de dados**: PostgreSQL
    
-   **ORM**: SQLAlchemy
    
-   **Migrations**: Alembic
    
-   **Autenticação**: JWT
    
-   **Testes**: Pytest
    
-   **Documentação**: Swagger (automático no FastAPI)
    

----------

## 🪜 Passo a passo

### 🧱 Etapa 1: Setup do projeto

-   Criar ambiente virtual e instalar dependências:
    
    bash
    
    CopiarEditar
    
    `pip install fastapi[all] sqlalchemy alembic psycopg2-binary python-jose[cryptography] passlib[bcrypt] pytest` 
    
-   Estrutura básica de diretórios (ex: `app/`, `models/`, `routers/`, `schemas/`, `services/`, `database/`)
    

----------

### 📖 Etapa 2: Modelagem do banco

-   **Tabelas principais**:
    
    -   `users`: nome, email, senha (hash), data de criação
        
    -   `books`: título, autor, ano, status (disponível, emprestado)
        
    -   `loans`: user_id, book_id, data_empréstimo, data_devolução
        
-   Usar SQLAlchemy para definir os modelos
    

----------

### 🔐 Etapa 3: Autenticação e segurança

-   Criar rota de cadastro (`/signup`) e login (`/login`)
    
-   Gerar e validar tokens JWT
    
-   Proteger rotas com `Depends(get_current_user)`
    

----------

### 🔄 Etapa 4: CRUD básico

-   **Usuários**: Criar, listar, buscar por ID
    
-   **Livros**: Criar, listar, buscar, atualizar, deletar
    
-   **Empréstimos**:
    
    -   Rota para emprestar livro (`/loans/`)
        
    -   Rota para devolver livro
        
    -   Rota para listar histórico de um usuário
        

----------

### 🧪 Etapa 5: Testes automatizados

-   Criar testes unitários para funções
    
-   Testes de integração das rotas com `TestClient` do FastAPI
    

----------

### 🚀 Etapa 6: Deploy (opcional)

-   Dockerizar a aplicação
    
-   Fazer deploy no Railway, Render ou VPS
    

----------

### 🧠 Extras (se quiser ir além)

-   Notificações por email para devolução
    
-   Sistema de penalidades por atraso
    
-   Filtrar livros por categoria ou autor
    
-   Painel com estatísticas de uso