import sqlite3
import pandas as pd
DATABASE_URL = ("file:/data/CS403F26/databases/yelp.db?mode=ro")
def query(sql, parameters=None):
    with sqlite3.connect(DATABASE_URL, uri=True) as connection:
        return pd.read_sql_query(
            sql,
            connection,
            params=parameters,
        )

#how did reviews change from before and after 2008 (review count) keeping in mind phones, financial crisis, etc

#looked up how to do a cutoff date using sqlitetutorial.net, highly recomend checking it out for SQL

dataset = query("""
    SELECT
        b.business_id,
        r.date,
        r.stars AS review_stars
    FROM business AS b
    JOIN review AS r
        ON b.business_id = r.business_id
    WHERE r.date < 2012-01-01
    LIMIT 1000
""")

print(dataset)

#dataset.to_csv("data_yay.csv", index=False)

