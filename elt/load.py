import database.models as models


def load_elt(comments, db):
    try:
        for row in comments.itertuples():
            db_query = models.Comments(
                author=row.author, author_image_url=row.author_image_url, content=row.content, date=row.date)
            db.add(db_query)

        db.commit()
    except Exception as error:
        raise Exception(f"Something went wrong with the loading the data. {error}")
