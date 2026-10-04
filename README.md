# EduTrack AI — Assistente Educacional Personalizado

> **Projeto Integrador (PI)** — Sistema Full Stack para organização de disciplinas, tarefas e acompanhamento de progresso acadêmico com métricas calculadas em Python.

---

## 🌟 Visão Geral

O **EduTrack AI** foi desenvolvido para solucionar a desorganização enfrentada por estudantes com múltiplas disciplinas e prazos acadêmicos. O sistema centraliza disciplinas e tarefas, calcula métricas acadêmicas avançadas em Python (como progresso ponderado pela carga horária) e fornece recomendações determinísticas para priorização de estudos.

### Principais Destaques:
- **Autenticação Completa com Isolamento**: Cadastro, Login, Recuperação de Senha e garantia de que cada aluno só acessa seus próprios dados.
- **CRUD Completo de Disciplinas e Tarefas**: Cadastro, listagem, filtros múltiplos, busca dinâmica, edição e exclusão com integridade referencial (`PRAGMA foreign_keys = ON`).
- **Métricas Avançadas em Python**:
  - *Progresso Ponderado*: Leva em conta a carga horária de cada matéria (disciplinas de 80h possuem peso maior que matérias de 40h).
  - *Velocidade de Conclusão*: Cálculo de tarefas concluídas ao longo do tempo (por dia e por semana).
  - *Previsão de Conclusão*: Projeta a data estimada de conclusão das pendências, exibindo aviso caso os dados sejam insuficientes.
- **Recomendações Determinísticas**: Alertas inteligentes baseados em prazos e status reais (tarefas atrasadas, baixo progresso, entregas próximas e bom ritmo).
- **Interface Web e Mobile Responsiva**: Desenvolvida em HTML5, CSS moderno e JavaScript nativo com gráficos interativos (Chart.js) e documentação Swagger integrada em `/docs`.
- **Documentação Acadêmica**: [Dicionário de Dados](DATA_DICTIONARY.md) e especificação [OpenSpec](OPENSPEC.md).

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem Principal**: Python 3.10+
- **Backend / APIs**: FastAPI, Uvicorn, Pydantic
- **Banco de Dados**: SQLite3 com Foreign Keys ativadas
- **Criptografia e Segurança**: PBKDF2-HMAC-SHA256 e Tokens Bearer
- **Frontend**: HTML5, CSS3 Responsivo, JavaScript (ES6+), Chart.js
- **Testes**: Python `unittest` com `TestClient`

---

## 📁 Estrutura do Projeto

```text
Edu Track 2/
├── backend/
│   ├── database.py             # Configuração do SQLite e tabelas
│   ├── security.py             # Hash de senhas e autenticação
│   ├── models.py               # Schemas de validação Pydantic
│   ├── services/
│   │   └── metrics.py          # Métricas de progresso, velocidade e recomendações
│   └── routers/
│       ├── auth_routes.py      # Endpoints de cadastro, login e perfil
│       ├── subject_routes.py   # Endpoints de CRUD de disciplinas
│       ├── task_routes.py      # Endpoints de CRUD de tarefas
│       └── dashboard_routes.py # Endpoints de resumo e métricas
├── frontend/
│   ├── index.html              # Interface do usuário (SPA)
│   ├── css/
│   │   └── style.css           # Estilos modernos e responsivos
│   └── js/
│       ├── api.js              # Cliente HTTP e toasts
│       ├── auth.js             # Gerenciamento de login e sessão
│       ├── dashboard.js        # Gráficos Chart.js e estatísticas
│       ├── subjects.js         # Interface de disciplinas
│       ├── tasks.js            # Interface de tarefas e filtros
│       └── app.js              # Roteamento e inicialização
├── tests/
│   └── test_backend.py         # Testes automatizados ponta a ponta
├── main.py                     # Inicialização do servidor FastAPI
├── requirements.txt            # Dependências Python
├── DATA_DICTIONARY.md          # Dicionário de Dados do banco
├── OPENSPEC.md                 # Documentação OpenSpec
└── README.md                   # Instruções do projeto
```

---

## 🚀 Como Executar o Projeto

### 1. Clonar ou Acessar a Pasta do Projeto
Abra o terminal (PowerShell ou Bash) na raiz do projeto:
```powershell
cd "c:\Users\kris1\OneDrive\Documentos\Edu Track 2"
```

### 2. Instalar as Dependências
```powershell
python -m pip install -r requirements.txt
```

### 3. Iniciar o Servidor
Execute o comando:
```powershell
python main.py
```
Ou com o Uvicorn diretamente:
```powershell
python -m uvicorn main:app --reload --port 8000
```

### 4. Acessar a Aplicação
- **Interface do Usuário (Web & Mobile)**: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- **Documentação Interativa das APIs (Swagger)**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

#### 👤 Usuário de Demonstração (Seed Automático):
- **E-mail**: `demo@edutrack.ai`
- **Senha**: `Demo@1234`
- **Nome**: Aluno Demo (4 disciplinas e 14 tarefas pré-cadastradas com métricas completas no dashboard).

---

## 🧪 Como Executar os Testes Automatizados

Para rodar a suíte completa de testes (Auth, CRUD, Isolamento, Cálculos em Python e Recomendações):

```powershell
python tests/test_backend.py
```

Saída esperada:
```text
Ran 6 tests in 1.050s

OK
```

---

## 📋 Roteiro Sugerido para Apresentação Acadêmica

1. **Apresentação do Problema**: Destacar a necessidade do estudante de acompanhar matérias e prazos com visão de prioridade.
2. **Demonstração do Sistema**:
   - Criar uma nova conta de estudante e efetuar login;
   - Cadastrar 2 disciplinas com cargas horárias diferentes (ex: *Engenharia de Software - 80h* e *Banco de Dados - 40h*);
   - Cadastrar tarefas para ambas as disciplinas (com datas futuras e uma data retroativa para demonstrar a detecção de atraso);
   - Alternar uma tarefa para "concluída" pelo checkbox e observar a atualização instantânea do percentual;
   - Visualizar o **Dashboard**:
     - Notar que o **Progresso Ponderado** prioriza a matéria de maior carga horária;
     - Analisar os gráficos de barras e de distribuição de tarefas;
     - Conferir os blocos de **Velocidade de Conclusão** e **Previsão de Término** calculados em Python;
     - Observar as **Recomendações Determinísticas** alertando sobre a tarefa atrasada e indicando a próxima entrega prioritária.
3. **Validação das APIs**: Abrir [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) e mostrar os endpoints REST funcionando em tempo real.
4. **Execução dos Testes**: Rodar `python tests/test_backend.py` no terminal demonstrando a cobertura automatizada.
