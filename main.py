from fastapi import FastAPI

from sum import operators, OperationRequest

app = FastAPI()


@app.post("/calculate")
async def calculate(data: OperationRequest):
    result = operators(data.operator)(data)
    return result.resultDict()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
