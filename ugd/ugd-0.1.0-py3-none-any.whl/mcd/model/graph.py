
from ugd.model.node import Node

'''
The baisic Graph contains the information on the degrees and edges, 
The RstGraph contains in addition information on the restrictions (here, the number of arrows between node groups, or node partitions) 
'''

class Graph():
    # Graph class ( Constructed fot CPP implementation)
    # the Graph has n nodes {0,..,n-1}, the Node n is looked at and treated as NONE (such that in C implementation working with primitive types is possible)
    def __init__(self,  degree_serie):
        self.is_directed = False
        self.degree_serie = degree_serie
        self.node_number = degree_serie.__len__()
        self.nodes = []
        for i in range(degree_serie.__len__()):
            self.nodes.append(Node(i, degree_serie[i], self.node_number))

    # CCC
    def add_edge(self, edge):
        from_id, to_id = edge
        from_node = self.nodes[from_id]
        from_node.add_outedge(to_id)
        from_node.del_passive_outedge(to_id)
        to_node = self.nodes[to_id]
        to_node.add_outedge(from_id)
        to_node.del_passive_outedge(from_id)


    def del_edge(self, edge):
        from_id, to_id = edge
        from_node = self.nodes[from_id]
        from_node.del_outedge(to_id)
        from_node.add_passive_outedge(to_id)
        to_node = self.nodes[to_id]
        to_node.del_outedge(from_id)
        to_node.add_passive_outedge(from_id)





class RstGraph(Graph):
    # Graph extention with restriction:
    def __init__(self, degree_serie, restriction_set_list, crossing_np_array):

        "fixed parameter"
        self.restriction_set_list = restriction_set_list # list of the restriction subsets, disjunct nodepartition
        self.crossing_matrix = crossing_np_array

        "parameters changesed in swich search"
        # stard node nodes for schlaufen
        self.startnodes = []
        # if schlaufe constains cycle, cycle start node, otherwise 0
        self.cycle_start_nodes =[]

        self.violation_matrix = None
        # build and inserted after random draw from
        super(RstGraph, self).__init__(degree_serie)






