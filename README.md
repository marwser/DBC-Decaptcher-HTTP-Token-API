# DBC-Decaptcher-HTTP-Token-API
Use Decaptcher HTTP API to solve recaptcha v2 tokens by DeathByCaptcha service.

```python
from dbc_decaptcher import Decaptcher


cl = Decaptcher("username-here", "password-here")
    result = cl.solve_token(
        "http://skyrock.com", "6LcTyP4SAAAAADBjv0TABENKwCOGOFe5H15-hd_4")
    print(result)
```
