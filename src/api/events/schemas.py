from pydantic import BaseModel,Field
from typing import List,Optional

# {'id':12}
class EventSchema(BaseModel):

    id:int




class EventListSchema(BaseModel):

    results:List[EventSchema]
    count: int


class EventUpdateSchema(BaseModel):
    id: int
    description: str = Field(...,min_length=1,max_length=40, description='Song Title')
    rating: Optional[float] = 0.0

