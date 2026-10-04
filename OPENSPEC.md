# OpenSpec — EduTrack AI (Projeto Integrador)

Documentação do ciclo de desenvolvimento, especificação das entregas, arquitetura e validações realizadas para o projeto **EduTrack AI — Assistente Educacional Personalizado**.

---

## 1. O que foi implementado

Foi desenvolvido um sistema Full Stack para auxílio na organização acadêmica e produtividade de estudantes universitários, contemplando:
1. **Módulo de Autenticação e Segurança**:
   - Cadastro de novos estudantes com nome, e-mail institucional e senha;
   - Login com geração de sessão/token Bearer persistido em banco de dados;
   - Recuperação de senha com atualização segura de hash criptográfico (PBKDF2-HMAC-SHA256);
   - Isolamento de dados no backend: cada estudante tem acesso restrito e exclusivo aos seus próprios registros.
2. **CRUD Completo de Disciplinas (`subjects`)**:
   - Criação, listagem com busca textual (`q`), detalhamento, edição e exclusão;
   - Registro de nome, professor, carga horária (horas), descrição e período letivo (início e término);
   - Exclusão em cascata (ao excluir disciplina, as tarefas vinculadas são removidas automaticamente).
3. **CRUD Completo de Tarefas Acadêmicas (`academic_tasks`)**:
   - Criação vinculada a uma disciplina existente do usuário;
   - Listagem com filtros combinados (por disciplina, por status `pending`/`completed`, busca textual por título/descrição e intervalo de datas previstas);
   - Alternância de status com 1 clique (toggle pendente/concluída com preenchimento automático de `completed_at`);
   - Detalhamento, edição e exclusão.
4. **Cálculos Avançados de Progresso com Python**:
   - **Progresso Ponderado pela Carga Horária**:
     $$\text{Progresso Ponderado} = \frac{\sum (\text{progresso\_disciplina} \times \text{carga\_horária})}{\sum \text{carga\_horária}}$$
     Diferencia disciplinas de maior carga (ex: 80h tem peso 2x maior que uma disciplina de 40h).
   - **Velocidade de Conclusão**:
     Calcula a taxa de tarefas concluídas por dia e por semana a partir dos registros temporais.
   - **Previsão de Término**:
     Projeta a data estimada de conclusão das tarefas pendentes com base na velocidade real; caso os dados sejam insuficientes (sem conclusões anteriores), exibe uma mensagem clara orientando o estudante sem inventar dados fictícios.
5. **Motor Determinístico de Recomendações Acadêmicas**:
   - Identificação de tarefas atrasadas (`due_date < hoje` e status pendente);
   - Alerta para disciplinas com baixo progresso (< 30%);
   - Indicação de prioridade para tarefas com prazo próximo (próximos 7 dias);
   - Notificação de bom ritmo para disciplinas com progresso $\ge 70\%$.
6. **Interface Web Responsiva**:
   - Desenvolvida em HTML5, CSS moderno e JavaScript nativo desacoplado;
   - Painel integrado com cards de métricas, gráficos interativos com Chart.js (gráfico de barras por disciplina e gráfico de distribuição de tarefas), modais para cadastro e edição rápida, filtros instantâneos e notificações toast.
7. **Documentação de APIs (Swagger/OpenAPI)**:
   - Disponibilizada de forma nativa e interativa no endpoint `/docs`.

---

## 2. Arquivos Criados e Alterados

| Arquivo | Descrição da Responsabilidade |
| :--- | :--- |
| `backend/database.py` | Configuração do SQLite, ativação de chaves estrangeiras (`PRAGMA foreign_keys = ON`), criação de tabelas e índices. |
| `backend/security.py` | Hashing de senhas seguro (PBKDF2), gerenciamento de sessões e injeção de dependência do usuário autenticado. |
| `backend/models.py` | Modelos Pydantic para validação das requisições e respostas das APIs. |
| `backend/services/metrics.py` | Algoritmos em Python para progresso ponderado, velocidade, previsão e recomendações determinísticas. |
| `backend/routers/auth_routes.py` | Endpoints REST de autenticação (`/register`, `/login`, `/forgot-password`, `/me`, `/logout`). |
| `backend/routers/subject_routes.py` | Endpoints REST do CRUD de disciplinas com filtros e cálculo de percentuais. |
| `backend/routers/task_routes.py` | Endpoints REST do CRUD de tarefas com busca combinada e endpoint de alternância de status. |
| `backend/routers/dashboard_routes.py` | Endpoints REST para resumo do dashboard, métricas avançadas e lista de recomendações. |
| `main.py` | Inicialização da aplicação FastAPI, configuração de CORS e montagem dos arquivos estáticos do frontend. |
| `frontend/index.html` | Interface SPA com abas de Dashboard, Disciplinas e Tarefas, formulários e modais responsivos. |
| `frontend/css/style.css` | Folha de estilos moderna e responsiva (suporte a desktop, tablet e celular). |
| `frontend/js/api.js` | Módulo cliente HTTP com gerenciamento de token Bearer e notificações toast. |
| `frontend/js/auth.js` | Controlador de autenticação, login, cadastro e recuperação de senha. |
| `frontend/js/dashboard.js` | Renderizador do dashboard, cards, gráficos Chart.js e métricas de Python. |
| `frontend/js/subjects.js` | Controlador do CRUD de disciplinas na interface do usuário. |
| `frontend/js/tasks.js` | Controlador do CRUD de tarefas, filtros combinados e alternância de status. |
| `frontend/js/app.js` | Coordenador de navegação entre abas e ciclo de vida da interface. |
| `DATA_DICTIONARY.md` | Dicionário de dados formal detalhando todas as tabelas, tipos e restrições. |
| `OPENSPEC.md` | Este documento de especificações abertas do projeto. |
| `requirements.txt` | Lista de dependências Python necessárias para execução do projeto. |
| `tests/test_backend.py` | Bateria de testes automatizados com cobertura de ponta a ponta. |

---

## 3. Funcionalidades Concluídas

- [x] **Autenticação de Usuários**:
  - [x] Cadastro com validação de dados e prevenção de duplicatas;
  - [x] Login com geração de token de sessão;
  - [x] Recuperação e redefinição de senha;
  - [x] Isolamento estrito de dados por estudante logado.
- [x] **Gestão de Disciplinas**:
  - [x] Criar disciplina com nome, professor, carga horária, datas e descrição;
  - [x] Listar disciplinas com busca textual dinâmica;
  - [x] Visualizar detalhes e progresso individual;
  - [x] Editar dados da disciplina;
  - [x] Excluir disciplina com confirmação e exclusão em cascata das tarefas vinculadas.
- [x] **Gestão de Tarefas Acadêmicas**:
  - [x] Criar tarefa vinculada a uma disciplina do estudante;
  - [x] Listar tarefas com filtros múltiplos (disciplina, status, busca e intervalo de datas);
  - [x] Visualizar detalhes e status de atraso;
  - [x] Marcar/desmarcar tarefa concluída em 1 clique (toggle);
  - [x] Editar dados da tarefa;
  - [x] Excluir tarefa com confirmação.
- [x] **Dashboard & Métricas Python**:
  - [x] Cards com total de disciplinas, tarefas pendentes, tarefas concluídas e progresso ponderado;
  - [x] Gráfico de progresso por disciplina (Chart.js);
  - [x] Gráfico de tarefas concluídas vs pendentes (Chart.js);
  - [x] Cálculo de velocidade de conclusão em tarefas por dia/semana;
  - [x] Previsão de conclusão com base na velocidade (ou mensagem amigável de dados insuficientes).
- [x] **Sistema de Recomendações**:
  - [x] Alertas determinísticos para tarefas atrasadas;
  - [x] Alertas para matérias com baixo progresso;
  - [x] Destaque para tarefas com prazo próximo;
  - [x] Reconhecimento de bom ritmo de estudos.

---

## 4. Testes Realizados

Os testes automatizados foram desenvolvidos com a biblioteca padrão `unittest` do Python em conjunto com `TestClient` e banco de dados isolado em memória temporária:

```powershell
python tests/test_backend.py
```

### Resultados dos Testes:
1. `test_01_health_check`: Validação do status da API e integridade do serviço. (**PASSOU**)
2. `test_02_auth_register_and_login`: Validação do fluxo de cadastro, bloqueio de e-mail duplicado, login e endpoint `/api/auth/me`. (**PASSOU**)
3. `test_03_password_reset`: Validação da redefinição de senha, invalidação de senha antiga e acesso com a nova senha. (**PASSOU**)
4. `test_04_subjects_crud_and_user_isolation`: Validação da criação de disciplinas (80h e 40h), listagem, busca textual, atualização, e garantia de que o Usuário B não acessa nem edita disciplinas do Usuário A. (**PASSOU**)
5. `test_05_tasks_crud_and_status_toggle`: Validação da criação de tarefas (incluindo cálculo de atraso), filtros combinados (por matéria, por status e por busca), alternância rápida de status (pendente <-> concluída com timestamp), edição e exclusão. (**PASSOU**)
6. `test_06_python_metrics_and_recommendations`: Validação matemática do cálculo de progresso ponderado ($33.3\%$ com pesos 80h vs 40h contra média simples de $50\%$), cálculo de velocidade, estimativa de conclusão e geração de recomendações de tarefas atrasadas. (**PASSOU**)

**Resultado Final dos Testes:**
> `Ran 6 tests in 1.050s — OK (100% de sucesso)`
