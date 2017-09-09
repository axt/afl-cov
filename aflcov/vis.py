from bingraphvis.base import Content

class AflCovInfo(Content):
    def __init__(self, project):
        super(AflCovInfo, self).__init__('aflcovinfo', ['text'])
        self.project = project
        
    def gen_render(self, n):
        node = n.obj
        n.content[self.name] = {
            'data': [{
                'text': {
                    'content': "Hit: %d / %d " % (self.project.kb.cov.node_hit_count(node.addr), self.project.kb.cov.nr_of_paths),
                    'style':'B',
                    'align':'LEFT'
                }
            }], 
            'columns': self.get_columns()
        }
