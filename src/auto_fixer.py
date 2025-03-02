## src/auto_fixer.py
import pandas as pd

def auto_fix_bug(code_snippet):
    """Suggests fixes for given C++ code snippet."""
    df = pd.read_csv("dataset/cplusplus_bugs.csv")
    match = df[df["Code Snippet"] == code_snippet]
    return match["Fixed Code"].values[0] if not match.empty else "No fix available."

if __name__ == "__main__":
    sample_code = "int* p; *p = 10;"  # Example code
    print(auto_fix_bug(sample_code))
