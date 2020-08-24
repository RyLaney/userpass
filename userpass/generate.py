"""Generate randome username and passwords
"""

# examples from https://docs.python.org/3/library/secrets.html

import string
import secrets

def token_urlsafe(nbytes=None):
    """generate urlsafe secret, a Base64 encoded string
    """
    return secrets.token_urlsafe(nbytes)

def alphanumeric(nbytes):
    """generate secret alpha numberic
    """
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for i in range(nbytes))

def passphrase(nwords):
    """xkcd style passphrase
    """
    with open('/usr/share/dict/words') as f:
        words = [word.strip() for word in f]
        return ' '.join(secrets.choice(words) for i in range(nwords))
