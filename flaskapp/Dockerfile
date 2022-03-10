FROM python

COPY . /app

RUN python3 -m pip install -r /app/requirements.txt

CMD python3 /app/hipflask.py
EXPOSE 9876
