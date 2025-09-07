def approx_charge(seq, his_weight=0.1):
    s=(seq or '').upper()
    return s.count('K')+s.count('R')+his_weight*s.count('H')-(s.count('D')+s.count('E'))
