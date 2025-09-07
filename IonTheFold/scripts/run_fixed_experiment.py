import argparse, yaml
from ionthefold.models.enhancement import DualPathEnhancementPredictor

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--config', default='configs/model.yaml')
    args = p.parse_args()
    cfg = yaml.safe_load(open(args.config))
    model = DualPathEnhancementPredictor(cfg)
    print("Loaded model with cfg keys:", list(cfg or {}).keys())

if __name__ == "__main__":
    main()
