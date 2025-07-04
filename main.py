from src.datascience import logger
from src.datascience.pipeline.data_ingestionPipeline import DataIngestionTainingPipeline
logger.info("Logging has been set up successfully.")
STAGE_NAME = "Data Ingestion Stage"
try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj=DataIngestionTainingPipeline()
        obj.initiate_data_ingestion()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e