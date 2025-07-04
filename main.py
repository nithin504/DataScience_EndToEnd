from src.datascience import logger
from src.datascience.pipeline.data_ingestionPipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validationPipeline import DataValidationTrainingPipeline
from src.datascience.pipeline.data_transformationPipeline import DataTransformationTrainingPipeline
from src.datascience.pipeline.model_trainerPipeline import ModelTrainerPipeline
from src.datascience.pipeline.model_evaluationPipeline import ModelEvaluationPipeline
logger.info("Logging has been set up successfully.")
STAGE_NAME = "Data Ingestion Stage"
try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        data_ingestion=DataIngestionTrainingPipeline()
        data_ingestion.initiate_data_ingestion()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Data Validation Stage"
try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        data_validation=DataValidationTrainingPipeline()
        data_validation.initiate_data_validation()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Data Trasformation Stage"
try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        data_transform=DataTransformationTrainingPipeline()
        data_transform.initiate_data_transformation()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Model Training Stage"
try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        model_trainer=ModelTrainerPipeline()
        model_trainer.initiate_model_trainer()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Model evaluation Stage"
try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        model_evaluation=ModelEvaluationPipeline()
        model_evaluation.initiate_model_evaluation()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e