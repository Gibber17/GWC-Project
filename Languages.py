# before running this you must enter this in your terminal: pip install googletrans
import asyncio
from googletrans import Translator, LANGUAGES

# Print available languages
for lang_code, lang_name in LANGUAGES.items():
    print(f"{lang_code}: {lang_name}")

async def translate_text(text, dest='en', src='auto'):
    async with Translator() as translator:
        result = await translator.translate(text, dest=dest, src=src)
        print(f"Original ({result.src}): {text}")
        print(f"Translated ({result.dest}): {result.text}")
        return result.text


asyncio.run(translate_text("안녕하세요", dest='en'))
