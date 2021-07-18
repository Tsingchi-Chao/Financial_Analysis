
import pandas as pd
import numpy as np
from collections import OrderedDict

class CommonSizeAnalysis:
    """CommonSizeAnalysis
    It's used to extract data of banlance sheet, incom statement and cash flow sheet and then do common size analysis.
    """
    def __init__(self,
                 start_date:str,
                 end_date:str,
                 dic_code:dict):
        """
                :parameter
                :param start_date: The start date of the data.
                :param end_date: The end date of the data.
                :param dic_code: The code of the company and the key is the code the value is the name of company.
                """
        self.start_date = start_date
        self.end_date = end_date
        self.dic_code = dic_code

    # def extractBSData(self):
    #     """
    #     It's used to extract data of balance sheet from Wind and then calculate banlance sheet account/total assets.
    #     Here we extract
    #     1.
    #     :return:
    #     """