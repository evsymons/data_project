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

#Prior to 2008, how well did businesses perform?*
#*This question will expand, we will later compare to after 2008.

#looked up how to do a cutoff date using sqlitetutorial.net, highly recomend checking it out for SQL

dataset = query("""
    SELECT
        b.business_id,
        r.date,
        b.stars AS business_stars,
        r.stars AS review_stars
    FROM business AS b
    JOIN review AS r
        ON b.business_id = r.business_id
    WHERE
        r.data BETWEEN '2004-01-01' and "2012-01-01"
    LIMIT 10
""")


#before_business = query("""
 #   SELECT
  #      b.business_id,
   #     r.date,
    #    b.stars AS business_stars
    #FROM business AS b
    #JOIN review AS r
    #    ON b.business_id = r.business_id
    #WHERE r.date < '2008-01-01'
    #IMIT 10
#""")

#after business = query("""
 #   SELECT
  #      b.business_id,
   #     r.date,
    #    b.stars AS business_stars
#    FROM business AS b
 #   JOIN review AS r
  #      ON b.business_id = r.business_id
   # WHERE 
    #    r.date BETWEEN '2008-01-01' and '2012-01-01'
    #LIMIT 10
#""")


dataset.to_csv("data_yay1.csv", index=False)
#before_business.to_csv("data_before2008.csv", index = True)

