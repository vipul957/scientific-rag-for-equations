from scientific_rag_for_equations.records import Evidence, normalize_equation, require_evidence

def test_normalize(): assert normalize_equation(" E  =  mc² ") == "E = mc²"

def test_grounding(): assert require_evidence("x", [Evidence("a", "q", "p1")])["grounded"]
