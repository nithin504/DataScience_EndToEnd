import os
from src.datascience import logger
import pandas as pd
from src.datascience.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
        logger.info(f"Data Validation Config: {self.config}")

    def validate_all_columns(self)-> bool:
        try:
            validation_status = True
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols=list(data.columns)
            all_schema=self.config.all_schema

            for col in all_cols:
                if col not in all_schema:
                    validation_status= False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation Status: {validation_status}\n")

                else:
                    validation_status= True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation Status: {validation_status}\n")    

            return validation_status
        except Exception as e:
            raise e