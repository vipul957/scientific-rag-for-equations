from scientific_rag_for_equations.chunking import chunk_text
def test_chunk(): assert chunk_text("one two three","paper",2,1)[0]["start_word"] == 0
