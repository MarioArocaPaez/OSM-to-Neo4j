import neo4j
import osmnx as ox
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Neo4j connection details
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USER = os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

# Create a Neo4j driver
driver = neo4j.GraphDatabase.driver(NEO4J_URI.strip(), auth=(NEO4J_USER, NEO4J_PASSWORD))

# Neo4j query
neo4j_query = '''
    MATCH path=shortestPath((startNode)-[:ROAD_SEGMENT*]->(endNode))
    WHERE ID(startNode) = 636 AND ID(endNode) = 10660
    RETURN path, [rel IN relationships(path) | rel.name] AS edgeNames
'''

with driver.session() as session:
    neo4j_result = session.run(neo4j_query).single()

# Extract path and edge names from Neo4j result
path = neo4j_result['path']
edge_names = neo4j_result['edgeNames']

# Search OpenStreetMap and create an OSMNx graph
G = ox.graph_from_place("Sevilla, Andalucía, España", network_type="drive")

# Plot the graph
fig, ax = ox.plot_graph(G, show=False, close=False)

# Plot the path with edge names
ox.plot_graph_route(G, [node['osmid'] for node in path.nodes], route_color='r', route_linewidth=6, route_alpha=0.5, ax=ax, route_linestyle='dashed')

# Highlight nodes in the path
ox.plot_graph(G, ax=ax, show=False, close=False, edge_color='k', node_color='k', node_size=0)

# Highlight edges in the path
for u, v in zip(path.nodes[:-1], path.nodes[1:]):
    edge = G.get_edge_data(u, v)
    edge_color = 'r' if edge and edge['name'] in edge_names else 'k'
    ox.plot_graph_route(G, route=[u, v], route_color=edge_color, route_linewidth=6, route_alpha=0.5, ax=ax, route_linestyle='dashed')

plt.show()
