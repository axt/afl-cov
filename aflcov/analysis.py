import logging
l = logging.getLogger('angr.analyses.axt.aflcoverage')


import os
from angr.analyses import Analysis, register_analysis
import tracer

class LightTracer(tracer.Tracer):
    def _prepare_paths(self):
        pass

class AflCoverage(Analysis):
    def __init__(self, cfg, afl_queue_path, max_samples=None):
        super(AflCoverage, self).__init__()
        self.cfg = cfg
        self.afl_queue_path = afl_queue_path
        self.max_samples = max_samples
        self.nodes_cov_partial = set()
        self.nodes_cov_full = set()
        self._analyse()

    def _analyse(self):
        queue_files = os.listdir(self.afl_queue_path)
        kb = self.project.kb
        for i, f in enumerate(queue_files):
            binary = self.project.filename
            argv = [ binary, self.afl_queue_path + "/" + f]
            #will be available in new tracer
            #t = tracer.QEMURunner(project=self.project, binary=sample.binary,  input="", argv=argv)
            t = LightTracer(project=self.project, binary=binary,  input="", argv=argv)
            kb.cov.register_new_path(set(t.trace))
            l.info("Processing [%d/%d] %s, blocks hit: %d" % (i+1, len(queue_files), f, kb.cov.nodes_hit))
            if self.max_samples and i+1 >= self.max_samples:
                break

        for pnode in self.cfg.nodes():
            if kb.cov.node_hit_count(pnode.addr) == 0:
                continue
            partial = False
            for node in self.cfg.get_all_nodes(pnode.addr):
                for succ in self.cfg.graph.successors(node):
                    if kb.cov.node_hit_count(succ.addr) == 0:
                        partial = True
                        break
            if partial:
                kb.cov.nodes_cov_partial.add(node.addr)
            else:
                kb.cov.nodes_cov_full.add(node.addr)

register_analysis(AflCoverage, 'AflCoverage')
