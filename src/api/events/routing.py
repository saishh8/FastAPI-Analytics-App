from fastapi import APIRouter,Depends, HTTPException
from .models import EventModel,EventListModel,EventUpdateModel,EventCreateModel
from sqlmodel import Session,select
from ..db.config import DATABASE_URL
from src.api.db.session import get_session

router = APIRouter()


# get data
@router.get("/",response_model=EventListModel)
async def read_events(session:Session = Depends(get_session)):
    
    query = select(EventModel)
    results = session.exec(query).all()
    return{
        "results": results,
        "count":len(results)
    }



# create data
@router.post("/",response_model=EventModel)
async def create_event(data:EventCreateModel,
                        session:Session = Depends(get_session)):
  
    # a bunch of items in the table
    obj = EventModel.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj
   

#get data with a reference
@router.get("/{event_id}",response_model=EventModel)
async def get_event(event_id: int, session:Session = Depends(get_session)):

    obj = session.get(EventModel,event_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Event not found")
    return obj

#update data with a reference
@router.put("/{event_id}",response_model=EventModel)
async def update_event(event_id: int, data: EventUpdateModel, session:Session = Depends(get_session)):


    obj = session.get(EventModel, event_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Event not found")

    print(f"Before Updation - Description = {obj.description}, Rating = {obj.rating}")
   
    
    update_data = data.model_dump(exclude_unset=True)
    for key,val in update_data.items():
        setattr(obj,key,val)

    session.add(obj)
    session.commit()
    session.refresh(obj)


    
    print(f"After Updation - Description = {obj.description}, Rating = {obj.rating}")
    return obj