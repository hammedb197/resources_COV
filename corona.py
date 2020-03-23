from neo4j import GraphDatabase


query = '''LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-20-2020.csv' AS row 
            with row
            MERGE(c:Country {country: row['Country/Region']})
            MERGE(c)-[:affected_state]->(s:State {state: coalesce(row["Province/State"], "Unknown")})
            MERGE(s)-[:confirmed]->(co:Confirmed {number_of_confirmed_case: row['Confirmed']})
            MERGE(s)-[:death_cases]->(d:Death {number_of_recorded_death: row['Deaths']})
            MERGE(s)-[:recovered]->(r:Recovered {number_of_recovered_cases : row['Recovered']})
            MERGE (r)-[:LAST_UPDATED]->(:LastUpdate {last_updated: row['Last Update']})<-[:LAST_UPDATED]-(d)
            MERGE (r)-[:LAST_UPDATED]->(:LastUpdate {last_updated: row['Last Update']})<-[:LAST_UPDATED]-(co)
            '''

def sendToNeo4j():
    print("saving to db")
    driver = GraphDatabase.driver('bolt://localhost:7687', auth=('neo4j', 'graph'))
    db = driver.session()
    consumer = db.run(query).consume()
    print("data saved")



sendToNeo4j()
