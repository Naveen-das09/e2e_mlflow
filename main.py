from mlproject import logger
from mlproject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlproject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlproject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from mlproject.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
from mlproject.pipeline.stage_03_model_trainer import ModelTrainerTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

try:
        
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<")
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<\n \n x=======x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Data Validation stage"

try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<")
        data_validation = DataValidationTrainingPipeline()
        data_validation.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<\n \n x=======x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Data Transformation Stage"

try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<")
        data_transformation = DataTransformationTrainingPipeline()
        data_transformation.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<\n \n x=======x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = " Model training stage"

try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<")
        model_trainer = ModelTrainerTrainingPipeline()
        model_trainer.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<\n \n x=======x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = " Model evaluation stage"

try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<")
        model_eval = ModelEvaluationTrainingPipeline()
        model_eval.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<\n \n x=======x")
except Exception as e:
        logger.exception(e)
        raise e
