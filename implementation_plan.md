# Plano de Implementação — EduTrack AI (Projeto Integrador)

Desenvolvimento do sistema acadêmico **EduTrack AI — Assistente Educacional Personalizado**, estruturado de forma simples, estável, funcional e apresentável, atendendo a todos os requisitos do Projeto Integrador.

## Arquitetura Geral

O projeto será composto por:
1. **Backend em Python com FastAPI e SQLite**:
   - APIs RESTful completas para Autenticação, Disciplinas, Tarefas, Dashboard, Métricas e Recomendações.
   - Swagger / OpenAPI nativo em `/docs` para testes visuais e validação acadêmica.
   - Banco de dados relacional SQLite (`edutrack.db`) com integridade referencial (`PRAGMA foreign_keys = ON`), tabelas `users`, `subjects` e `academic_tasks`.
   - Segurança: Hash de senhas seguro (`pbkdf2_hmac` com salt) e controle de sessão/token garantindo que cada usuário visualize apenas seus próprios dados.
2. **Módulo de Métricas e Recomendações em Python**:
   - **Progresso ponderado**: cálculo ponderado pela carga horária das disciplinas.
   - **Velocidade de conclusão**: média de tarefas finalizadas no tempo.
   - **Previsão de conclusão**: estimativa matemática da data de término das tarefas restantes (com mensagem adequada quando dados forem insuficientes).
   - **Motor de recomendações determinístico**: análise de prazos atrasados, baixo progresso (<30%), tarefas com vencimento próximo e disciplinas com bom ritmo.
3. **Frontend Web Responsivo (Mobile & Desktop)**:
   - Interface moderna em Português do Brasil com navegação simples, cards informativos, gráficos claros (Chart.js), tabelas/listas responsivas e filtros em tempo real.
   - CRUD completo via modais intuitivos com validação, estados de carregamento, feedback de erro/sucesso (toast) e estados vazios amigáveis.
4. **Documentação Acadêmica**:
   - `DATA_DICTIONARY.md`: Dicionário de dados formal com tabelas, campos, tipos, PK, FK, descrições e obrigatoriedade.
   - `OPENSPEC.md`: Registro de especificações abertas (OpenSpec), alterações, arquivos criados e testes realizados.
   - `README.md`: Instruções detalhadas de execução, arquitetura e apresentação.
5. **Testes Automatizados**:
   - Testes cobrindo Autenticação, CRUD Disciplinas, CRUD Tarefas, Isolamento entre usuários, Métricas Python e Recomendações.

---

## Proposta de Arquivos e Componentes

### 1. Backend Python & Banco de Dados

#### [NEW] [requirements.txt](file:///c:/Users/kris1/OneDrive/Documentos/Edu%20Track%202/requirements.txt)
Dependências do projeto: `fastapi`, `uvicorn`, `pydantic`.

#### [NEW] [backend/database.py](file:///c:/Users/kris1/OneDrive/Documentos/Edu%20Track%202/backend/database.py)
Inicialização do SQLite, conexão com ativação de `foreign_keys`, criação das tabelas `users`, `subjects`, `academic_tasks` e seeds opcionais.

#### [NEW] [backend/security.py](file:///c:/Users/kris1/OneDrive/Documentos/Edu%20Track%202/backend/security.py)
Funções de hash de senha, validação de credenciais e geração/validação de tokens de autenticação para isolamento por usuário.

#### [NEW] [backend/models.py](file:///c:/Users/kris1/OneDrive/Documentos/Edu%20Track%202/backend/models.py)
Modelos Pydantic para validação das requisições e respostas da API:
- `UserCreate`, `UserLogin`, `UserResponse`, `PasswordReset`
- `SubjectCreate`, `SubjectUpdate`, `SubjectResponse`
- `TaskCreate`, `TaskUpdate`, `TaskResponse`
- `DashboardStats`, `RecommendationResponse`, `MetricsResponse`

#### [NEW] [backend/services/metrics.py](file:///c:/Users/kris1/OneDrive/Documentos/Edu%20Track%202/backend/services/metrics.py)
Lógica pura em Python para:
- Progresso ponderado por carga horária (\(\frac{\sum progresso \times carga}{\sum carga}\))
- Velocidade de conclusão (tarefas concluídas por dia/semana)
- Previsão de conclusão (estimativa em dias ou aviso de dados insuficientes)
- Geração de recomendações com regras determinísticas

#### [NEW] [backend/routers/auth_routes.py](file:///c:/Users/kris1/OneDrive/Documentos/Edu%20Track%202/backend/routers/auth_routes.py)
Endpoints de autenticação:
- `POST /api/auth/register`
- `POST /api/auth/login`
- `POST /api/auth/forgot-password`
- `GET /api/auth/me`

#### [NEW] [backend/routers/subject_routes.py](file:///c:/Users/kris1/OneDrive/Documentos/Edu%20Track%202/backend/routers/subject_routes.py)
CRUD de Disciplinas com filtro obrigatório por usuário:
- `POST /api/subjects` (Criar)
- `GET /api/subjects` (Listar com busca/filtro)
- `GET /api/subjects/{id}` (Detalhes)
- `PUT /api/subjects/{id}` (Atualizar)
- `DELETE /api/subjects/{id}` (Excluir em cascata tarefas associadas)

#### [NEW] [backend/routers/task_routes.py](file:///c:/Users/kris1/OneDrive/Documentos/Edu%20Track%202/backend/routers/task_routes.py)
CRUD de Tarefas vinculadas a disciplinas do usuário:
- `POST /api/tasks` (Criar)
- `GET /api/tasks` (Listar com filtros: disciplina, status, data, busca textual)
- `GET /api/tasks/{id}` (Detalhes)
- `PUT /api/tasks/{id}` (Atualizar)
- `DELETE /api/tasks/{id}` (Excluir)
- `PATCH /api/tasks/{id}/toggle-status` (Alternar pendente/concluída rapidamente)

#### [NEW] [backend/routers/dashboard_routes.py](file:///c:/Users/kris1/OneDrive/Documentos/Edu%20Track%202/backend/routers/dashboard_routes.py)
Endpoints de métricas, dashboard e recomendações:
- `GET /api/dashboard/summary`
- `GET /api/dashboard/metrics`
- `GET /api/dashboard/recommendations`

#### [NEW] [main.py](file:///c:/Users/kris1/OneDrive/Documentos/Edu%20Track%202/main.py)
Ponto de entrada FastAPI, montagem dos roteadores, configuração de CORS e montagem dos arquivos estáticos do frontend.

---

### 2. Frontend Responsivo

#### [NEW] [frontend/index.html](file:///c:/Users/kris1/OneDrive/Documentos/Edu%20Track%202/frontend/index.html)
SPA sem recarregamento de página:
- Seções: Tela de Login/Cadastro/Recuperação de Senha, Barra Lateral/Navegação Superior responsiva, Dashboard com Gráficos e Recomendações, Painel de Disciplinas (Cards e Modais), Painel de Tarefas (Filtros avançados e Modais).
- Modais acessíveis para inclusão/edição de disciplinas e tarefas.

#### [NEW] [frontend/css/style.css](file:///c:/Users/kris1/OneDrive/Documentos/Edu%20Track%202/frontend/css/style.css)
Folha de estilo moderna, limpa, responsiva (mobile first com suporte a desktop e tablet), paleta de cores agradável (azul/índigo acadêmico), badges de status e barras de progresso visuais.

#### [NEW] [frontend/js/api.js](file:///c:/Users/kris1/OneDrive/Documentos/Edu%20Track%202/frontend/js/api.js)
Cliente HTTP desacoplado com gerenciamento de token JWT/sessão e tratamento centralizado de erros.

#### [NEW] [frontend/js/auth.js](file:///c:/Users/kris1/OneDrive/Documentos/Edu%20Track%202/frontend/js/auth.js)
Controle de autenticação, login, logout, registro e recuperação de senha.

#### [NEW] [frontend/js/dashboard.js](file:///c:/Users/kris1/OneDrive/Documentos/Edu%20Track%202/frontend/js/dashboard.js)
Renderização dos cards de estatísticas, gráfico de progresso por disciplina, gráfico de pizza de tarefas pendentes vs concluídas (usando Chart.js via CDN) e lista de recomendações.

#### [NEW] [frontend/js/subjects.js](file:///c:/Users/kris1/OneDrive/Documentos/Edu%20Track%202/frontend/js/subjects.js)
Operações CRUD de disciplinas na interface (formulário de criação/edição, listagem com filtros, exclusão confirmada e visualização de detalhes).

#### [NEW] [frontend/js/tasks.js](file:///c:/Users/kris1/OneDrive/Documentos/Edu%20Track%202/frontend/js/tasks.js)
Operações CRUD de tarefas (criação, edição, exclusão, alternância de status com 1 clique, filtros combinados por disciplina, status e data).

#### [NEW] [frontend/js/app.js](file:///c:/Users/kris1/OneDrive/Documentos/Edu%20Track%202/frontend/js/app.js)
Navegação entre abas, inicialização e escuta de eventos globais.

---

### 3. Documentação & Testes

#### [NEW] [DATA_DICTIONARY.md](file:///c:/Users/kris1/OneDrive/Documentos/Edu%20Track%202/DATA_DICTIONARY.md)
Dicionário de dados contendo estrutura das tabelas `users`, `subjects`, `academic_tasks`, relacionamentos e tipos de campos.

#### [NEW] [OPENSPEC.md](file:///c:/Users/kris1/OneDrive/Documentos/Edu%20Track%202/OPENSPEC.md)
Registro OpenSpec com histórico de implementação, componentes, funcionalidades concluídas e validações realizadas.

#### [NEW] [tests/test_backend.py](file:///c:/Users/kris1/OneDrive/Documentos/Edu%20Track%202/tests/test_backend.py)
Bateria de testes automatizados com Python:
- Teste de cadastro, login e recuperação de senha;
- Teste de CRUD de disciplinas e tarefas;
- Teste de integridade referencial e isolamento por usuário;
- Teste dos cálculos matemáticos de progresso ponderado, velocidade e previsão;
- Teste do motor de recomendações.

---

## Plano de Verificação

### 1. Testes Automatizados
- Executar `python -m pytest tests/` ou script de testes com `python tests/test_backend.py` validando todas as rotas e regras de negócio.

### 2. Validação Manual do CRUD e Interface
- Iniciar a aplicação (`python main.py`).
- Acessar `http://127.0.0.1:8000` no navegador.
- Cadastrar um novo usuário e fazer login.
- Criar 3 disciplinas com cargas horárias diferentes (ex: 80h, 40h, 60h).
- Cadastrar tarefas variadas (pendentes, concluídas, atrasadas).
- Testar edição e exclusão de disciplinas e tarefas.
- Verificar a atualização em tempo real do dashboard (progresso ponderado, velocidade, previsão e recomendações).
- Testar a responsividade no modo mobile/tablet via inspeção do navegador.
- Acessar `http://127.0.0.1:8000/docs` para inspecionar a documentação interativa OpenAPI/Swagger.
