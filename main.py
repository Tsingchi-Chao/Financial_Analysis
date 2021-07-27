
import pandas as pd
import numpy as np
from financial_analysis.ratio_analysis import RatioAnalysis
from collections import OrderedDict

def main():
    dic_code=OrderedDict()
    code=['601636.SH','000012.SZ','0868.HK','600586.SH']
    compnay_name=['旗滨集团','南玻A','信义玻璃','金晶科技']
    dic_code = dict(zip(code, compnay_name))
    path = r''
    #财务分析
    ratio_analysis=RatioAnalysis("2000-03-31",'2021-06-30',dic_code)
    ratio_analysis.sortProfitabilityData(path)
    ratio_analysis.sortActivityData(path)
    ratio_analysis.sortLiquidityData(path)
    ratio_analysis.sortSolvencyData(path)
    ratio_analysis.sortCFOData(path)
    ratio_analysis.sortCreditData(path)
    ratio_analysis.sortGrowthRata(path)

    #估值分析
#     ratio_analysis = RatioAnalysis("2019-04-26", '2021-04-26', dic_code)
#     ratio_analysis.sortValuationData(path)



if __name__=="__main__":
    main()
