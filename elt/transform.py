import pandas as pd


def transform_elt(comments):
    comments_df = pd.json_normalize(comments, sep='.')

    
    columns_to_extract = ['snippet.topLevelComment.snippet.authorDisplayName',
                          'snippet.topLevelComment.snippet.authorProfileImageUrl', 'snippet.topLevelComment.snippet.textDisplay',
                          'snippet.topLevelComment.snippet.publishedAt']
    extracted_df = comments_df[columns_to_extract]

    extracted_df = extracted_df.rename(columns={
        'snippet.topLevelComment.snippet.authorDisplayName': 'author',
        'snippet.topLevelComment.snippet.authorProfileImageUrl': 'author_image_url',
        'snippet.topLevelComment.snippet.textDisplay': 'content',
        'snippet.topLevelComment.snippet.publishedAt': 'date'
    })

    # Format the date
    extracted_df['date'] = pd.to_datetime(extracted_df['date']).dt.strftime('%m-%d-%Y')
    
    # Removes any links from the comments
    extracted_df = extracted_df[~extracted_df['content'].str.contains(
        "<a href", case=False, na=False)]

    return extracted_df
