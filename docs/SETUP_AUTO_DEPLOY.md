# 🚀 Setup do Auto-Deploy GitHub Actions → Netlify

> **Status atual**: workflow YAML pronto local (em `.github/workflows/deploy.yml`), mas não foi commitado. Secrets do GitHub Actions já configurados (`NETLIFY_AUTH_TOKEN` + `NETLIFY_SITE_ID`).
> **Falta apenas**: autorizar o gh CLI a criar workflows no repo. **2 min de setup**.

---

## ✅ O QUE JÁ TÁ PRONTO

- ✅ `NETLIFY_AUTH_TOKEN` setado como GitHub Actions secret
- ✅ `NETLIFY_SITE_ID` setado como GitHub Actions secret
- ✅ Arquivo `.github/workflows/deploy.yml` pronto na pasta local

## ⏳ FALTA APENAS 1 DAS 2 OPÇÕES ABAIXO

### 🅰️ Opção A — Pelo terminal (recomendado, mais limpo)

Abre PowerShell e roda:

```powershell
& "C:\Program Files\GitHub CLI\gh.exe" auth refresh -h github.com -s workflow
```

1. Vai imprimir um device code novo
2. Copia o code
3. Abre https://github.com/login/device
4. Cola → autoriza → pronto

Depois:

```powershell
cd C:\Users\marce\Downloads\garimpo-sp
git add .github/workflows/deploy.yml
git commit -m "feat: GitHub Action auto-deploy Netlify"
git push
```

A partir desse momento, **todo push pra `main` faz deploy automático em ~1 minuto**.

---

### 🅱️ Opção B — Pelo navegador (zero terminal)

1. Abre **https://github.com/garimpospoficial-code/garimpo-sp**
2. Clica em **Add file → Create new file**
3. Nome do arquivo (na barra de cima): `.github/workflows/deploy.yml` *(o GitHub vai criar as pastas automaticamente)*
4. **Cola o conteúdo abaixo:**

```yaml
name: Deploy to Netlify

on:
  push:
    branches: [main]
  workflow_dispatch:

jobs:
  deploy:
    name: Deploy site/ to garimposp.netlify.app
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@v4

      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install Netlify CLI
        run: npm install -g netlify-cli

      - name: Deploy to Netlify (production)
        run: netlify deploy --prod --dir=site --site "$NETLIFY_SITE_ID" --auth "$NETLIFY_AUTH_TOKEN" --message "Auto-deploy from commit $GITHUB_SHA"
        env:
          NETLIFY_SITE_ID: ${{ secrets.NETLIFY_SITE_ID }}
          NETLIFY_AUTH_TOKEN: ${{ secrets.NETLIFY_AUTH_TOKEN }}
```

5. Embaixo, clica **Commit new file** → main → Commit
6. **Pronto.** A partir do próximo push, deploy automático.

---

## 🧪 Como testar se tá funcionando

Depois do setup, faz uma alteração qualquer no `site/index.html` (vírgula que seja):

```powershell
cd C:\Users\marce\Downloads\garimpo-sp
git commit -am "test: trigger auto-deploy"
git push
```

Vai em **https://github.com/garimpospoficial-code/garimpo-sp/actions** e vai ver o workflow rodando. Em ~1 min, o site no Netlify reflete a mudança.

---

## ⚙️ Como o sistema funciona depois de setado

```
┌──────────────────────┐
│ Tu (ou eu) faz       │
│ git push pra main    │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ GitHub Actions       │
│ dispara workflow     │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Ubuntu runner roda:  │
│ npm i netlify-cli    │
│ netlify deploy --prod│
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ garimposp.netlify.app│
│ atualizado em ~1 min │
└──────────────────────┘
```

---

🔥 **Ativando isso, qualquer mudança no repo (artigo novo, ajuste no site, post novo) vira deploy de 1 min sem tocar em nada.**
