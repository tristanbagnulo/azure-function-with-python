import azure.functions as func
import logging
import json

def main(inputMsg: func.QueueMessage, outputMsg: func.Out[func.QueueMessage]) -> None:
    logging.info("Below is the inputMsg values")
    logging.info(inputMsg)
    message = inputMsg.get_body().decode('utf-8')
    logging.info(message)

    # if message.str():
    #     try:
    # logging.info('Python QueueTrigger function processed a message: %s', parsed_message)
    updated_message = f"{inputMsg.get_body().decode('utf-8')} added this text"
    outputMsg.set(updated_message)
        # except Exception as e:
    # logging.error(f'Error parsing message as JSON: {e}')
    # else:
    #     logging.info('Empty message received. Skipping...')
