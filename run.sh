echo "Starting"
pip install -r requirements.txt
python main.py
python send_email.py
rm *.csv
