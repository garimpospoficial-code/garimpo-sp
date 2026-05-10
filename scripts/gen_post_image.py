"""
Gera imagens pra posts do Garimpo SP usando Gemini Imagen 3.

Uso:
  python scripts/gen_post_image.py --produto airfryer --tema chuva --output content/posts/post_novo.png

Pré-requisitos:
  pip install google-generativeai pillow python-dotenv
  Configurar GEMINI_API_KEY em .env

API: https://ai.google.dev/gemini-api/docs/image-generation
"""
import os
import sys
import argparse
from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # python-dotenv opcional

try:
    from google import genai
    from google.genai import types
    from PIL import Image
    from io import BytesIO
except ImportError as e:
    print(f"❌ Falta dependência: {e}")
    print("Instala: pip install google-genai pillow python-dotenv")
    sys.exit(1)


PROMPTS_BASE = {
    "airfryer": (
        "Mobile Instagram post in Portuguese for paulistano audience. "
        "Title: '5 ACHADINHOS PRA COZINHA EM SP'. "
        "Vibrant orange gradient background (#F59E0B to #D97706), "
        "white modern bold sans-serif text, list of 5 items, "
        "1:1 square 1080x1080, kitchen icon top-right, "
        "logo 'Garimpo SP' bottom-right with pickaxe emoji, "
        "professional design, high contrast"
    ),
    "chuva": (
        "Mobile Instagram post in Portuguese for paulistano audience. "
        "Title: '5 ACHADINHOS PRA SOBREVIVER À CHUVA EM SP'. "
        "Vibrant orange gradient background (#F59E0B to #D97706), "
        "white modern bold sans-serif text, list of 5 rain-survival items, "
        "1:1 square 1080x1080, umbrella icon top-right, "
        "logo 'Garimpo SP' bottom-right, professional design"
    ),
    "mobilidade": (
        "Mobile Instagram post in Portuguese for paulistano audience. "
        "Title: '5 ACHADINHOS QUE SALVAM O TRANSPORTE EM SP'. "
        "Orange gradient background, white modern bold text, "
        "list of 5 commute items (headphones, power bank, mochila), "
        "1:1 square 1080x1080, subway icon, Garimpo SP logo bottom"
    ),
    "apto": (
        "Mobile Instagram post in Portuguese for paulistano audience. "
        "Title: '5 ACHADINHOS PRA APTO PEQUENO DE SP'. "
        "Orange gradient background, white modern bold text, "
        "list of 5 small-apartment items, 1:1 square 1080x1080, "
        "apartment icon, Garimpo SP logo bottom"
    ),
    "powerbank": (
        "Mobile Instagram post in Portuguese. "
        "Title: 'CELULAR NÃO MORRE MAIS EM SP'. "
        "Orange gradient, white bold text, "
        "I2GO power bank product photo center, "
        "1:1 square, '4-5 cargas · R$ 169' tagline, Garimpo SP logo"
    ),
    "fone": (
        "Mobile Instagram post in Portuguese. "
        "Title: 'METRÔ SP TEM SOLUÇÃO'. "
        "Orange gradient, white bold text, "
        "Anker Q11i headphones product photo, "
        "ANC active noise cancellation visualization, '60h bateria · R$ 233', "
        "Garimpo SP logo bottom"
    ),
}


def gen_image(tema: str, output_path: str) -> None:
    """Gera imagem usando Gemini Imagen."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("❌ GEMINI_API_KEY não configurada no .env")
        sys.exit(1)

    prompt = PROMPTS_BASE.get(tema)
    if not prompt:
        print(f"❌ Tema '{tema}' não conhecido. Disponíveis: {list(PROMPTS_BASE.keys())}")
        sys.exit(1)

    client = genai.Client(api_key=api_key)

    print(f"🎨 Gerando imagem '{tema}'...")
    response = client.models.generate_images(
        model="imagen-3.0-generate-002",
        prompt=prompt,
        config=types.GenerateImagesConfig(
            number_of_images=1,
            aspect_ratio="1:1",
            output_mime_type="image/png",
        ),
    )

    if not response.generated_images:
        print("❌ Geração retornou vazio")
        sys.exit(1)

    img_bytes = response.generated_images[0].image.image_bytes
    img = Image.open(BytesIO(img_bytes))

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    img.save(output_path)

    print(f"✅ Imagem salva em {output_path} ({img.size})")


def main():
    parser = argparse.ArgumentParser(description="Gera imagem pra post Garimpo SP")
    parser.add_argument("--tema", required=True, choices=list(PROMPTS_BASE.keys()),
                        help="Tema da imagem")
    parser.add_argument("--output", required=True, help="Caminho do arquivo PNG de saída")
    args = parser.parse_args()
    gen_image(args.tema, args.output)


if __name__ == "__main__":
    main()
