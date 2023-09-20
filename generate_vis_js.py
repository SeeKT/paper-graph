import json 
import argparse

def _read_from_json(path):
    """read from json file

    Args:
        path (str): the path of JSON file

    Returns:
        Dictionary: dict of JSON content
    """
    with open(path, 'r', encoding='utf-8') as f:
        d = json.load(f)
    return d

def _create_js(d, out, template):
    """Create JavaScript file

    Args:
        d (Dictionary): dict of paper
        out (str): the path of output JavaScript file
        template (str): the path of template JavaScript file
    """
    nodes, edges = _get_graph(d)
    nodes_str = 'var nodes = new vis.DataSet([\n'
    for node in nodes:
        nodes_str = nodes_str + str(node).replace('"', '') + ',\n'
    nodes_str = nodes_str + ']);\n'
    edges_str = 'var edges = new vis.DataSet([\n'
    for edge in edges:
        edges_str = edges_str + str(edge).replace('"', '') + ',\n'
    edges_str = edges_str + ']);\n'
    with open(template, 'r', encoding='utf-8') as f:
        others_subject = f.read()
    with open(out, mode='w', encoding='utf-8') as f:
        f.write(nodes_str)
        f.write(edges_str)
        f.write(others_subject)

def _get_graph(d):
    """get the information of graph

    Args:
        d (Dictionary): dict of paper

    Returns:
        List: the list of nodes information
        List: the list of edges information
    """
    nodes = []; edges = []
    for data in d:
        if data['status'] == 'read':
            node = "{id: " + str(data['id']) \
                + ", label: '" + str(data['id']) \
                    + "', group: '" + data['group'] \
                        + "', status: '" + data['status'] \
                            + "', shape: 'box', value: 20, scaling: { label: {enabled: true} }" \
                                + ", title: '" + data['title'] + "'" \
                                    + ", link: '" + data['link'] + "'" + '}'
        else:
            node = "{id: " + str(data['id']) \
                + ", label: '" + str(data['id']) \
                    + "', group: '" + data['group'] \
                        + "', status: '" + data['status'] \
                            + "', title: '" + data['title'] + "'" \
                                + ", link: '" + data['link'] + "'" + '}'
        nodes.append(node)
        for n in data['next']:
            edge= "{from: " + str(data['id']) \
                + ", to: " + str(n) \
                    + ", arrows: 'to'}"
            edges.append(edge)
    return nodes, edges

def parse_args():
    parser = argparse.ArgumentParser(
        description='generate JavaScript Code'
    )
    parser.add_argument('-l', '--list', help='JSON file (list of paper)', default='./list.json')
    parser.add_argument('-o', '--out', help='Output JavaScript File', default='./out/script.js')
    parser.add_argument('-t', '--template', help='Template JavaScript File', default='./template.js')
    return parser.parse_args()

def main():
    args = parse_args()
    d = _read_from_json(args.list)
    _create_js(d, args.out, args.template)
    
if __name__ == '__main__':
    main()