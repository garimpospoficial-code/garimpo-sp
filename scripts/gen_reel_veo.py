"""
Gera vídeos curtos (5-8s) pra Reels do Garimpo SP usando Veo 2.

Uso:
  python scripts/gen_reel_veo.py --tema airfryer --output content/reels/reel_novo.mp4

Pré-requisitos:
  pip install google-genai python-dotenv
  Configurar GEMINI_API_KEY em .env (com Veo 2 access — Gemini API paid tier)

API: https://ai.google.dev/gemini-api/docs/video
"""
import os
import sys
import time
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
except ImportError as e:
    print(f"❌ Falta dependência: {e}")
    print("Instala: pip install google-genai python-dotenv")
    sys.exit(1)


PROMPTS_VIDEO = {
    "airfryer": (
        "8-second cinematic vertical (9:16) reel for Instagram. "
        "Modern São Paulo apartment kitchen, small countertop. "
        "Hands placing frozen chicken pieces in a Mondial Air Fryer 4L. "
        "Time-lapse of chicken cooking through the transparent window. "
        "Final shot: golden crispy chicken, steam rising. "
        "Warm orange/amber color grading. "
        "Text overlay (Portuguese): 'AIR FRYER MUDOU MEU JOGO EM SP'. "
        "End frame: 'Mondial 4L · R$ 244 · link na bio'. "
        "Cinematic, professional, Instagram Reel style"
    ),
    "fone": (
        "8-second vertical (9:16) reel. "
        "POV shot inside São Paulo subway car, packed with people. "
        "Person putting on Anker Q11i black over-ear headphones. "
        "Background noise visualization fades to silence as ANC activates. "
        "Phone screen showing music playing. "
        "Text overlay: 'ANC SILENCIA O METRÔ SP'. "
        "End: 'Anker Q11i · R$ 233 · link na bio'. "
        "Cinematic, professional"
    ),
    "guardachuva": (
        "5-second vertical (9:16) reel. "
        "São Paulo Avenida Paulista, heavy rain pouring, strong wind. "
        "Person opening a black anti-wind umbrella with automatic mechanism. "
        "Wind hitting the umbrella, hastes flexing but not turning inside out. "
        "Person walking confidently in the rain. "
        "Text overlay: 'R$ 37 · AGUENTA TEMPORAL SP'. "
        "Dramatic lighting, cinematic"
    ),
    "powerbank": (
        "6-second vertical (9:16) reel. "
        "São Paulo street, busy morning commute. "
        "Phone showing 5% battery, then power bank I2GO 20kmAh connected. "
        "Battery icon filling up rapidly via USB-C cable. "
        "Person continues walking with phone now charging. "
        "Text overlay: '14H FORA DE CASA · I2GO 20K · R$ 169'. "
        "Modern, minimalist style"
    ),
}


def gen_video(tema: str, output_path: str) -> None:
    """Gera vídeo usando Veo 2."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("❌ GEMINI_API_KEY não configurada no .env")
        sys.exit(1)

    prompt = PROMPTS_VIDEO.get(tema)
    if not prompt:
        print(f"❌ Tema '{tema}' não conhecido. Disponíveis: {list(PROMPTS_VIDEO.keys())}")
        sys.exit(1)

    client = genai.Client(api_key=api_key)

    print(f"🎬 Gerando vídeo '{tema}' (pode levar 1-3 minutos)...")
    operation = client.models.generate_videos(
        model="veo-2.0-generate-001",
        prompt=prompt,
        config=types.GenerateVideosConfig(
            aspect_ratio="9:16",
            number_of_videos=1,
            duration_seconds=8,
            person_generation="dont_allow",  # cuidado com conteúdo de pessoa
        ),
    )

    while not operation.done:
        print("  ⏳ Processando...")
        time.sleep(10)
        operation = client.operations.get(operation)

    if not operation.response.generated_videos:
        print("❌ Geração retornou vazio")
        sys.exit(1)

    video = operation.response.generated_videos[0].video
    video_bytes = client.files.download(file=video)

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "wb") as f:
        f.write(video_bytes)

    print(f"✅ Vídeo salvo em {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Gera vídeo Reel pra Garimpo SP via Veo 2")
    parser.add_argument("--tema", required=True, choices=list(PROMPTS_VIDEO.keys()),
                        help="Tema do vídeo")
    parser.add_argument("--output", required=True, help="Caminho do arquivo MP4 de saída")
    args = parser.parse_args()
    gen_video(args.tema, args.output)


if __name__ == "__main__":
    main()
