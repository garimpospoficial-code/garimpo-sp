---
name: esteira-garimpa
description: Esteira diária de produção de conteúdo Garimpa — gera 3 vídeos via Veo no Gemini Pro + agenda 3 Reels no Buffer. Trigger quando Marcelo digitar `/esteira-garimpa` (sem args), ou pedir "rodar esteira", "gerar vídeos da Garimpa", "esteira diária", "fazer 3 vídeos do dia".
---

# Esteira Garimpa — Produção Diária Automática

## Quando usar

- Usuário digita `/esteira-garimpa` ou variações ("rodar esteira", "gera 3 vídeos hoje", "esteira diária")
- Idealmente 1x por dia, depois das 15:49 (quando Veo rate limit reseta)

## O que faz

1. **Seleciona 3 cenários** do banco `docs/CENARIOS-VEO.md` que não foram usados nos últimos 14 dias, em **categorias diferentes**
2. **Gera 3 vídeos no Gemini Pro** via Chrome MCP (Veo)
3. **Baixa cada vídeo** pro `content/garimpa/videos/`
4. **Agenda 3 Reels no Buffer** com captions específicas
5. **Atualiza** `docs/CENARIOS-VEO.md` (tabela de uso)
6. **Commit + push** dos vídeos novos

## Pré-requisitos (checar antes)

- Chrome ativo + extensão Claude in Chrome conectada
- Gemini Pro web acessível (gemini.google.com — Marcelo logado)
- Buffer publish.buffer.com — Marcelo logado
- Queue Buffer com pelo menos 3 spots livres (Free plan: 10 total)
- Veo rate limit não atingido hoje

## Pipeline detalhada

### Passo 1: Selecionar 3 cenários

```
1. Read docs/CENARIOS-VEO.md — lista de 30 cenários (C01-C30)
2. Glob content/garimpa/videos/garimpa_*.mp4 — vídeos já existentes
3. Cross-reference com tabela "Métrica de uso" do MD
4. Selecionar 3 cenários:
   - 1 de categoria APTO/HOME (C01-C05)
   - 1 de categoria COZINHA/PRODUTO (C06-C10 ou C23-C27)
   - 1 de categoria MOBILIDADE/LIFESTYLE (C11-C22 ou C28-C30)
5. Skip cenários usados nos últimos 14 dias (verificar timestamp do .mp4)
```

### Passo 2: Gerar vídeos no Gemini Pro

Pra cada cenário selecionado (3x):

```
1. Navigate to https://gemini.google.com/app (ou continuar conversa "Geração de Vídeo Vertical Brasileiro" no histórico)
2. Click Ferramentas → Criar vídeo (se não estiver em modo vídeo já)
3. Click no campo "Insira um comando" (textbox)
4. Type o prompt completo (PERSONA-BASE + CENÁRIO + SETTINGS COMUNS — formato exato em docs/CENARIOS-VEO.md "Template do prompt final")
5. Click "Enviar mensagem" (button)
6. Aguardar render 60-120s (Veo demora) — verificar "Seu vídeo está pronto!" no chat
7. Hover na thumbnail → click no ícone de download (coords aprox 1184, 337 na conversa)
8. PowerShell mv: /c/Users/marce/Downloads/[video_*].mp4 → /c/Users/marce/Downloads/garimpo-sp/content/garimpa/videos/garimpa_<NOME-CENARIO>_v1.mp4
```

**Nomenclatura sugerida do arquivo:** `garimpa_<categoria>_<descricao>_v<numero>.mp4`
- Ex: `garimpa_cozinha_liquidificador_v1.mp4`, `garimpa_metro_anker_v1.mp4`

**Se bater rate limit Veo** (aviso "Você atingiu seu limite diário de criação. Tente de novo em X"):
- Parar geração
- Informar Marcelo: quantos vídeos foram baixados + horário pra retomar
- Salvar o que tem e seguir pra agendar

### Passo 3: Agendar Reels no Buffer

Pra cada vídeo gerado (até 3):

```
1. PowerShell SetFileDropList do .mp4 pro clipboard
2. Navigate to https://publish.buffer.com/channels/69ffc1e25c4c051afa2c0694/queue
3. Click "+ New Post" (coords aprox 1483, 150)
4. Click "Reel" radio (coords aprox 466, 158) — NÃO Post
5. Click área Drag&drop (coords aprox 630, 300)
6. Ctrl+V — vídeo cola
7. Aguardar 8s (upload)
8. Click campo de caption (coords aprox 630, 190)
9. Type caption (formato abaixo) — atenção: primeira linha sempre falha CDP timeout, workaround = Ctrl+Home + re-type primeira linha
10. Click "Schedule Post" (verde, canto inferior direito, coords aprox 1153, 677)
11. Verificar toast "Your post has been added to your queue."
```

**Template caption (adaptar por cenário):**

```
<frase de gancho com emoji do cenário>

<corpo descrevendo o produto/cena testada — 2-3 linhas>

<CTA: link da bio / pergunta / engagement>

— Garimpa 🤖
.
.
.
<5-7 hashtags relevantes>
```

**Hashtags-padrão sempre incluir:**
- `#garimposp #achadinhos #saopaulo`
- + específico do produto/cena

### Passo 4: Atualizar banco de cenários

```
1. Edit docs/CENARIOS-VEO.md — tabela "Métrica de uso" no fim
2. Para cada cenário usado, adicionar linha:
   | <CN> <Nome> | <YYYY-MM-DD> | ✅ Usado, agendado |
3. Commit: "feat(garimpa): esteira diária — 3 vídeos via Veo + agendados Buffer"
4. Push: git push origin main (passa pelo .claude/settings.json sem prompt)
```

## Comportamentos importantes

### Falhas conhecidas e workarounds

**Bug 1: Primeira linha do `type` no Buffer composer sempre falha** (CDP timeout)
- Workaround: depois do type completo, click no composer + Ctrl+Home + re-type só a primeira linha

**Bug 2: Veo às vezes ignora cenário específico** (ex: pediu metrô, renderizou varanda)
- Workaround: ser mais agressivo no prompt ("DENTRO de um vagão de metrô — NÃO rooftop, NÃO varanda")
- Se ainda errar, baixar mesmo assim (qualidade da imagem é alta) e re-categorizar arquivo

**Bug 3: Composer Buffer fecha após Schedule, próximo + New Post recria do zero**
- Esperado. Repetir flow completo pra cada Reel.

**Bug 4: Chrome download silencioso** (raro mas pode acontecer com Veo)
- Workaround: hover thumbnail, find element "Baixar imagem no tamanho original" via ref_XXX e click ref direto

### Ética e disclosure

- **TODA caption termina com "— Garimpa 🤖"** — disclosure mandatório
- Nunca afirmar que é pessoa real
- Manter tom "Garimpa": descolada paulistana, gírias contidas, honesta

## Recovery / interrupção

Se Marcelo interromper no meio:
- Salvar progresso (vídeos baixados ficam em `content/garimpa/videos/`)
- Reportar onde parou: "Gerei X de 3 vídeos, falta Y. Quer que eu retome?"
- NÃO duplicar geração de cenário já feito hoje

## Métricas de sucesso (reportar ao fim)

```
✅ Esteira do dia rodada
- 3 vídeos gerados via Veo (~5 min cada)
- 3 Reels agendados Buffer (próximos 3 slots disponíveis: 9h/13h/19h)
- Cenários usados: <C01>, <C06>, <C11>
- Próxima esteira: amanhã pós 15:49 (Veo rate limit reset)

Buffer queue: X/10
Próximo deploy automático: <horário>
```

## Trigger words

Ativar SEMPRE que ver:
- `/esteira-garimpa`
- "rodar esteira"
- "esteira diária"
- "gera 3 vídeos da Garimpa"
- "esteira hoje"
- "produção diária"
- "vídeos do dia"
