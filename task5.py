from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class WebhookData(BaseModel):
    function: str
    data: dict

function_registry = {}

def register_function(name: str):
    def decorator(func):
        function_registry[name] = func
        return func
    return decorator

@register_function('function1')
def function1(data):
    return f"Была вызывана функция function1 с данными: {data}"

@register_function('function2')
def function2(data):
    return f"Была вызывана функция function2 с данными: {data}"

@app.post("/Datalore")
async def handle_webhook(webhook: WebhookData):
    function_name = webhook.function
    data = webhook.data
    if function_name in function_registry:
        result = function_registry[function_name](data)
        return {"result": result}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
