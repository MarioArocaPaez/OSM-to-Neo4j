from flask import Flask, render_template
from py2neo import Graph
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Set Neo4j connection details using environment variables
    NEO4J_URI = os.getenv("NEO4J_URI")
    NEO4J_USER = os.getenv("NEO4J_USER")
    NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

    # Create a Graph instance for Neo4j connection
    graph = Graph(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

    # Ejecuta una consulta de ejemplo (puedes personalizar según tus necesidades)
    cypher_query = '''
        MATCH (n)-[r]->(m)
        RETURN n, r, m
        LIMIT 25
    '''

    result = graph.run(cypher_query).data()

    # Convierte el resultado de la consulta a JSON
    nodes = []
    links = []

    for record in result:
        nodes.append({'id': record['n'].id, 'label': record['n'].labels, 'properties': record['n'].properties})
        nodes.append({'id': record['m'].id, 'label': record['m'].labels, 'properties': record['m'].properties})
        links.append({'source': record['n'].id, 'target': record['m'].id, 'type': record['r'].type, 'properties': record['r'].properties})

    return render_template('index.html', nodes=nodes, links=links)

if __name__ == '__main__':
    app.run(debug=True)
