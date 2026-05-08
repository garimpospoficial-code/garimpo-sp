# ⛏️ Garimpo SP

> Negócio de afiliação Amazon Brasil com recorte em São Paulo. Conteúdo focado em achadinhos para apto pequeno, mobilidade urbana e cozinha esperta.

## 🎯 Tese

Pessoas que moram em SP têm dores específicas: apto pequeno, transporte cansativo, cozinha apertada, chuva imprevisível. O Garimpo SP recomenda produtos da Amazon que resolvem esses pontos, com identidade paulistana clara, e monetiza via comissão de afiliação (`tag=garimposp-20`).

## 📁 Estrutura

```
garimpo-sp/
├── site/              Landing page (deploy Netlify)
│   └── index.html
├── tools/             Painéis ao vivo (HTML standalone)
│   ├── hub-garimpo.html        Dashboard executivo
│   ├── garimpo-cockpit.html    Produção de conteúdo
│   └── jarvis-painel.html      Financeiro
├── content/           Assets visuais
│   ├── avatar/        Avatar do perfil
│   ├── posts/         6 posts feed Instagram (PNG 1080x1080)
│   ├── reels/         Capas de reels
│   └── carrossel/     5 slides do carrossel "5 receitas Air Fryer"
├── docs/              Estratégia e planos
│   ├── plano-primeira-venda-7-dias.md
│   ├── plano-divulgacao.md
│   ├── calendario-editorial-pipeline.md
│   ├── linktree-otimizacao.md
│   ├── produtos-extras.md
│   ├── dms-outreach.md
│   └── DEPLOY-NETLIFY.md
├── data/              Dados estruturados
│   └── warmachine-prospects.xlsx
└── scripts/           Automações Python/Bash
```

## 🛒 Catálogo Atual (7 produtos · tag=garimposp-20)

| Produto | ASIN | Preço | Comissão |
|---------|------|-------|----------|
| 🍳 Mondial Air Fryer 4L | B0BBQ3GBX1 | R$ 244 | 8% |
| 🎧 Anker Soundcore Q11i ANC | B0DJW5G283 | R$ 233 | 8% |
| 🎒 Mochila Antifurto USB | B0DVZBXSLK | ~R$ 149 | 11% |
| 🔋 I2GO Power Bank 20kmAh | B094YR4SLJ | R$ 169 | 8% |
| 👕 SONGMICS Guarda-Roupa | B09R4KQ2LY | R$ 273 | 8% |
| 🛡️ Capa Mochila Impermeável | B0CFKC1TRV | ~R$ 25 | 11% |
| ☂️ Guarda-chuva Anti-Vento | B0D1MMCMRP | R$ 37 | 11% |

## 🤖 Time (agentes)

| Agente | Responsabilidade | Status |
|--------|------------------|--------|
| **Ultron** | Orquestração / CEO digital | Ativo |
| **Vision** | Marketing & Conteúdo | Cockpit V2 rodando |
| **Jarvis** | Financeiro | Painel V1 rodando |
| **WarMachine** | Crescimento | 20 prospects mapeados |
| **Pepper** | Administrativo | Casa em ordem |

## 🌐 Plataformas Ativas

- **Instagram**: [@garimposp.oficial](https://www.instagram.com/garimposp.oficial)
- **TikTok**: [@garimposp.oficial](https://www.tiktok.com/@garimposp.oficial)
- **Linktree** (legado): linktr.ee/garimposp.oficial
- **Site próprio** (substituindo Linktree): a definir após deploy Netlify

## 💰 Afiliações Aprovadas

- **Amazon Associados**: `garimposp-20`
- **Mercado Livre Afiliados**: `gs20260501195956`
- **Shopee Afiliados**: aguardando ID

## 🚀 Próximas Frentes (semana atual)

1. ⚡ Deploy do `site/index.html` no Netlify
2. ⚡ Atualizar bio Instagram com URL nova
3. 📸 Postar 3 dos 6 posts prontos
4. 🎬 Gravar Reel A (Mondial Air Fryer review honesto)
5. 📨 Disparar 5 DMs outreach
6. 💰 Validar primeira venda (qualquer comissão Amazon entra no Jarvis)

## 📚 Como continuar via Claude Code

Veja `INIT.md` na raiz para os comandos iniciais (git init, push GitHub, etc).

## 🛡️ Compliance

- Disclosure de afiliação visível em todos os links públicos
- LGPD: site não captura dados de visitante (apenas localStorage local)
- Amazon Associates Operating Agreement: cumprido
