class DualPathEnhancementPredictor:
    def __init__(self, cfg=None):
        self.cfg = cfg or {}
    def forward(self, x):
        return x
