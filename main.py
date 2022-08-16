from fastapi import FastAPI
from uuid import UUID
from math import floor

app = FastAPI()

def is_valid_uuid(uuid_to_test, version=4):
    try:
        uuid_obj = UUID(uuid_to_test, version=version)
    except ValueError:
        return False
    return str(uuid_obj) == uuid_to_test

@app.get("/")
def read_root():
    return "Nothing to see here, i mean..."

@app.get("/ping")
def read_item(uuid: str):
    if not is_valid_uuid(uuid): return "uuid_wrong"
    else:
      out = open("pings/"+uuid+".dat").write(str(math.floor(time.time())))
      out.close()
      return "ok"
