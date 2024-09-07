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

@app.get('/api/v1/elt/{video_id}')
def elt(video_id: str, db: Session = Depends(get_db), status_code=200):
    try:
        comments = extract_elt(video_id)
        transformed_comments = transform_elt(comments)
        load_elt(transformed_comments, db)
        return {'message': 'ELT pipleline was completed'}
    except Exception as error:
        raise HTTPException(status_code=403, detail=error)

