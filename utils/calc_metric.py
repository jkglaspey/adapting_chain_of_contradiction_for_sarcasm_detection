@staticmethod
def calc_precision(TP: int, FP: int) -> float:
    if TP + FP == 0:
        return 0.0
    
    return TP / (TP + FP)


@staticmethod
def calc_recall(TP: int, FN: int) -> float:
    if TP + FN == 0:
        return 0.0
    
    return TP / (TP + FN)


@staticmethod
def calc_F1(P: int, R: int) -> float:
    if P + R == 0:
        return 0.0
    
    return 2.0 * (P * R) / (P + R)


@staticmethod
def calc_acc(TP: int, TN: int, FP: int, FN: int) -> float:
    denom = TP + FN + FP + TN
    if denom == 0:
        return 0.0
    
    return TP + TN / denom