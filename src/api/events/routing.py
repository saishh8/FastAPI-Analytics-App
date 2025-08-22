from fastapi import APIRouter
from .schemas import EventSchema,EventListSchema,EventUpdateSchema
router = APIRouter()


# get data
@router.get("/")
async def read_events()-> EventListSchema:
    return{
        "results": [{"id":1},{"id":2},{"id":3}],
        "count":3
    }



# create data
@router.post("/")
async def create_event(data:dict={})-> EventSchema:

    # a bunch of items in the table
    print(data)
    print(type(data))
    return {"id":123}
   

#get data with a reference
@router.get("/{event_id}")
async def get_event(event_id: int) -> EventSchema:
    return {"id":event_id}

#update data with a reference
@router.put("/{event_id}")
async def update_event(event_id: int, data: EventUpdateSchema) -> EventUpdateSchema:

    description = 'Zephyr Song'
    rating = 9.0
    print(f'Before Updation - Description = {description}, Rating = {rating}')
   
    print(data)

    #pydantic approach
    description = data.description
    rating = data.rating

    #to dict approach
    # data = data.model_dump()
    # description = data['description']
    # rating = data['rating']
    print(f'After Updation - Description = {description}, Rating = {rating}')
    return {"id":event_id,"description":description,"rating":rating}
