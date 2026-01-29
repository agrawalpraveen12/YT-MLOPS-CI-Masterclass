# 🔢 YT-MLOPS-CI-Masterclass

Modernized version of the MLOps Continuous Integration (CI) Masterclass. This project demonstrates a complete CI pipeline using GitHub Actions, Python, and Streamlit.

## 🚀 Overview

This repository contains a simple Power Calculator application that allows users to compute the square, cube, and fifth power of any number. The main goal is to showcase:
- **Modular Code Structure**: Logic is separated into `utils.py`.
- **Modern Tech Stack**: Python 3.11, Streamlit, Pytest, and Ruff.
- **Automated CI**: GitHub Actions for linting and testing.
- **Containerization**: Docker support for easy deployment.

## 📂 Project Structure

```text
YT-MLOPS-CI-Masterclass/
├── .github/workflows/
│   └── ci.yaml          # GitHub Actions CI pipeline
├── app.py               # Streamlit UI
├── utils.py             # Calculation logic
├── _test.py             # Pytest suite
├── requirements.txt     # Python dependencies
├── pyproject.toml       # Modern project configuration
├── Dockerfile           # Container configuration
└── README.md            # Documentation
```

## 🛠️ Setup & Installation

### Local Setup
1. **Clone the repository**:
   ```bash
   git clone <repo-url>
   cd YT-MLOPS-CI-Masterclass
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the App**:
   ```bash
   streamlit run app.py
   ```

### Running Tests
Execute the following to run automated tests:
```bash
pytest
```

To check for code quality issues:
```bash
ruff check .
```

### Docker
Build and run the app in a container:
```bash
docker build -t power-calc .
docker run -p 8501:8501 power-calc
```

## ⚙️ CI/CD Pipeline

The `.github/workflows/ci.yaml` file defines the CI process:
1. **Linting**: Uses `ruff` to ensure code style consistency.
2. **Testing**: Runs `pytest` to verify mathematical logic.

---
*Created for the YT-MLOPS-CI Masterclass.*
