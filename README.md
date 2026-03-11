## Installation

git clone https://github.com/TEJAS-PARKAR/Resume-Analyzer
cd Resume-Analyzer

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
python -m spacy download en_core_web_sm

streamlit run app.py