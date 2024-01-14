# Route Reina Mercedes to Pino Montano
'''
    MATCH path=shortestPath((startNode)-[:ROAD_SEGMENT*]->(endNode))
    WHERE ID(startNode) = 636 AND ID(endNode) = 10660
    RETURN path, [rel IN relationships(path) | rel.name] AS edgeNames
'''

# Route Santa Justa to la Alameda
'''
MATCH path=shortestPath((startNode)-[edges:ROAD_SEGMENT*]->(endNode))
WHERE ID(startNode) = 653 AND ID(endNode) = 692
RETURN path, [rel IN relationships(path) | rel.name] AS edgeNames
'''

# Nodes intersecting with Avenida de la Reina Mercedes
'''
MATCH (node)-[:ROAD_SEGMENT {name: 'Avenida de la Reina Mercedes'}]->()
RETURN node
'''