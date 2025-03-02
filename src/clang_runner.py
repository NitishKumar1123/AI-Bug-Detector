# src/clang_runner.py
import subprocess
import os

def run_clang_analysis(code_file):
    """Runs Clang Static Analyzer on a given C++ code file."""
    if not os.path.exists(code_file):
        return "Error: File does not exist."

    command = f"clang --analyze {code_file}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    return result.stdout if result.returncode == 0 else "Error in Clang analysis."

if __name__ == "__main__":
    print(run_clang_analysis("test.cpp"))
