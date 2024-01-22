const data = JSON.parse(document.getElementById("graph-data").textContent);
const sigma = new Sigma({
    container: document.getElementById("sigma-container"),
    data: {
        nodes: data.nodes,
        edges: data.edges
    },
    layout: "forceAtlas2",
    renderer: "canvas"
});