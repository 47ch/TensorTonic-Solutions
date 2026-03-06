def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """


    chunks = []
    for i in range(0, len(tokens), chunk_size-overlap):
        chunks.append(tokens[i:i+chunk_size])
        if i+chunk_size >= len(tokens):
            break
    # print(tokens[0:5])

    return chunks
    # Write code here