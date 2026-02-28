import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here

    L = max(len(seq) for seq in seqs) if max_len is None else max_len 

    if not seqs:
        return seqs
        
    for i in range(len(seqs)):
        seq = seqs[i]
        # print(seq)
        
        temp = np.full(L,pad_value, dtype = np.int32)
        # print(temp.dtype)
        copy_length = min(L, len(seq))
        # np.copyto(temp[:copy_length], seq[:copy_length])
        temp[:copy_length] = seq[:copy_length]
        seqs[i] = temp
        # print(temp)
        # print(temp.dtype)
        # print(type(temp))
        
        
    return seqs

    