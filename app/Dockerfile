FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

WORKDIR /code

COPY . .

RUN pip install -r ./requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/app/"

CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "5000"]
