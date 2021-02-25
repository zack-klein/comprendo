FROM public.ecr.aws/lambda/python:3.8

RUN yum install git -y
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY ./lambdahandler.py .
COPY ./compo.py .

CMD ["lambdahandler.handler"]