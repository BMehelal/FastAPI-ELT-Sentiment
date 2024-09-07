from typing import Annotated
from fastapi import FastAPI, HTTPException, Depends
from database.database import engine, get_db
from elt.extract import extract_elt
from elt.load import load_elt
import database.models as models
from elt.transform import transform_elt
from sqlalchemy.orm import Session 


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# extract, transform, load
# make sure to get the video id
@app.get('/api/v1/elt/{video_id}')
def elt(video_id: str, db: Session = Depends(get_db)):
    try:
        comments = extract_elt(video_id)
        transformed_comments = transform_elt(comments)
        load_elt(transformed_comments, db)
        return {'message':1}
    except Exception as e:
        print(e)


# elt("f-t01niuCKE")
