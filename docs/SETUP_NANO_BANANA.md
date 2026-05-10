# 🍌 Setup Nano Banana (Imagen 3 + Veo 2)

> Geração automática de imagens e vídeos via Google Gemini API.

## ✅ Pré-requisitos

- Conta Google AI Studio (`aistudio.google.com`)
- Gemini API enabled
- Python 3.10+

## 🚀 Setup (5 min)

### 1. Pegar API Key

1. Vai em **https://aistudio.google.com/app/apikey**
2. Loga com Google
3. Clica **"Create API Key"**
4. Copia a key

### 2. Configurar .env

Na raiz do repo:

```bash
cp .env.example .env
```

Edita `.env` e cola a key:

```
GEMINI_API_KEY=AIzaSy...
```

⚠️ `.env` está no `.gitignore` — **nunca comita**.

### 3. Instalar dependências

```bash
pip install -r scripts/requirements.txt
```

## 📋 Uso dos scripts

### Gerar imagem de post

```bash
python scripts/gen_post_image.py --tema airfryer --output content/posts/post_novo.png
```

Temas disponíveis: `airfryer`, `chuva`, `mobilidade`, `apto`, `powerbank`, `fone`.

### Gerar Reel/vídeo (Veo 2)

```bash
python scripts/gen_reel_veo.py --tema airfryer --output content/reels/reel_novo.mp4
```

Temas disponíveis: `airfryer`, `fone`, `guardachuva`, `powerbank`.

⚠️ Veo 2 leva 1-3 min por geração + custa ~$0,50/8s. Use com critério.

### Gerar OG image pra artigo blog

```bash
python scripts/gen_og_image.py --titulo "Air Fryer apto pequeno SP" --output site/og-airfryer-novo.png
```

## 💰 Custos aproximados (Gemini API)

| Modelo | Preço |
|---|---|
| Imagen 3 (imagem 1024x1024) | $0.039/img |
| Veo 2 (vídeo 8s) | $0.40-0.50 |
| Gemini 2.0 Flash Image (edit) | $0.039/img |

**Free tier**: 60 RPM em modelos básicos. Imagen e Veo são paid (cobrado direto no Google Cloud).

## 🔥 Pipeline completo (futuro)

```
1. Gera 5 ideias de post via Claude API → catalog.json
2. Pra cada ideia:
   a. Gera imagem (Imagen 3)
   b. Gera caption (Claude)
   c. Sobe pro Buffer (API)
   d. Agenda
3. Pra cada produto-âncora:
   a. Gera Reel (Veo 2) 1x/semana
   b. Sobe pro Buffer (Reel slot)
4. Pra cada artigo blog novo:
   a. Gera OG image (Imagen 3)
   b. Adiciona meta tag og:image
   c. Deploy Netlify
```

Tudo automatizado. Tu não toca em foto/vídeo.
