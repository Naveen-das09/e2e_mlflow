from mlproject.config.configuration import ConfigurationManager
from mlproject.components.model_evaluation import ModelEvaluation
from mlproject import logger

STAGE_NAME = "Model evaluation stage"

class ModelEvaluationTrainingPipeline():
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n \n x=============x")
    except Exception as e:
        raise e
