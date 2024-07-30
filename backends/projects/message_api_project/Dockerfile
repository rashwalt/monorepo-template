FROM python:3.12

ARG project_name=message_api_project
ARG project_version=0.1.0
ARG wheel=$project_name-$project_version-py3-none-any.whl

RUN python -m pip install --upgrade pip

WORKDIR /code

COPY projects/$project_name/dist/$wheel /code/$wheel
RUN pip install --no-cache-dir --upgrade /code/$wheel

CMD ["uvicorn", "backends.message_api.core:app", "--host", "0.0.0.0", "--port", "8000"]
