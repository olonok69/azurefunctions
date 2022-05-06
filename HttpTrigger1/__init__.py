import logging
import io
import azure.functions as func
import pandas as pd


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')
    for input_file in req.files.values():
        content = input_file.stream.read()
        conten_pd = io.BytesIO(content)
        test = pd.read_csv(conten_pd)
        print(test.head())
        filename = req.get_body().decode()
        

    if filename:
        return func.HttpResponse(f"Hello, {filename}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
