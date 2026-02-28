import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    # Write code here

    positions = np.arange(seq_len)[:, np.newaxis]

    dims = np.arange(d_model)[np.newaxis, :]

    # Compute the angle rates
    angle_rates = 1 / np.power(base, (2 * (dims // 2)) / np.float32(d_model))
    angle_rads = positions * angle_rates

    # Apply sin to even indices (2i) and cos to odd indices (2i+1)
    pos_encoding = np.zeros_like(angle_rads)
    pos_encoding[:, 0::2] = np.sin(angle_rads[:, 0::2])  # even dims
    pos_encoding[:, 1::2] = np.cos(angle_rads[:, 1::2])  # odd dims
     
        
    return pos_encoding
        