FROM public.ecr.aws/docker/library/python:3.12-slim

WORKDIR /app
ADD ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app

CMD ["python", "-m", "flask", "run"]
