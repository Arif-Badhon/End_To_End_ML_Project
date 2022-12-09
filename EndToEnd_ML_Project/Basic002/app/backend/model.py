from typing import Optional
from pydantic import BaseModel

class prediction(BaseModel):
    CRIM : float
    ZN : float
    INDUS : float
    CHAS : float
    NOX : float
    RM : float
    AGE : float
    DIS : float
    RAD : float
    TAX : float
    PTRATIO : float
    B : float
    LSTAT : float