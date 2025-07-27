# language.py

from en import STRINGS as ENGLISH
from hi import STRINGS as HINDI
from te import STRINGS as TELUGU

# Default language
DEFAULT_LANGUAGE = "en"

# Supported language codes
SUPPORTED_LANGUAGES = {
    "en": ENGLISH,
    "hi": HINDI,
    "te": TELUGU
}

def get_strings(lang_code: str):
    return SUPPORTED_LANGUAGES.get(lang_code, ENGLISH)
