import logging
logging.getLogger('angr.analyses').setLevel(logging.INFO)

from cfgexplorer import CFGExplorerCLI

import knowledge
import analysis

from cfgexplorer import CFGVisEndpoint
from bingraphvis import ColorNodes
from vis import AflCovInfo

class AflCFGVisEndpoint(CFGVisEndpoint):
    def __init__(self, cfg):
        super(AflCFGVisEndpoint, self).__init__('cfg', cfg)
    
    def annotate_vis(self, vis, addr):
        kb = self.cfg.project.kb
        vis.add_node_annotator(ColorNodes(filter=lambda node: node.obj.addr in kb.cov.nodes_cov_full, fillcolor='salmon'))
        vis.add_node_annotator(ColorNodes(filter=lambda node: node.obj.addr in kb.cov.nodes_cov_partial, fillcolor='orchid'))
        vis.add_content(AflCovInfo(self.cfg.project))

class AflCovCFGExplorerCLI(CFGExplorerCLI):
    def __init__(self):
        super(AflCovCFGExplorerCLI, self).__init__()    
    
    def _extend_parser(self):
        self.parser.add_argument('aflqueue', metavar='aflqueue', type=str, help='afl fuzz queue directory')

    def _postprocess_cfg(self):
        self.project.analyses.AflCoverage(self.cfg, self.args.aflqueue)

    def add_endpoints(self):
        self.app.add_vis_endpoint(AflCFGVisEndpoint(self.cfg))
