from pydantic import BaseModel

#Modelo de dados para representar request de operação matemática
class OperationRequest(BaseModel):
    a: float
    b: float

#Modelo de dados para representar response de operação matemática	
class OperationResponse(BaseModel):
    result: float
  