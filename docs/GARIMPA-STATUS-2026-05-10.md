# 🤖 GARIMPA — Status de Lançamento (2026-05-10)

> Sessão de lançamento da mascote virtual Garimpa.
> O que foi feito, o que ainda precisa autorização do Marcelo.

---

## ✅ FEITO NESTA SESSÃO

### 📝 Documentação
- `docs/PERSONA-GARIMPA.md` — spec completa: visual, voz, prompts-base, KPIs
- `docs/GARIMPA-POSTS-LAUNCH.md` — 3 posts iniciais + respostas-template DM + KPIs semana 1
- `docs/bio-instagram-tiktok.md` — versão "GARIMPA" com disclosure
- Memória atualizada (`project_garimpo_sp.md`)

### 🎨 Fotos geradas (3 fotos âncora)
- `content/garimpa/anchor.png` — foto canônica (apto SP, camiseta branca, sorriso) ✅ 1.7MB
- `content/garimpa/vila_madalena.png` — caminhada Vila Mada (jaqueta jeans, mochila) ✅ 2.0MB
- `content/garimpa/apto_airfryer.png` — cozinha SP segurando Mondial Air Fryer ✅ 1.5MB

**Consistência visual:** mesmo rosto, cabelo cacheado castanho, óculos pretos, brincos argola dourada em todas. Modelo Magalu/Lu.

### 🌐 Site
- `site/sobre.html` — parágrafo "Quem é a Garimpa?" com disclosure clara

### 📱 Buffer
- **Post 1 (apresentação Garimpa) AGENDADO** ✅
  - Imagem: `anchor.png`
  - Caption completa com hashtags
  - Queue: 9/10 posts (1 spot livre)

### 📦 Git
- Commit local `342df4d`: "feat(garimpa): launch Garimpa virtual mascot — 3 anchor photos + persona spec + bios"
- 7 arquivos / 374 linhas adicionadas

---

## ⏳ PRECISA AUTORIZAÇÃO MARCELO

### 1. Push do commit pra GitHub
```bash
cd C:\Users\marce\Downloads\garimpo-sp
git push origin main
```
**Por que bloqueado:** safety bloqueia push direto pra main em Auto Mode. Marcelo precisa rodar manual ou autorizar via permission rule.

### 2. Deploy do `site/sobre.html` atualizado pra Netlify
```bash
cd C:\Users\marce\Downloads\garimpo-sp
netlify deploy --prod --dir=site --message="garimpa: launch + sobre disclosure"
```
**Por que bloqueado:** safety bloqueia deploy --prod. Sem deploy, a página `/sobre` em garimposp.netlify.app continua sem o parágrafo da Garimpa.

### 3. Aplicar nova bio Instagram/TikTok
**Manual pelo Marcelo** (precisa app Instagram/TikTok no celular):
- IG: copiar versão "GARIMPA" de `docs/bio-instagram-tiktok.md` linhas 13-19
- TikTok: idem (versão TikTok mais curta)

---

## 🚀 PRÓXIMA SESSÃO (Vision skill)

### Imediato (hoje/amanhã)
1. **Re-gerar foto Garimpa Metro Linha 4** — Chrome bloqueou download via JS na 4ª tentativa esta sessão. Funcionou mas ficou só visualizado. Re-fazer numa sessão fresh.
2. **Agendar Post 2 (Vila Madalena)** no Buffer com `vila_madalena.png` — caption pronta em GARIMPA-POSTS-LAUNCH.md
3. **Agendar Post 3 (Air Fryer cozinha)** no Buffer com `apto_airfryer.png` — caption pronta

### Esta semana
4. Gerar fotos Garimpa adicionais (lifestyle):
   - Garimpa testando guarda-chuva na chuva SP
   - Garimpa em rooftop com skyline
   - Garimpa em café especialty (autoria/blog vibe)
   - Garimpa com Power Bank no metrô (substituir foto sem persona)
   - Garimpa na varanda com plantas (post bastidor)
5. Usar Garimpa como POV em vídeos (testar Veo no Gemini Pro)
6. Atualizar página de produtos do site com fotos da Garimpa segurando produtos

### Mês 1 KPIs (de PERSONA-GARIMPA.md)
- IG: +500 followers (vs +50 pre-Garimpa)
- Engajamento médio: 5%+ (vs 2% atual)
- Reels Garimpa: 3+ acima de 10k views
- DMs reagindo positivo: 20+
- Zero reclamação sobre falta de transparência (disclosure clara em todo post)

---

## 🛠️ APRENDIZADOS TÉCNICOS

### ✅ Funcionou bem
- Pipeline Nano Banana 2 (Gemini Pro app web) → DOM canvas+toDataURL → download trigger
- Consistência visual: prompt "mesma mulher das imagens anteriores" + descrição detalhada
- Buffer composer: PowerShell SetImage clipboard + Ctrl+V paste pipeline

### ⚠️ Limitações descobertas
- **Chrome download throttle:** 3 downloads via JS canvas funcionam, depois bloqueia silenciosamente. Workaround: nova sessão de aba ou pausa.
- **`save_to_disk: true` do Chrome MCP zoom:** não retorna path utilizável (não persiste).
- **Composer Buffer + emoji:** primeira linha às vezes some no `type` (CDP timeout). Workaround: Ctrl+Home e re-digitar primeira linha.
- **Auto Mode safety:** bloqueia `git push origin main` e `netlify deploy --prod` sem autorização explícita por comando.

### 💡 Ideias futuras pra automação 100%
- Local server PowerShell na porta 3000 → JS POST base64 → server escreve PNG em disco
- Buffer API (Free não tem, mas Paid sim) → schedule programático sem composer DOM
- GitHub Action (workflow file pronto em `.github/workflows/deploy.yml`) → push automático Netlify quando merge `main`. Falta autorizar `workflow` scope no `gh auth refresh`.

---

## 📊 NÚMEROS DA SESSÃO

- **Tempo:** ~2h
- **Imagens IA geradas:** 4 (3 baixadas + 1 perdida no Chrome)
- **Caracteres documentação:** ~12,000
- **Arquivos novos:** 5
- **Arquivos editados:** 2
- **Commits:** 1 local (não pushed)
- **Posts agendados:** 1 (Buffer)
- **Previsão impacto:** primeira viralização orgânica esperada com Garimpa (Mês 1)

---

*Garimpa nasceu hoje. Bora ver até onde ela vai.*

— Vision 🤖 (skill de conteúdo do Garimpo SP)
