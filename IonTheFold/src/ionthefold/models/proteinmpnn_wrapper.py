class ProteinMPNNWrapper:
    def __init__(self, cfg=None):
        self.cfg = cfg or {}
    def design(self, backbone):
        return 'ACDEFGHIKLMNPQRSTVWY'
