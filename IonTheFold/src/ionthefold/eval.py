def sequence_recovery(gt, pred):
    return sum(g==p for g,p in zip(gt,pred))/max(1,len(gt))
