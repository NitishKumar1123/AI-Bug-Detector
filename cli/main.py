# cli/main.py
import argparse
from src.bug_detector import detect_bug
import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# CLI parser
parser = argparse.ArgumentParser(description="AI-powered C++ Bug Detector")
parser.add_argument("file", type=str, help="C++ source file to analyze")
args = parser.parse_args()

# Read code file
with open(args.file, "r", encoding="utf-8") as f:
    code = f.read()

# Detect bugs
bug, fix = detect_bug(code)

print(f"Bug Type: {bug}\nSuggested Fix: {fix}")
