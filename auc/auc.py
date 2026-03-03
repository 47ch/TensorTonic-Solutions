import numpy as np

def auc(fpr, tpr):
    """
    Compute AUC (Area Under ROC Curve) using trapezoidal rule.
    """
    # Write code here

    auc = sum([(tpr[i] + tpr[i+1])*(fpr[i+1]-fpr[i])/2 for i in range(len(fpr)-1)])
    
    return auc
    