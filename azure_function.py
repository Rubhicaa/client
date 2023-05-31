import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Check if 'file' key is present in the dictionary
    if 'file' in req.files:
        file_stream = req.files['file'].read()

        # Log the received file contents
        logging.info(f'Received file content: {file_stream}')
        # Process the file stream (example: convert to uppercase)
        output_stream = file_stream.upper()

        logging.info(f'Processed output: {output_stream}')

        # Return the processed stream as the response
        return func.HttpResponse(
            output_stream,
            status_code=200,
            headers={'Content-Type': 'application/octet-stream'}
        )
    else:
        return func.HttpResponse(
            "No file found in the request",
            status_code=400
        )

        
        

