import os

from fastapi import FastAPI, APIRouter

from sum import operators, OperationRequest, registered_operators_as_enum

app = FastAPI()
router = APIRouter()


@router.post("/calculate")
def calculate(data: OperationRequest):
    result = operators(data.operator)(data)
    return result.resultDict()


@router.get("/operators")
def get_supported_operators():
    return dict(operators=sorted([i.value for i in registered_operators_as_enum()]))


app.include_router(router, prefix=os.getenv("APP_PREFIX", ""))

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
