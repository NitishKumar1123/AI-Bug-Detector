from flask import Flask, render_template, request
import os
import sys

# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.bug_detector import detect_bug  # Removed unused predict_bug

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    # Read file content before passing it to detect_bug()
    with open(filepath, "r", encoding="utf-8") as f:
        code_snippet = f.read()

    # Run bug detection
    bug_type, fix_suggestion = detect_bug(code_snippet)

    return render_template('index.html', bug_type=bug_type, fix_suggestion=fix_suggestion)

if __name__ == '__main__':
    app.run(debug=True)
