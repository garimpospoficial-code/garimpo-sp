"""
Gera Open Graph images (1200x630) pros artigos do blog.
Quando alguém compartilha no WhatsApp/Telegram, aparece preview bonito.

Uso:
  python scripts/gen_og_image.py --titulo "Air Fryer apto pequeno SP" --output site/og-airfryer.png

Pré-requisitos:
  pip install google-genai pillow python-dotenv
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
    print(f"❌ Falta dependência: {e}")
    print("Instala: pip install google-genai pillow python-dotenv")
    sys.exit(1)


def gen_og(titulo: str, output_path: str) -> None:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("❌ GEMINI_API_KEY não configurada no .env")
        sys.exit(1)

    prompt = (
        f"Open Graph banner image (1200x630, 16:9), modern web design, "
        f"orange gradient background (#F59E0B to #D97706), "
        f"large bold white sans-serif title text in Portuguese: '{titulo}', "
        f"left-aligned, minimal layout, subtle product icon on the right, "
        f"Garimpo SP logo with pickaxe emoji bottom-right, "
        f"clean professional design, high contrast, social media share preview"
    )

    client = genai.Client(api_key=api_key)

    print(f"🎨 Gerando OG image '{titulo}'...")
    response = client.models.generate_images(
        model="imagen-3.0-generate-002",
        prompt=prompt,
        config=types.GenerateImagesConfig(
            number_of_images=1,
            aspect_ratio="16:9",
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
    print(f"✅ OG image salva em {output_path} ({img.size})")


def main():
    parser = argparse.ArgumentParser(description="Gera OG image pra artigo Garimpo SP")
    parser.add_argument("--titulo", required=True, help="Título do artigo")
    parser.add_argument("--output", required=True, help="Caminho do PNG de saída")
    args = parser.parse_args()
    gen_og(args.titulo, args.output)


if __name__ == "__main__":
    main()
