import asyncio
from googletrans import Translator, LANGUAGES

class Languages:
    @staticmethod
    async def translate_text(text, dest='en', src='auto'):
        # always convert to list
        if isinstance(text, (list, tuple)):
            text_list = list(text)
        else:
            text_list = [text]

        async with Translator() as translator:
            results = await translator.translate(text_list, dest=dest, src=src)

        # googletrans sometimes returns a single object, sometimes a list
        if not isinstance(results, list):
            results = [results]

        # return a single string if only one input
        if len(text_list) == 1:
            return results[0].text

        return [r.text for r in results]
