def chunk_text(text, source_id, size=500, overlap=50):
    """Create deterministic word chunks with stable source locators."""
    if size <= overlap or size < 1: raise ValueError("size must exceed overlap")
    words=text.split(); step=size-overlap; out=[]
    for start in range(0,len(words),step):
        body=" ".join(words[start:start+size])
        if body: out.append({"source_id":source_id,"start_word":start,"text":body})
    return out
