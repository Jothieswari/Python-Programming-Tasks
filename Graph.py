
def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

def make_graph(link_list):
    G = dict()
    for n1, n2 in link_list:
        make_link(G, n1, n2)
    return G
