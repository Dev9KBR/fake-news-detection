import re
import unicodedata
from typing import Optional

def clean_text(text: Optional[str], remove_punct: bool = False) -> str:
    """
    Clean and normalize a text string.

    Steps performed:
    1. If text is None -> returns empty string.
    2. Normalize unicode (NFKC) to reduce equivalent codepoints.
    3. Remove URLs (http(s)://... and www....).
    4. Remove non-printable/control characters (Unicode category starting with 'C').
    5. Optionally remove punctuation (Unicode categories starting with 'P') if remove_punct=True.
    6. Convert to lower-case.
    7. Collapse consecutive whitespace to a single space and strip leading/trailing space.

    Args:
        text: Input text (str or anything convertible to str). If None returns "".
        remove_punct: If True, remove punctuation characters (.,!?;: and other Unicode punctuation).

    Returns:
        Cleaned string.

    Examples:
        >>> clean_text("Check this out: https://example.com!!!  \nNew line.")
        'check this out: new line.'
        >>> clean_text("BREAKING!!! Visit www.news.com NOW", remove_punct=True)
        'breaking visit now'
    """
    if text is None:
        return ""

    # ensure string and normalize unicode
    s = str(text)
    s = unicodedata.normalize("NFKC", s)

    # 1) remove URLs (http(s) and www)
    url_re = re.compile(r"https?://\S+|www\.\S+", flags=re.IGNORECASE)
    s = url_re.sub("", s)

    # 2) remove non-printable/control characters (Unicode category 'C*', e.g., Cc, Cf)
    s = "".join(ch for ch in s if not unicodedata.category(ch).startswith("C"))

    # 3) optionally remove punctuation (all Unicode punctuation categories 'P*')
    if remove_punct:
        s = "".join(ch for ch in s if not unicodedata.category(ch).startswith("P"))

    # 4) lowercase
    s = s.lower()

    # 5) collapse whitespace (spaces, tabs, newlines) to single space and trim
    s = re.sub(r"\s+", " ", s).strip()

    return s
