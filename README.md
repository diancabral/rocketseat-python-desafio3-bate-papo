# Rocketseat Python — Desafio 3: Bate-papo

Aplicação web de sala de bate-papo em tempo real usando **Flask**, **Flask-SocketIO** e uma interface em **React** (via CDN) servida pelo próprio Flask.

https://github.com/user-attachments/assets/cc212f76-1240-4c34-ae98-e465f32cd875

## Pré-requisitos

- **Python** `>= 3.12.10` (conforme `pyproject.toml`)
- [uv](https://docs.astral.sh/uv/) (recomendado) ou `pip` com ambiente virtual

## Configuração

1. Clone o repositório e entre na pasta do projeto.
2. Crie o arquivo de ambiente a partir do exemplo:
  ```bash
   cp .env.example .env
  ```
3. Edite o `.env` e defina uma chave secreta forte para sessões e cookies do Flask:
  ```env
   SECRET_KEY=sua_chave_secreta_aqui
  ```
   O aplicativo carrega variáveis de ambiente a partir do `.env` na raiz do projeto (via `python-dotenv`).

## Instalação das dependências

Com **uv** (há um `uv.lock` no repositório):

```bash
uv sync
```

Com **pip** (alternativa):

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# .venv\Scripts\activate    # Windows
pip install -e .
```

## Como executar

Na raiz do projeto:

```bash
uv run python src/app.py
```

Com o venv já ativado e dependências instaladas:

```bash
python src/app.py
```

## Uso

1. Abra no navegador:
  `**http://127.0.0.1:5000/client/v1/chat/**`
2. Informe um nome e entre na sala. Mensagens, eventos de “digitando…” e entradas de outros usuários são sincronizados via WebSocket (Socket.IO).
3. Para testar com várias pessoas, abra a mesma URL em abas ou dispositivos diferentes na mesma rede (nesse caso você precisará expor o host/porta adequadamente e alinhar a URL em `routes.py` ao endereço acessível).

## Estrutura relevante


| Caminho                        | Descrição                                                                   |
| ------------------------------ | --------------------------------------------------------------------------- |
| `src/app.py`                   | Ponto de entrada: cria a app e inicia o Socket.IO                           |
| `src/config/`                  | Configuração da aplicação Flask e constantes (`SECRET_KEY`, prefixo da API) |
| `src/modules/chat/routes.py`   | Rota HTTP que renderiza `index.html`                                        |
| `src/modules/socket/events.py` | Handlers Socket.IO (`join`, `message_send`, `typing_*`)                     |
| `src/templates/index.html`     | Interface do chat (React + Tailwind via CDN)                                |


## Prefixo da API

O blueprint do chat usa o prefixo definido em `src/config/constants.py` (`API_PREFIX`, por padrão `/client`), resultando na URL base `/client/v1/chat/` para a página principal.

