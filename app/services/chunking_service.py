def split_into_chunks(
    text:str,                             # To be converted to chunks
    chunk_size: int = 800,                # 800 char in each chunk
    overlap: int = 100,                   # with overlap we will know which is the next chunk
):
    chunks=[]
    start = 0
    while start < len(text):
        end = start + chunk_size          

        chunks.append(
            text[start:end]              # Appending chunk of 800 char to chunks list
        )

        start += chunk_size - overlap    # Determining new start 

    return chunks

 