import yaml, itertools
def sweep():
    cfg = yaml.safe_load(open('configs/sweep.yaml'))
    for lr, wd in itertools.product(cfg['lrs'], cfg['wds']):
        print(f"Run with lr={lr}, wd={wd}")
if __name__ == "__main__":
    sweep()
