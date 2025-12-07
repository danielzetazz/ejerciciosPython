import json
import os
persona ={"nombre": "Daniel", "edad": 18, "ciudad": "Madrid"}

print(json.dumps(persona))
print(json.loads(json.dumps(persona)))

