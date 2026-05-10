"""
Gera imagens pra posts do Garimpo SP usando Gemini 2.5 Flash Image (Nano Banana).

Uso:
  python scripts/gen_post_image.py --tema airfryer --output content/posts/post_novo.png

Pré-requisitos:
  pip install google-genai pillow python-dotenv
  Configurar GEMINI_API_KEY em .env

API: https://ai.google.dev/gemini-api/docs/image-generation (modelo Nano Banana)
"""
import os
import sys
import argparse
from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

try:
    from google import genai
    from google.genai import types
    from PIL import Image
    from io import BytesIO
except ImportError as e:
    print(f"[ERRO] Falta dependencia: {e}")
    print("Instala: pip install google-genai pillow python-dotenv")
    sys.exit(1)


PROMPTS_BASE = {
    "airfryer": (
        "Mobile Instagram post 1080x1080 1:1 square format. "
        "Vibrant orange to amber gradient background. "
        "Top: bold white sans-serif Portuguese title 'AIR FRYER PRA APTO PEQUENO EM SP'. "
        "Center: clean illustration of a black Mondial 4L air fryer on white kitchen counter. "
        "Below: 5 bullet items in white text: "
        "1. Cabe na bancada (28cm), "
        "2. Esquenta em 3 minutos, "
        "3. Substitui forno em 80 porcento, "
        "4. 110V, "
        "5. R$ 244 frete gratis. "
        "Bottom right: small 'Garimpo SP' logo with pickaxe icon. "
        "Style: modern, clean, high contrast, professional Instagram aesthetic"
    ),
    "chuva": (
        "Mobile Instagram post 1080x1080 1:1 square. "
        "Deep blue to amber gradient. "
        "Top: bold white title '5 ACHADINHOS PRA SOBREVIVER A CHUVA EM SP'. "
        "Center: stylized illustration of black umbrella in rain with São Paulo skyline. "
        "Below: 5 items white text: 1. Guarda-chuva anti-vento, 2. Capa de mochila, "
        "3. Galocha, 4. Toalha microfibra, 5. Sapato impermeavel. "
        "Bottom right: 'Garimpo SP' logo. Modern professional design"
    ),
    "mobilidade": (
        "Instagram post 1080x1080 square. Orange-amber gradient. "
        "Title: '5 ACHADINHOS QUE SALVAM O TRANSPORTE EM SP'. "
        "Center: illustration of person in subway with backpack and headphones. "
        "List of 5: power bank, fone ANC, garrafa termica, capa de chuva, snack. "
        "Garimpo SP logo bottom. Professional"
    ),
    "apto": (
        "Instagram post 1080x1080 square. Orange gradient. "
        "Title: '5 HACKS PRA APTO ALUGADO EM SP'. "
        "Center: small modern Sao Paulo apartment interior, 38m2 layout, "
        "with portable wardrobe (SONGMICS), space-saving solutions. "
        "List of 5 hacks. Garimpo SP logo bottom"
    ),
    "powerbank": (
        "Instagram post 1080x1080 square. Tech blue to amber gradient. "
        "Title: 'CELULAR NAO MORRE MAIS EM SP'. "
        "Center: black power bank I2GO 20kmAh with USB-C cable connected to phone. "
        "Battery icon showing full charge. "
        "Tagline: '4-5 cargas - R$ 169 - frete gratis'. "
        "Garimpo SP logo bottom"
    ),
    "fone": (
        "Instagram post 1080x1080 square. Dark amber gradient. "
        "Title: 'METRO SP TEM SOLUCAO'. "
        "Center: black Anker Soundcore Q11i over-ear headphones. "
        "Sound waves visualization showing noise cancellation. "
        "Tagline: 'ANC - 60h bateria - R$ 233'. "
        "Garimpo SP logo bottom right"
    ),
}


def gen_image(tema: str, output_path: str) -> None:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("[ERRO] GEMINI_API_KEY nao configurada no .env")
        sys.exit(1)

    prompt = PROMPTS_BASE.get(tema)
    if not prompt:
        print(f"[ERRO] Tema '{tema}' nao conhecido. Disponiveis: {list(PROMPTS_BASE.keys())}")
        sys.exit(1)

    client = genai.Client(api_key=api_key)

    print(f"Gerando imagem '{tema}' via Gemini 2.5 Flash Image (Nano Banana)...")

    response = client.models.generate_content(
        model="gemini-2.5-flash-image",
        contents=[prompt],
    )

    img_saved = False
    for part in response.candidates[0].content.parts:
        if part.inline_data is not None:
            img = Image.open(BytesIO(part.inline_data.data))
            Path(output_path).parent.mkdir(parents=True, exist_ok=True)
            img.save(output_path)
            print(f"[OK] Imagem salva em {output_path} ({img.size})")
            img_saved = True
        elif part.text:
            print(f"[INFO] Texto retornado: {part.text[:100]}...")

    if not img_saved:
        print("[ERRO] Resposta nao continha imagem")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Gera imagem pra post Garimpo SP via Nano Banana")
    parser.add_argument("--tema", required=True, choices=list(PROMPTS_BASE.keys()))
    parser.add_argument("--output", required=True, help="Caminho do PNG de saida")
    args = parser.parse_args()
    gen_image(args.tema, args.output)


if __name__ == "__main__":
    main()
