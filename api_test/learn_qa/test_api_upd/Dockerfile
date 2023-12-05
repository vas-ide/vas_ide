FROM python
WORKDIR /test_api_upd/
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV ENV="dev"
CMD python -m pytest -s /test_api_upd/tests/
#CMD python -m pytest -s --allure=test_results/ /test_api_upd/tests/


#bash ----- docker build -t pytest_runner .
