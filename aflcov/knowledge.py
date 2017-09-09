from collections import defaultdict
from angr.knowledge_plugins import KnowledgeBasePlugin

class Coverage(KnowledgeBasePlugin, dict):

    def __init__(self, kb):
        super(Coverage, self).__init__()
        self._kb = kb
        self._nr_of_paths = 0
        self._nodes_hit = defaultdict(int)

        self.nodes_cov_partial = set()
        self.nodes_cov_full = set()

    def copy(self):
        o = IndirectJumps(self._kb)
        o._nr_of_paths = self._nr_of_paths
        o._nodes_hit = _nodes_hit.copy()
        o.nodes_cov_partial.update(self.nodes_cov_partial)
        o.nodes_cov_full.update(self.nodes_cov_full)
        
    def register_new_path(self, nodes_hit=None):
        self._nr_of_paths += 1
        if nodes_hit:
            for addr in nodes_hit:
                self.register_node_hit(addr)

    def register_node_hit(self, addr):
        self._nodes_hit[addr] += 1

    def node_hit_count(self, addr):
        return self._nodes_hit[addr]
    
    @property
    def nr_of_paths(self):
        return self._nr_of_paths
    
    @property
    def nodes_hit(self):
        return len(self._nodes_hit)

KnowledgeBasePlugin.register_default('cov', Coverage)
