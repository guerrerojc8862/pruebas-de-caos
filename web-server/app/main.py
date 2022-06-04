from datetime import datetime
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    now = datetime.now()
    data = {
            "datetime": now.strftime('%m/%d/%Y, %H:%M:%S'),
            "message": "Hello, World!",
            "region": "us-east-1",
            "availability-zone": "az",
            "instance-id": "iid",
            "instance-ip": "iip"
    }
    return data
