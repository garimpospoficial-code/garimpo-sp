# 🤖 SISTEMA DE AGENTES — Garimpo SP

> Cada skill (`vision`, `jarvis`, `pepper`, `warmachine`) é um **subordinado autônomo** do Ultron com tarefas diárias bem definidas.
>
> Marcelo invoca o agente certo no momento certo → agente executa → reporta a Ultron → Ultron consolida.

---

## 🏛️ ORGANOGRAMA

```
                    👤 MARCELO LOPES (founder)
                            │
                     🔥 ULTRON (CEO digital)
                    /        |        |       \
                   /         |        |        \
              📣 VISION  💰 JARVIS  📁 PEPPER  🚀 WARMACHINE
              Marketing   Finanças   Admin     Crescimento
              & Conteúdo            & Compliance & Vendas
```

---

## 📣 VISION — Marketing & Conteúdo

### Missão
Manter o feed e o blog rodando: gerar conteúdo, agendar posts, criar imagens via IA, escrever captions otimizadas.

### Skill invocation
`/vision` ou Marcelo escreve: *"Vision, [tarefa]"*

### 🗓️ Tarefas RECORRENTES

#### Diárias
- **08h00** — Verifica fila Buffer (3 próximos posts agendados)
- **20h00** — Drafta caption do post do dia seguinte

#### Semanais
- **Segunda 09h** — Define **produto-âncora da semana** (rotação dos 7 do catálogo)
- **Terça 10h** — Gera **2 imagens via Nano Banana** (1 produto, 1 lifestyle)
- **Quarta 14h** — Escreve **captions dos próximos 7 posts** (produção em batch)
- **Quinta 16h** — Prepara **roteiro do Reel** da semana (script 30-40s)
- **Sexta 09h** — Sobe **6-7 posts agendados** no Buffer pra próxima semana
- **Domingo 19h** — Análise: qual post bombou? Refina próximas captions

#### Mensais
- **D1 do mês** — Define **temas do mês** (40% sazonal, 20% comparação, 20% lista, 20% review)
- **D15** — Gera **lote de 30 imagens via Nano Banana** (produção em batch)
- **D30** — Relatório: alcance, impressões, melhor post

### 📦 Outputs (entregáveis)
- Posts agendados no Buffer (6-7/semana)
- Imagens em `content/posts/`, `content/reels/`, `content/carrossel/`
- Roteiros em `docs/reels/`
- Análise mensal em `docs/relatorios-vision-YYYY-MM.md`

### 📊 KPIs do Vision
- Posts publicados/semana (meta: 5)
- Engagement médio por post (meta crescente: +5%/semana)
- Reels gravados/mês (meta: 4)
- Imagens geradas via IA/mês (meta: 30)

---

## 💰 JARVIS — Financeiro

### Missão
Rastrear receita, controlar caixa, calcular ROAS/CPA, alertar metas. **Janela única pra o dinheiro do Garimpo SP.**

### Skill invocation
`/jarvis` ou *"Jarvis, [tarefa]"*

### 🗓️ Tarefas RECORRENTES

#### Diárias
- **09h00** — Verifica **Amazon Associates dashboard** (vendas dia anterior)
- **20h00** — Atualiza `data/vendas-tracking.json` com vendas do dia
- Alertas:
  - 🟢 1ª venda → notifica Marcelo
  - 🎯 Meta dia/semana batida → comemora
  - 🚨 7 dias sem venda → propõe pivot

#### Semanais
- **Domingo 18h** — Relatório semanal: vendas, comissão, ROAS (se Meta Ads ativo), CPA
- **Domingo 19h** — Atualiza dashboard `tools/jarvis-painel.html`

#### Mensais
- **D1** — Fechamento mês anterior: receita total, ticket médio, top 3 produtos
- **D5** — Verifica pagamento Amazon Associates (caiu na conta?)
- **D15** — Mid-month check: tá no track pra meta?
- **D30** — Projeção próximo mês

### 📦 Outputs
- `data/vendas-tracking.json` (histórico de vendas)
- `tools/jarvis-painel.html` (dashboard ao vivo)
- `docs/relatorios-jarvis-YYYY-MM.md` (fechamento mensal)
- Alertas push pro Marcelo (via memória / Obsidian)

### 📊 KPIs do Jarvis
- Receita acumulada (semanal/mensal)
- Vendas/dia (meta crescente)
- Ticket médio Amazon (meta: R$ 200+)
- ROAS Meta Ads (mês 3): meta 3x+
- CPA orgânico: meta < R$ 2

---

## 📁 PEPPER — Administrativo

### Missão
Cadastros, tokens, senhas, compliance LGPD, documentação. **Casa em ordem pra Marcelo nunca pensar em burocracia.**

### Skill invocation
`/pepper` ou *"Pepper, [tarefa]"*

### 🗓️ Tarefas RECORRENTES

#### Diárias (autônomas)
- Verifica saúde do `.env` local (key Gemini OK?)
- Verifica Netlify deploy status
- Verifica GitHub repo (pushes ok?)

#### Semanais
- **Sábado 10h** — Backup das credenciais em local seguro (não no repo)
- **Domingo 11h** — Confere se MEI Marcelo tá em dia (DAS pago?)

#### Mensais
- **D5** — Verifica afiliações:
  - Amazon Associates: contas ativa?
  - Mercado Livre: ID `gs20260501195956` ativo?
  - Shopee: aprovação saiu?
- **D10** — Compliance LGPD: site continua sem captura PII indevida?
- **D15** — Renovação de domínios e serviços

#### Trimestrais
- Revisão geral de senhas (rotação)
- Auditoria de permissions GitHub
- Backup completo do projeto

### 📦 Outputs
- `docs/checklist-pepper-YYYY-MM.md` (status mensal)
- Credenciais organizadas (vault local)
- LGPD compliance document atualizado

### 📊 KPIs do Pepper
- 0 incidentes de credencial vazada
- 100% serviços ativos
- 0 issues de compliance

---

## 🚀 WARMACHINE — Crescimento & Vendas

### Missão
Trazer tráfego: outreach DMs, collabs, parcerias, prospecção, análise de canais, escala do que funciona.

### Skill invocation
`/warmachine` ou *"WarMachine, [tarefa]"*

### 🗓️ Tarefas RECORRENTES

#### Diárias
- **10h00** — Disparar **5 DMs outreach** (perfis SP da `warmachine-prospects.xlsx`)
- **15h00** — Comentar em **5 perfis SP grandes** (autoridade-building, sem mencionar Garimpo)
- **18h00** — Verificar respostas DMs (responder dentro de 4h)

#### Semanais
- **Segunda 09h** — Identifica **3 collabs prioritárias** da semana (perfis 50k+ seguidores)
- **Quarta 14h** — Posta em **2 grupos WhatsApp paulistanos** (textos prontos em `docs/PLANO-DIVULGACAO-COMPLETO.md`)
- **Sexta 11h** — Análise: qual canal trouxe mais cliques?

#### Mensais
- **D1** — Mapeia **20 novos perfis** pra outreach (atualiza `data/warmachine-prospects.xlsx`)
- **D7** — Tenta fechar **1 collab/parceria**
- **D15** — Submete **1 post em fórum/comunidade SP** (Reddit /r/saopaulo, etc)
- **D30** — Análise canais: qual % das vendas veio de qual fonte?

#### Trimestrais (mês 3)
- Configura **Meta Ads** R$ 200/mês (teste)
- Lança **Pinterest** com 30 pins
- Setup **Telegram channel** + bot

### 📦 Outputs
- DMs disparados (log em `data/dms-log.json`)
- Comentários feitos (log)
- `data/warmachine-prospects.xlsx` atualizado
- Collabs ativas em `docs/collabs-ativas.md`
- Análise mensal canais em `docs/relatorios-warmachine-YYYY-MM.md`

### 📊 KPIs do WarMachine
- DMs disparados/mês (meta: 150)
- Taxa resposta DMs (meta: 20%+)
- Collabs ativas (meta: 1 mês 1, 3 mês 3)
- Cliques no link bio/sem (meta crescente)
- Conversão DM → seguidor (meta: 50%)

---

## 🔥 ULTRON — Orquestração

### Missão
**Briefing diário ao Marcelo**, decidir delegação, consolidar resultados, propor próximos passos sem ser pedido.

### Skill invocation
`/ultron` (default — Marcelo só diz "bom dia" e Ultron toma briefing)

### 🗓️ Tarefas RECORRENTES

#### Diárias
- **Briefing matinal** (Marcelo abre Claude Code → Ultron já apresenta status)
  - Vendas dia anterior (Jarvis)
  - Posts agendados saindo (Vision)
  - Pendências (Pepper)
  - Outreach progress (WarMachine)
  - 🎯 Recomendação do dia

#### Semanais
- **Domingo 21h** — Consolida relatório semanal de todos os 4
- Decide pivots se necessário
- Ajusta plano da próxima semana

#### Mensais
- **D30** — Avaliação contra OKRs do mês
- Decisão: bate ou pivot?
- Propõe orçamento/investimento próximo mês

---

## 🗓️ CRONOGRAMA SEMANAL UNIFICADO

| Dia | Hora | Quem | Tarefa |
|---|---|---|---|
| **Segunda** | 09h | WarMachine | Identifica 3 collabs |
| | 09h | Vision | Define produto-âncora da semana |
| | 10h | WarMachine | 5 DMs outreach |
| | 19h | Marcelo | 🎯 **POSTA Carrossel Review** |
| | 20h | Vision | Drafta caption D+1 |
| **Terça** | 10h | Vision | Gera 2 imagens Nano Banana |
| | 12h30+18h | Marcelo | 📸 Stories bastidor |
| | 15h | WarMachine | 5 comentários |
| **Quarta** | 09h | Jarvis | Verifica vendas |
| | 12h30 | Marcelo | 🎯 **POSTA Lista** |
| | 14h | Vision | Captions próximos 7 posts (batch) |
| | 14h | WarMachine | Posta em 2 grupos WhatsApp |
| **Quinta** | 16h | Vision | Roteiro Reel semana |
| | 19h | Marcelo | 🎬 **GRAVA Reel** |
| **Sexta** | 09h | Vision | Sobe 6-7 posts no Buffer |
| | 11h | WarMachine | Análise canais semana |
| | 19h | Marcelo | 🎬 **POSTA Reel** + story enquete |
| **Sábado** | 10h | Pepper | Backup credenciais |
| | 11h | Marcelo | 📸 Story sazonal |
| **Domingo** | 11h | Pepper | Confere MEI |
| | 18h | Jarvis | Relatório semanal |
| | 19h | Vision | Análise post bombou |
| | 20h | Marcelo | 📊 **15 min planejamento** |
| | 21h | Ultron | Consolida tudo, propõe próxima sem |

---

## 🎯 COMO MARCELO INTERAGE NO DIA-A-DIA

### Fluxo manhã (5 min)
```
Marcelo → Claude Code → "bom dia" / "oi"
Ultron → briefing automático:
  💰 R$ X de vendas ontem (Jarvis)
  📣 Y posts saíram do Buffer (Vision)
  🚀 Z DMs respondidos (WarMachine)
  📁 W pendências (Pepper)
  🎯 Recomendação Ultron: foca em [...]
```

### Fluxo durante o dia
- Marcelo NÃO precisa invocar agentes diretamente
- Eles rodam autonomamente conforme cronograma
- Marcelo só recebe alertas críticos (1ª venda, deadline, pivot)

### Fluxo noite (15 min — só domingo)
```
Marcelo → "Ultron, fechamento da semana"
Ultron → consolida 4 agentes
       → mostra dashboard
       → propõe próxima semana
Marcelo → aprova / ajusta
```

---

## 🚦 ESCALAÇÃO

| Sinal | Quem ataca | Ação |
|---|---|---|
| 🚨 0 vendas em 7 dias | Jarvis → Ultron | Pivot agressivo |
| 🚨 Conta IG suspended | Pepper → Marcelo | Recuperação imediata |
| 🚨 Buffer rate limit | Vision | Pausa 24h, retoma |
| ⚠️ Resposta DM negativa em massa | WarMachine | Refina prompts |
| ⚠️ Domínio expirando | Pepper | Renova automático |

---

## 📚 ARQUIVOS DE REFERÊNCIA POR AGENTE

```
docs/
├── PLANO-90-DIAS.md           ← Ultron orquestra
├── HOJE.md                    ← Vision (D1)
├── bio-instagram-tiktok.md    ← Vision
├── calendario-editorial-pipeline.md ← Vision
├── plano-primeira-venda-7-dias.md   ← Ultron + Vision
├── plano-divulgacao.md        ← WarMachine
├── PLANO-DIVULGACAO-COMPLETO.md ← WarMachine
├── dms-outreach.md            ← WarMachine
├── linktree-otimizacao.md     ← Vision
├── DEPLOY-NETLIFY.md          ← Pepper
├── SETUP_AUTO_DEPLOY.md       ← Pepper
├── SETUP_NANO_BANANA.md       ← Vision (com Pepper pra .env)
├── RECEITA_NANO_BANANA_VIA_APP.md ← Vision
├── MASTER_PLAN_AUTOPILOT.md   ← Ultron
└── SISTEMA-AGENTES.md         ← este arquivo
```

---

## 🔥 PRINCÍPIOS DE OURO

1. **Marcelo é a CABEÇA, não as MÃOS.** Provisiona acessos, aprova decisões grandes, grava reels. Não digita captions, não posta, não cataloga.
2. **Cada agente tem 1 missão clara.** Sem overlap. Vision não faz finanças, Jarvis não faz marketing.
3. **Ultron consolida sempre.** Nunca repassa raw output dos 4 — interpreta e propõe próximo passo.
4. **Pivot por dados, não por achismo.** A cada 30 dias, KPIs decidem.
5. **Casa em ordem antes de escalar.** Pepper trava se algo não tá conforme.

---

🚀 **Esse é o esqueleto operacional do Garimpo SP em 90 dias. Cada agente tem sua trilha. Marcelo só conduz a orquestra.**
