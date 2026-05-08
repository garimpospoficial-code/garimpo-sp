# 🚀 Deploy Garimpo SP no Netlify (1 min, gratuito, sem cartão)

## Passo a passo

### 1. Acessa Netlify Drop (NÃO precisa criar conta antes)

Abre no Chrome: **https://app.netlify.com/drop**

### 2. Arrasta o arquivo `index.html`

Pega o arquivo:
**`C:\Users\marce\Downloads\garimpo-sp\index.html`**

E **arrasta solta na área cinza** que aparece na página da Netlify.

### 3. Aguarda 5 segundos

Netlify faz upload + deploy automaticamente. Vai gerar uma URL tipo:
**`https://random-name-12345.netlify.app`**

### 4. (Opcional) Cria conta pra renomear

Após o deploy, Netlify pede pra criar conta gratuita pra "salvar o site". Cria com email garimposp.oficial@gmail.com (Bitwarden gera senha).

Após login:
- Clica em **Site settings** → **Change site name**
- Renomeia pra `garimposp` (ou similar disponível)
- URL final fica: **`https://garimposp.netlify.app`** ✨

### 5. Atualiza bio do Instagram

Pelo celular: Instagram → Editar perfil → campo **Site** → cola:
```
https://garimposp.netlify.app
```

Pronto. **Bio do Instagram agora aponta pro NOSSO site, não pro Linktree.**

---

## ⚙️ Como ATUALIZAR depois

Quando você quiser adicionar/trocar produto:

1. Me peça aqui no chat ("adiciona X produto" / "tira o guarda-chuva" / "muda preço do Mondial")
2. Eu atualizo o `index.html`
3. **Você reabre `app.netlify.com/drop`** e arrasta o novo arquivo
4. Netlify atualiza em 5 segundos com a MESMA URL

OU (se criou conta):
1. Vai em `app.netlify.com` → seu site
2. Aba **Deploys** → arrastar arquivo novo no quadrado
3. Pronto

---

## 🎯 Vantagens desse setup vs Linktree

| | Linktree Free | Garimpo SP Site (este) |
|---|---|---|
| Custo | Grátis | Grátis |
| Domínio | linktr.ee/garimposp.oficial | garimposp.netlify.app |
| Tracking de clique | Básico (lifetime) | Por produto via `ascsubtag` Amazon |
| Customização visual | Limitada | Total |
| Velocidade de update | Cliques no painel | Eu mudo, você arrasta |
| Identidade Garimpo | Diluída | 100% |
| Deploy domínio próprio depois | Pago | Free no Netlify |

---

## 🔬 Como ver tracking de clique

**No relatório Amazon Associados** (associados.amazon.com.br):

Vai em **Reports** → **Tracking IDs Report**. Cada produto aqui no site gera um sub-tag único:
- `site_mondial` (Air Fryer)
- `site_anker` (Fone)
- `site_mochila` (Mochila Antifurto)
- `site_powerbank` (Power Bank)
- `site_armario` (SONGMICS)
- `site_capa` (Capa mochila)
- `site_guardachuva` (Guarda-chuva)

No relatório, vai aparecer **clique e venda por sub-tag**, então você sabe EXATAMENTE qual produto converteu.

**Localmente no site**: o navegador do visitante salva em localStorage quantos cliques deu em cada produto. Você abre `garimposp.netlify.app/?debug=1` no console e vê suas próprias estatísticas (não dá pra ver de outros visitantes — pra isso, próximo nível seria Plausible Analytics free).

---

## 🎨 Próximas evoluções (V2)

- 📊 **Plausible Analytics** (free 10k pageviews/mês) — analytics real de visitantes, não só Amazon
- 🌐 **Domínio próprio** — `garimposp.com.br` apontando pro Netlify (R$ 40/ano Registro.br)
- 🖼️ **Imagens reais dos produtos** — em vez de emoji, usar fotos da Amazon
- 🎯 **Página de produto individual** — `/produto/mondial` com mais detalhes pra quem quer ver mais antes de comprar
- 📧 **Captura de email** — "Cadastra pra receber 1 achadinho por semana"
- 🤖 **API Amazon** — atualizar preço automático

---

## 🆘 Troubleshooting

**"Netlify pediu pra criar conta antes do drop"**: cria com garimposp.oficial@gmail.com. Free, sem cartão.

**"Não sei onde tá o arquivo `index.html`"**: tá em `C:\Users\marce\Downloads\garimpo-sp\index.html`. Win+E pra abrir explorador, navega lá.

**"URL Netlify com nome aleatório me incomoda"**: faz o passo 4 (criar conta + renomear).

**"Quero usar garimposp.com.br"**: registra em registro.br, manda o domínio aqui que eu te passo a config DNS.

---

🔥 **5 minutos do teu lado, link público pronto, identidade 100% Garimpo, tracking real por produto.**
