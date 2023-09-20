var nodes = new vis.DataSet([
{id: 1, label: '1', group: 'Dataset Generation ICS', status: 'read', shape: 'box', value: 20, scaling: { label: {enabled: true} }, title: 'Anomaly Detection Dataset for Industrial Control Systems', link: 'https://arxiv.org/abs/2305.09678'},
{id: 2, label: '2', group: 'Dataset Generation ICS', status: 'unread', title: 'On the Generation of Anomaly Detection Datasets in Industrial Control Systems', link: 'https://ieeexplore.ieee.org/document/8926471'},
{id: 3, label: '3', group: 'ICS Testbed', status: 'unread', title: 'ICSSIM - A framework for building industrial control systems security testbeds', link: 'https://www.sciencedirect.com/science/article/pii/S0166361523000568'},
{id: 4, label: '4', group: 'ICS Testbed', status: 'read', shape: 'box', value: 20, scaling: { label: {enabled: true} }, title: 'SWaT: a water treatment testbed for research and training on ICS security', link: 'https://ieeexplore.ieee.org/document/7469060'},
]);
var edges = new vis.DataSet([
{from: 1, to: 2, arrows: 'to'},
{from: 1, to: 3, arrows: 'to'},
{from: 1, to: 4, arrows: 'to'},
]);
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