# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
# import json

# import azure.functions as func
import azure.durable_functions as df

from shared_code import Config, Logger

def orchestrator_function(context: df.DurableOrchestrationContext):
    # This logger won't emit any logs during replay
    logger = Logger(context)
    logger.info("Starting orchestrator_one...")

    # Get config - uses cached value when available
    config = Config().load()
    logging.info(f"Current config: {config}")

    logger.info("Calling activity_hello -> Tokyo...")
    result1 = yield context.call_activity("activity_hello", "Tokyo")

    logger.info("Calling activity_hello -> Seattle...")
    result2 = yield context.call_activity("activity_hello", "Seattle")

    logger.info("Calling activity_hello -> London...")
    result3 = yield context.call_activity("activity_hello", "London")

    logger.info("Finishing orchestrator_one")
    return [result1, result2, result3]

main = df.Orchestrator.create(orchestrator_function)
