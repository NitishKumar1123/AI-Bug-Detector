# AI-Powered Bug Detection and Auto-Fix Tool for C++

## Overview
This project is an AI-powered tool designed to detect and fix bugs in C++ code automatically. It leverages machine learning models trained on C++ code snippets to identify common errors such as memory leaks, buffer overflows, and uninitialized variables. The tool provides suggested fixes and supports both a **Command-Line Interface (CLI)** and a **Graphical User Interface (GUI)**.

## Features
- **Automated Bug Detection**: Uses AI models to classify and detect common C++ bugs.
- **Suggested Fixes**: Provides intelligent recommendations for resolving detected issues.
- **Multi-Platform Support**: Works as a CLI tool and a Flask-based web application.
- **Extensible and Scalable**: Designed for future integration into IDEs like VS Code.
- **Machine Learning Models**: Utilizes Random Forest, XGBoost, and fine-tuned GPT models.

## Technologies Used
- **Programming Language**: Python (Backend) & C++ (Testing)
- **Machine Learning**: Scikit-learn, PyTorch, TensorFlow (for model training)
- **Feature Extraction**: LLVM Clang Static Analyzer
- **Backend**: Flask (API for GUI support)
- **Frontend**: HTML, CSS, Bootstrap (for web-based UI)
- **Deployment**: Local Flask Server (Future: Cloud & VS Code Extension)

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.12+
- Flask
- Scikit-learn
- PyTorch
- LLVM Clang Static Analyzer

### Setup
Clone the repository and install dependencies:
```sh
$ git clone https://github.com/NitishKumar1123/AI-Bug-Detector.git
$ cd AI-Bug-Detector
$ python -m venv myenv
$ source myenv/bin/activate   # For Windows: myenv\Scripts\activate
$ pip install -r requirements.txt
```

## Usage
### CLI Mode
Run the tool on a C++ file:
```sh
$ python -m cli.main test.cpp
```
**Example Output:**
```
Bug Type: Memory Leak
Suggested Fix: delete[] ptr;
```

### GUI Mode
Start the Flask web server:
```sh
$ python app.py
```
Open your browser and visit `http://127.0.0.1:5000/` to use the web interface.

## Project Workflow
1. **Data Collection & Preprocessing**:
   - Gathered C++ code snippets with known bugs.
   - Extracted features using Clang Static Analyzer.
   - Vectorized code data using TF-IDF and embeddings.
2. **Model Training & Evaluation**:
   - Trained ML models for bug classification.
   - Evaluated models on Accuracy, Precision, Recall, and F1-score.
3. **CLI Development**:
   - Built a lightweight command-line tool.
4. **GUI Development**:
   - Designed a Flask-based web application for user-friendly bug detection.
5. **Testing & Debugging**:
   - Tested multiple C++ snippets to ensure robust detection.
6. **Deployment & Future Enhancements**:
   - Planned for VS Code extension & cloud-based deployment.

## Future Enhancements
- **VS Code Extension**: Real-time bug detection inside the editor.
- **Cloud API**: Scalable bug analysis via cloud services.
- **Advanced ML Models**: Implement deep learning-based error detection.

## Contributing
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-xyz`).
3. Commit your changes (`git commit -m 'Added new feature'`).
4. Push to your branch (`git push origin feature-xyz`).
5. Submit a pull request.

## License
This project is licensed under the MIT License.

## Contact
For any questions or collaborations, contact: [nitish23129@iiitd.ac.in]

