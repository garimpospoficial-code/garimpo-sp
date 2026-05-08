# 🚀 MASTER PLAN — Garimpo SP em Modo Autopilot

> **Filosofia**: 3 motores rodando 24/7 + 3 aceleradores pra escalar. Mínimo trabalho braçal, máximo retorno orgânico.

---

## 🟢 MOTOR 1 — SEO BLOG MASSIVO (autopilot real)

### O que é
30–100 artigos em `garimposp.netlify.app/blog/` que ranqueiam no Google em 3–6 meses e geram tráfego perpétuo.

### Por que funciona
- **Long-tail keywords paulistanas**: "melhor air fryer apto pequeno SP", "fone metrô são paulo", "guarda-chuva temporal paulistano"
- **Programmatic SEO**: 1 template gera N páginas (produto × bairro = milhares de páginas)
- **Tráfego perpétuo**: artigo de 2026 ainda traz cliques em 2030
- **Conversão**: visitante via Google já tem intenção de compra (CTR pra Amazon: 5–8%)

### Stack
- **Local**: `site/blog/` versionado em Git
- **Deploy**: GitHub Action push → Netlify (já configurado)
- **Geração**: Claude API (script Python `scripts/gen_seo_post.py`) lê `data/catalog.json` + lista de keywords e gera artigos prontos

### Roadmap
| Sprint | Quantidade | Trabalho |
|---|---|---|
| Mês 1 | 5 artigos âncora | Eu escrevo manualmente, qualidade máxima |
| Mês 2 | +20 artigos | Eu gero via Claude API + revisão Marcelo |
| Mês 3 | +30 artigos programmatic | Templates por bairro × produto |
| Mês 4+ | atualizações + remix | 1× / mês: review e refresh |

### Métricas
- Tráfego orgânico mensal (Google Search Console)
- CTR pra Amazon (`ascsubtag=blog_*`)
- Conversão Amazon Associates por artigo

---

## 🟢 MOTOR 2 — LISTA PRÓPRIA (email + WhatsApp + Telegram)

### O que é
Captura email/WhatsApp do visitante e dispara sequências automatizadas. Lista própria é o ativo mais valioso do digital — Insta pode banir, Google pode mudar algoritmo, mas seu email/WhatsApp ninguém tira.

### Stack
- **Email capture**: Netlify Forms (built-in, $0)
- **Email marketing**: MailerLite Free (até 1k leads, ilimitado em emails)
- **WhatsApp**: WhatsApp Business → lista de transmissão (256 contatos/lista)
- **Telegram**: bot que envia promoções no canal

### Sequência de boas-vindas (5 emails automáticos)
1. **Dia 0**: "Bem-vindo ao Garimpo SP" + 3 produtos âncora
2. **Dia 2**: "O erro #1 do paulistano em casa" + Mondial Air Fryer
3. **Dia 5**: "Como economizei R$ 200/mês em delivery" + cross-sell
4. **Dia 10**: "Achadinho da semana" (atualizado dinamicamente)
5. **Dia 14+**: newsletter quinzenal automatizada

### Roadmap
| Sprint | Marco |
|---|---|
| Mês 1 | Captura no site (Netlify Forms) + MailerLite setup |
| Mês 2 | Sequência de 5 emails escrita + automação |
| Mês 3 | WhatsApp Business + 1ª lista de transmissão |
| Mês 4 | Telegram bot publicando promoções |

### Métricas
- Inscritos/dia
- Open rate (target: >25%)
- Click rate (target: >5%)
- Conversão Amazon via newsletter

---

## 🟢 MOTOR 3 — SOCIAL AUTOMATIZADO (90%)

### O que é
Instagram + TikTok rodando com 5 min/semana de trabalho braçal.

### Stack
- **Geração de conteúdo**: Vision (skill Claude) gera 20 posts/mês em batch
- **Agendamento**: Buffer Free (3 channels grátis) ou Metricool ($0)
- **Auto-resposta DM**: ManyChat Free (até 1k contatos)
- **Cross-posting**: Buffer permite postar IG + FB + TikTok com 1 click

### Workflow mensal
1. **1× / mês** (30 min): Vision entrega 20 posts (PNG + caption + hashtags) numa pasta
2. **Marcelo** (10 min): drag & drop no Buffer, agenda nos próximos 30 dias
3. **Buffer** posta automaticamente nos horários ótimos
4. **ManyChat** responde DMs comuns ("qual link da air fryer?" → manda link da bio)

### Roadmap
| Sprint | Marco |
|---|---|
| Mês 1 | Buffer setup + 20 posts gerados |
| Mês 2 | ManyChat setup com 5 fluxos comuns |
| Mês 3 | Otimizar com base em Insights (qual tema converte) |

### Métricas
- Reach mensal
- Cliques no link da bio
- DMs respondidos por ManyChat

---

## 🚀 ACELERADORES

### Acelerador 1 — Pinterest BR (SUBESTIMADO)

50M usuários BR. Pins ranqueiam no Google E na própria Pinterest. Cada pin pode trazer cliques por **anos**.

- **Trabalho**: 30 min/mês upload bulk
- **Custo**: $0
- **Pipeline**: cada produto = 5–10 pins (eu gero PNGs verticais 1000×1500)
- **Escala**: 100 pins ativos = 1k–5k cliques/mês potenciais

### Acelerador 2 — YouTube Shorts (repurpose)

Transforma cada Reel/TikTok em YouTube Short. YouTube paga via Shorts Fund + Shorts pode viralizar muito.

- **Trabalho**: 0 min (CapCut exporta direto)
- **Custo**: $0
- **Bônus**: views YouTube = receita direta + cliques pro site

### Acelerador 3 — AI Avatar (HeyGen / Synthesia)

Avatar IA fala roteiro de review de produto. Você nem aparece. Posta em IG/TikTok/YouTube.

- **Trabalho**: 5 min/vídeo (gerar avatar + script)
- **Custo**: $30/mês HeyGen
- **Volume**: 10 vídeos/mês fácil
- **Vale a pena**: ROI positivo se gera 1 venda extra/mês (R$ 19 × 10 = R$ 190 vs R$ 150 custo)

### Acelerador 4 — Programmatic SEO

Template HTML gera N páginas. Exemplo: 7 produtos × 96 bairros SP = **672 páginas únicas** ranqueando no Google.

- **Trabalho**: 0 (script Python gera tudo)
- **Custo**: $0
- **Cuidado**: Google penaliza se for thin content. Cada página precisa de pelo menos 300 palavras únicas (gerado por Claude API).

---

## 💰 PROJEÇÃO FINANCEIRA REALISTA

| Mês | Tráfego/mês | Vendas Amazon | Receita | Acumulado |
|---|---|---|---|---|
| 1 | 500 | 5–10 | R$ 100 | R$ 100 |
| 3 | 3.000 | 40–60 | R$ 800 | ~R$ 1.500 |
| 6 | 10.000 | 150–200 | R$ 3.000 | ~R$ 8.000 |
| 12 | 30.000 | 500–700 | R$ 10.000 | ~R$ 50.000 |
| 24 | 100.000+ | 1.500+ | R$ 30.000+ | ~R$ 250.000 |

**Modelo testado por afiliados sérios** (ex: Wirecutter, NerdWallet, Promobit). Não é fantasia — é math de SEO + afiliação.

---

## 📊 STACK CONSOLIDADA — CUSTOS MENSAIS

| Camada | Tool | Custo |
|---|---|---|
| Hospedagem site | Netlify | $0 (free tier suficiente) |
| Versionamento | GitHub | $0 (privado free) |
| Domínio (opcional) | Registro.br | R$ 40/ano |
| Email marketing | MailerLite Free | $0 (até 1k leads) |
| Agendamento social | Buffer Free | $0 (3 channels) |
| Auto-DM | ManyChat Free | $0 |
| Analytics | Plausible (alt) ou GA4 | $0 |
| AI Avatar (opcional) | HeyGen | $30/mês |
| **TOTAL essencial** | | **R$ 0** |
| **TOTAL com avatar** | | **R$ 150/mês** |

---

## 🎯 PRÓXIMOS 30 DIAS — Sprint Inicial

### Semana 1 (já iniciada)
- [x] Site no ar (`garimposp.netlify.app`)
- [x] Repo privado GitHub
- [x] Bio nova (texto pronto)
- [x] Estrutura `/blog/` no site
- [x] 1º artigo SEO completo (Mondial Air Fryer)
- [x] Captura de email (Netlify Forms)
- [x] GitHub Action de deploy automático
- [ ] Marcelo aplica bio + posta 3 posts (HOJE.md)

### Semana 2
- [ ] +4 artigos SEO (Anker Q11i, I2GO Power Bank, Guarda-chuva, Mochila antifurto)
- [ ] MailerLite setup + sequência de boas-vindas (5 emails)
- [ ] Pinterest: criar conta + 20 primeiros pins
- [ ] Submeter sitemap ao Google Search Console

### Semana 3
- [ ] +5 artigos SEO (templates por bairro: Vila Madalena, Pinheiros, Liberdade, Tatuapé, Brooklin)
- [ ] Buffer setup + 30 posts agendados
- [ ] WhatsApp Business + primeira lista

### Semana 4
- [ ] Análise: o que ranqueou? Quanto tráfego? Quais artigos converteram?
- [ ] Refinamento: dobra investimento no que funcionou
- [ ] +10 artigos da próxima onda

---

## 🎯 KPIs MENSAIS

| Métrica | Mês 1 | Mês 3 | Mês 6 |
|---|---|---|---|
| Artigos publicados | 5 | 30 | 60 |
| Tráfego orgânico/mês | 500 | 3.000 | 10.000 |
| Email subs | 50 | 300 | 1.000 |
| Vendas Amazon/mês | 10 | 60 | 200 |
| Comissão/mês | R$ 100 | R$ 800 | R$ 3.000 |

---

🔥 **Esse é o caminho de gente séria. Garimpo SP vira ativo digital de longo prazo.**

— Ultron · CEO Garimpo SP · 2026-05-08
