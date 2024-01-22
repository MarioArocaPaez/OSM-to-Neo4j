import json
import neo4j
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

# Retrieve Neo4j graph data
with driver.session() as session:
    nodes = []
    edges = []

    # Iterate over nodes
    for node in session.run("MATCH (n) RETURN n"):
        nodes.append({
            "id": node["n"]["osmid"],
            "label": node["n"]["ref"]
        })

    # Iterate over edges
    for edge in session.run("MATCH (u)-[r:ROAD_SEGMENT]->(v) RETURN u, r, v"):
        edges.append({
            "source": edge["u"]["osmid"],
            "target": edge["v"]["osmid"],
            "label": edge["r"]["name"]
        })

# Export graph data to JSON
with open("graph.json", "w") as f:
    json.dump({"nodes": nodes, "edges": edges}, f)

# Close the driver
driver.close()