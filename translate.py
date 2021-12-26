from google_trans_new import google_translator
from textblob import TextBlob
def translate_uz(text):
    tarjimon = google_translator() # Translator bu maxsus klass (tarjimon esa obyekt)
    if TextBlob(text).detect_language()=="en":
        tarjima = tarjimon.translate(text,lang_tgt='uz',)
        a = "en-uz"
        return [tarjima,a]
    elif TextBlob(text).detect_language()=="uz" or TextBlob(text).detect_language() is None:
        tarjima = tarjimon.translate(text,lang_tgt='en',)
        a = "uz-en"
        return [tarjima,a]
    tarjima = tarjimon.translate(text,lang_tgt='en',lang_src="uz")
    return [tarjima,"uz-en"]
 