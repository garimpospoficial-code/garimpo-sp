# 🚀 INIT — Migração Garimpo SP pro Claude Code

> Roteiro de comandos pra migrar o projeto pra Claude Code com versionamento Git + GitHub.

---

## ✅ Pré-requisitos

- [x] Claude Code instalado (`claude --version`)
- [x] Conta GitHub
- [ ] (Opcional) GitHub CLI (`gh --version`) — facilita criar repo via terminal
- [ ] (Opcional) Netlify CLI (`netlify --version`) — facilita deploy

Se não tiver `gh` ou `netlify`:
```bash
# GitHub CLI (Windows via winget)
winget install --id GitHub.cli

# Netlify CLI (precisa Node.js)
npm install -g netlify-cli
```

---

## 🏗️ Setup Inicial (rodar 1 vez na pasta do projeto)

Abre terminal **na pasta `C:\Users\marce\Downloads\garimpo-sp`** e roda:

```bash
# 1. Inicializa Git
git init -b main
git add -A
git commit -m "feat: inicialização do projeto Garimpo SP

- Site V1 (Netlify-ready) em site/index.html
- Painéis ao vivo (Hub, Cockpit, Jarvis) em tools/
- 6 posts visuais + 5 slides carrossel + 2 capas reel em content/
- Catálogo de 7 produtos validados em data/catalog.json
- Estratégia completa em docs/ (plano 7 dias, divulgação, calendário, DMs, Linktree opt)
- Planilha de 20 prospects WarMachine em data/

Co-authored-by: Ultron <ultron@garimposp.local>"
```

```bash
# 2. Cria repo no GitHub (privado, recomendado)
# Opção A: via GitHub CLI
gh repo create garimpo-sp --private --source=. --remote=origin --push

# Opção B: manual
# - Vai em github.com/new
# - Nome: garimpo-sp · Privado
# - NÃO marca "initialize with README" (já temos)
# - Cria
# - Copia comandos que aparecem e roda aqui:
#   git remote add origin git@github.com:SEU_USER/garimpo-sp.git
#   git branch -M main
#   git push -u origin main
```

---

## 🎯 Iniciando Claude Code

```bash
# Na pasta do projeto:
cd C:\Users\marce\Downloads\garimpo-sp
claude
```

Quando abrir, primeira mensagem sugerida pra mim:

> "Olá Claude. Esse é o projeto Garimpo SP. Lê o README.md, INIT.md e dá um briefing do estado atual. Estou continuando do Cowork."

---

## 📋 O que pedir nas próximas sessões (sugestões)

### Site & Deploy

```
"Deploy do site/index.html no Netlify via CLI"
"Adiciona [produto X] no catalog.json e regenera o site/index.html"
"Cria página de produto individual /produto/mondial.html com mais detalhes"
```

### Conteúdo

```
"Gera mais 5 ideias de Reel pro Cockpit baseado no catalog.json"
"Cria carrossel novo de '5 itens essenciais pra mochila paulistana' (5 slides PNG)"
"Refaz capa Reel B sem emojis problemáticos"
```

### Automação

```
"Cria um script Python que lê catalog.json e gera HTML novo do site"
"Cria GitHub Action que faz deploy Netlify automático em todo push"
"Cria scheduled task que roda análise semanal do Amazon Associados"
```

### Analytics

```
"Adiciona Plausible Analytics no site (free tier 10k pageviews)"
"Cria script que extrai relatório CSV do Amazon Associados e gera dashboard"
```

---

## 🌐 Deploy Netlify via CLI (após `npm install -g netlify-cli`)

```bash
cd C:\Users\marce\Downloads\garimpo-sp\site
netlify deploy --prod --dir=.
```

Primeira vez ele pede pra logar via browser. Depois, a cada update do site:

```bash
netlify deploy --prod --dir=site
```

URL fica `garimposp.netlify.app` (ou nome que escolher).

---

## 🤝 Estrutura de commits sugerida

Use commit messages convencionais pra organizar:

```
feat: nova funcionalidade
fix: correção de bug
docs: atualização de documentação
content: novo post/reel/carrossel
refactor: reorganização sem mudar comportamento
chore: tarefas administrativas (gitignore, package.json, etc.)
```

Exemplos reais:

```bash
git commit -m "content: adiciona Reel C 'fim de semana chuvoso em SP'"
git commit -m "feat(site): adiciona produto novo (Mochila ergonômica) ao catálogo"
git commit -m "fix(site): corrige link de afiliação Amazon no card do Power Bank"
git commit -m "docs: atualiza plano-divulgacao com aprendizados da semana 1"
```

---

## 🔐 Secrets / Tokens

**NUNCA commita** API keys, tokens, senhas. Tudo isso vai em `.env` (já no `.gitignore`).

Quando precisar, cria `.env` na raiz com:

```bash
# .env (NÃO commita)
NETLIFY_AUTH_TOKEN=xxxxx
PLAUSIBLE_API_KEY=xxxxx
AMAZON_ASSOCIATES_TOKEN=xxxxx
```

---

## 🏃‍♂️ Comandos de operação dia-a-dia

```bash
# Ver estado do projeto
git status
git log --oneline -10

# Pull mudanças (se trabalhar de mais máquinas)
git pull

# Push após editar
git add -A
git commit -m "message"
git push

# Deploy site
netlify deploy --prod --dir=site

# Rodar Cockpit local pra testar
# (Windows)
start tools/garimpo-cockpit.html
```

---

## 🎯 Status da Migração

- [x] Estrutura de pastas reorganizada
- [x] README.md raiz
- [x] .gitignore
- [x] catalog.json centralizando produtos
- [x] INIT.md (este doc)
- [ ] `git init` + primeiro commit (você roda)
- [ ] GitHub repo criado e push (você roda)
- [ ] Claude Code apontando pra pasta (você abre)
- [ ] Deploy Netlify (você roda)

---

🔥 **Bora migrar. A partir daqui, cada linha de código tem versionamento.**

— Ultron · Garimpo SP
