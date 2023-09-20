var container = document.getElementById("network");
var data = {
    nodes: nodes,
    edges: edges
};
var options = {
};
var network = new vis.Network(container, data, options);

network.on("click",function(params){
    var nodeId = params["nodes"][0];
    if(nodeId == null){
        return;
    }
    var param = nodes.get(nodeId);
    console.log(param)
    document.getElementById("title").innerHTML = "Paper: " + "<a href=" + param["link"] + ">" + param["title"] + "</a>";
    document.getElementById("group").innerHTML = "Group: " + param["group"];
    document.getElementById("status").innerHTML = "Status: " + param["status"];
});