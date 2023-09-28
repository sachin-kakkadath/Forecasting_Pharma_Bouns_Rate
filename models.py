from pydantic import BaseModel

class pharmainput(BaseModel):
    quantity : int 
    dateofbill : str
    drugname : str
    