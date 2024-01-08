import osmnx as ox
import matplotlib.pyplot as plt

# Search OpenStreetMap and create an OSMNx graph
G = ox.graph_from_place("Sevilla, Andalucía, España", network_type="drive")

# Plot the first graph
# ox.plot_graph(G) returns a tuple of two objects: the figure and the axes
fig, ax = ox.plot_graph(G)
plt.show()

# Our road network graph can be represented as two GeoDataFrames
# ox.graph_to_gdfs(G) returns a tuple of two GeoDataFrames
gdf_nodes, gdf_relationships = ox.graph_to_gdfs(G)
gdf_nodes.reset_index(inplace=True)
gdf_relationships.reset_index(inplace=True)

# Plot the nodes graph
gdf_nodes.plot(markersize=0.1)
plt.show()

# Plot the relationships graph
gdf_relationships.plot(markersize=0.01, linewidth=0.5)
plt.show()
