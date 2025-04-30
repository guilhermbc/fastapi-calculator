from fastapi import FastAPI, HTTPException
from app.models import OperationRequest, OperationResponse
from app.operations import add, subtract, multiply, divide

app = FastAPI(
    title="FastAPI Calculator",
    description="Calculadora Simples feita com FastAPI.",
    version="1.0.0"
)

@app.post("/add", response_model=OperationResponse, summary="Adição", description="Soma dois números.")
def add_numbers(request: OperationRequest):
    result = add(request.a, request.b)
    return OperationResponse(result=result)

@app.post("/subtract", response_model=OperationResponse, summary="Subtração", description="Subtrai dois números.")
def subtract_numbers(request: OperationRequest):
    result = subtract(request.a, request.b)
    return OperationResponse(result=result)

@app.post("/multiply", response_model=OperationResponse, summary="Multiplicação", description="Multiplica dois números.")
def multiply_numbers(request: OperationRequest):
    result = multiply(request.a, request.b)
    return OperationResponse(result=result)

@app.post("/divide", response_model=OperationResponse, summary="Divisão", description="Divide dois números.")
def divide_numbers(request: OperationRequest):
    try:
        result = divide(request.a, request.b)
        return OperationResponse(result=result)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))