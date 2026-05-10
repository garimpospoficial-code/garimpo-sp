# 🍌 Receita Nano Banana via App Gemini Pro (sem billing API)

> Pipeline validada em 2026-05-10. Funciona 100% com conta Premium do app Gemini, sem precisar billing Google Cloud.

## ✅ O que destrava

- **App Gemini Pro** (gemini.google.com) com subscription Premium → permite Nano Banana 2 (modelo de imagem) sem cobrança extra
- **Claude in Chrome MCP** automatiza o app: manda prompt, aguarda imagem, baixa
- **Trick canvas + dataURL** captura imagem (blob URL) sem CORS issue
- **PowerShell** move arquivo do Downloads pro projeto

## 🎯 Pipeline (já testada)

```
1. Eu navego pra gemini.google.com
2. Eu digito prompt no campo
3. Eu pressiono Enter
4. Gemini gera imagem (15-30s)
5. Eu uso JS canvas pra capturar PNG
6. Eu disparo download
7. PowerShell move pra content/
8. Subo no Buffer manual ou via clipboard
```

## 🔑 Tipos de prompt que FUNCIONAM bem

### ✅ Fotografia de produto / lifestyle
**Funciona muito bem**. Nano Banana é treinado em fotos.

Exemplo bem-sucedido:
```
Crie uma fotografia profissional de produto, formato quadrado 1080x1080.
Air Fryer Mondial 4L preta sobre bancada de mármore branco em cozinha de
apartamento moderno em São Paulo. Janela ao fundo desfocada mostrando
edifícios da cidade ao entardecer. Iluminação suave dourada vinda da janela.
Air Fryer com a porta aberta, fritas crocantes douradas dentro, vapor sutil
saindo. Estilo: fotografia comercial premium, estética clean, foco perfeito
no produto. Sem texto, sem logo. Apenas a foto.
```

### ⚠️ Posts com texto estruturado (lista, título, etc)
**Funciona mal**. Nano Banana NÃO é design tool — ignora layout estruturado e gera "vibe".

Pra POSTS com texto: use Canva (template) ou Figma.

### ✅ Lifestyle/atmosfera SP
**Funciona bem**. Pessoa, cenário, ambiente.

```
Crie uma foto de lifestyle paulistano, mulher jovem em rooftop ao pôr do sol,
skyline de SP ao fundo, vibe descolada, óculos de sol, smartphone na mão,
formato 1080x1080.
```

## 📋 Templates prontos pro Garimpo SP

### Template 1: Foto de produto (Air Fryer)
```
Foto comercial: [PRODUTO] sobre bancada [SUPERFÍCIE], janela ao fundo
mostrando [CIDADE/AMBIENTE], iluminação [TIPO], formato 1080x1080,
sem texto.
```

### Template 2: Lifestyle paulistano
```
Pessoa [GÊNERO/IDADE] em [LOCAL SP], usando [PRODUTO], ambiente urbano,
hora dourada, formato 9:16 vertical pra Reel.
```

### Template 3: Background pra Story
```
Background abstrato laranja amber com elementos paulistanos sutis,
formato 9:16, sem texto, espaço pra overlay de texto.
```

## 🚀 Próximos passos

1. **Gerar 5-10 fotos de produto** (Air Fryer, Anker, Power Bank, etc) usando Template 1
2. **Subir como POSTS no Buffer** (substitui PNGs com texto que estavam no `/content/posts/`)
3. **Gerar fotos de lifestyle** pra usar como backgrounds de Stories
4. **Repetir 1x/semana** pra ter conteúdo fresh sempre

## ⚠️ Limites do app Gemini Premium

- **~5 imagens/hora** (rate limit não documentado mas observado)
- **1024×1024 fixo** (não dá pra customizar resolução)
- **Quality varia** por geração — às vezes precisa rodar prompt 2-3x
- **Sem texto estruturado complexo** (use Canva pra isso)
