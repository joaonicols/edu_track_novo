# Walkthrough — EduTrack AI (Projeto Integrador)

O projeto acadêmico **EduTrack AI — Assistente Educacional Personalizado** foi desenvolvido integralmente, atendendo a todos os requisitos do Projeto Integrador e respeitando os princípios de simplicidade, estabilidade, funcionalidade e apresentação acadêmica.

---

## 1. O que foi Construído

### Backend & APIs RESTful (FastAPI + SQLite)
- **Estrutura de Banco de Dados**: SQLite com `PRAGMA foreign_keys = ON`, contendo as tabelas `users`, `subjects`, `academic_tasks` e `user_sessions`, devidamente indexadas.
- **Autenticação Segura & Isolamento de Usuários**:
  - Hashing seguro via PBKDF2-HMAC-SHA256 com salt individual;
  - Sessões Bearer com expiração;
  - Garantia de que cada estudante tem visão e controle restrito aos seus próprios dados.
  - Endpoints: `POST /api/auth/register`, `POST /api/auth/login`, `POST /api/auth/forgot-password`, `GET /api/auth/me`, `POST /api/auth/logout`.
- **CRUD de Disciplinas**:
  - Cadastro, listagem com busca textual, detalhamento, atualização e exclusão em cascata;
  - Campos: nome, professor, carga horária, descrição, data de início e término.
- **CRUD de Tarefas**:
  - Cadastro vinculado a disciplinas existentes, listagem com filtros combinados (disciplina, status, busca e intervalo de datas), alternância rápida de status (toggle concluída/pendente) e exclusão;
  - Detecção automática de tarefas atrasadas (`due_date < hoje`).

### Cálculos Avançados em Python
- **Progresso Ponderado por Carga Horária**:
  $$\text{Progresso Ponderado} = \frac{\sum (\text{progresso\_disciplina} \times \text{carga\_horária})}{\sum \text{carga\_horária}}$$
  Exemplo validado: Uma disciplina de 80h tem o dobro do peso de uma matéria de 40h.
- **Velocidade de Conclusão**:
  Métrica em tarefas por dia e tarefas por semana com base no histórico real de finalizações.
- **Previsão de Conclusão**:
  Estimativa em dias e data projetada para término das tarefas restantes; quando não há dados suficientes, exibe mensagem clara e orientativa sem inventar dados.
- **Motor de Recomendações Determinístico**:
  Identifica e alerta sobre tarefas atrasadas, baixo progresso em disciplinas, priorização de entregas próximas e elogio para disciplinas com bom ritmo.

### Frontend Web & Mobile Responsivo
- Interface em Português do Brasil, moderna, com tema acadêmico e mobile-first.
- **Dashboard Integrado**:
  - 4 cards de visão geral (Disciplinas, Tarefas Pendentes, Concluídas, Progresso Ponderado);
  - Banner de Métricas Python (Velocidade e Previsão de Conclusão);
  - Lista de Recomendações Determinísticas em destaque;
  - Gráfico de barras com progresso por disciplina (Chart.js);
  - Gráfico de pizza/rosca com tarefas concluídas vs pendentes (Chart.js).
- **Aba de Disciplinas**: Cards com barra de progresso visual, carga horária, professor, período letivo, botão de atalho para tarefas da disciplina, botões de editar e excluir com modal.
- **Aba de Tarefas**: Filtro por disciplina, por status, busca por texto, filtro de datas, checkbox para alternar conclusão em tempo real, botões de editar e excluir.
- **Notificações Toast**: Feedback em tempo real para ações de sucesso, erro ou alerta.

### Documentação Acadêmica
- [DATA_DICTIONARY.md](file:///c:/Users/kris1/OneDrive/Documentos/Edu%20Track%202/DATA_DICTIONARY.md): Dicionário de dados completo com tipos, chaves PK/FK e descrições.
- [OPENSPEC.md](file:///c:/Users/kris1/OneDrive/Documentos/Edu%20Track%202/OPENSPEC.md): Registro OpenSpec com histórico de implementação e escopo de testes.
- [README.md](file:///c:/Users/kris1/OneDrive/Documentos/Edu%20Track%202/README.md): Guia de instalação, execução e apresentação para os avaliadores.

---

## 2. Validação e Resultados dos Testes

Executamos a suíte automatizada `tests/test_backend.py` cobrindo todas as regras de negócio:

```powershell
python tests/test_backend.py
```

### Resultados Obtidos:
| Teste | Escopo Testado | Resultado |
| :--- | :--- | :---: |
| `test_01_health_check` | Disponibilidade do serviço da API | ✅ PASSOU |
| `test_02_auth_register_and_login` | Cadastro, login, bloqueio de e-mail duplicado e `/me` | ✅ PASSOU |
| `test_03_password_reset` | Recuperação e redefinição de senha | ✅ PASSOU |
| `test_04_subjects_crud_and_user_isolation` | CRUD de Disciplinas e isolamento estrito de dados entre usuários | ✅ PASSOU |
| `test_05_tasks_crud_and_status_toggle` | CRUD de Tarefas, filtros combinados e alternância de status | ✅ PASSOU |
| `test_06_python_metrics_and_recommendations` | Progresso ponderado, velocidade, previsão e recomendações | ✅ PASSOU |
| `tests/test_demo_seed.py` (6 testes) | Validação do seed demo (idempotência, login, 4 matérias, 14 tarefas, dashboard e CRUD) | ✅ PASSOU |

**Status Geral:** `Todos os testes passando com 100% de sucesso.`

---

## 3. Usuário de Demonstração (Seed)

- **E-mail**: `demo@edutrack.ai`
- **Senha**: `Demo@1234`
- **Disciplinas**: Programação (80h), Banco de Dados (60h), Engenharia de Software (60h), Inteligência Artificial (80h).
- **Tarefas**: 14 tarefas distribuídas entre concluídas (6), pendentes (8) e atrasadas (2).

---

## 3. Como Iniciar a Aplicação

Para rodar o sistema e apresentar ao professor ou avaliadores:

1. No terminal do projeto:
   ```powershell
   python main.py
   ```
2. Abra no navegador:
   - **Aplicação Completa**: [http://127.0.0.1:8000](http://127.0.0.1:8000)
   - **Documentação Interativa Swagger**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
