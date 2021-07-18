
import pandas as pd
import numpy as np
from collections import OrderedDict
from WindPy import *
w.start()

class RatioAnalysis:
    """RatioAnalysis
    It's used to do ratio analysis of financial analysis.
    The categories are Profitability, Activity, Liquidity, Solvendy, Valuation.
    """
    def __init__(self,start_date:str,end_date:str,dic_code:dict):
        """
        :parameter
        :param start_date: The start date of the data.
        :param end_date: The end date of the data.
        :param dic_code: The code of the company and the key is the code the value is the name of company.
        """
        self.start_date=start_date
        self.end_date=end_date
        self.dic_code=dic_code

    def extractProfitabilityData(self) -> dict:
        """
        It's used to extract profitability data from Wind.
        Here we use
        1.毛利率，
        2.经营利润率(EBIT/net revenue),
        3.净利率，
        4.ROA,
        5.ROE.(这里是扣除非经常性损益的加权平均净资产收益率)
        6.ROIC(投入资本回报率)
        7.销售费用率
        8.管理费用率
        9.财务费用率
        10.销售期间费用率（三费加上研发/营业收入）
        to do analysis.

        :return:A dictionary whose key is the name of company and the value is the data of the company and it's a dataframe
                 whose index is datetime and columns are the indicators we want.
        """
        dic_profitability = OrderedDict()
        for stock_id in self.dic_code.keys():
            data = w.wsd(stock_id,
                         "grossprofitmargin,ebittogr,netprofitmargin,roa,roe_exbasic,roic,operateexpensetogr,adminexpensetogr,finaexpensetogr,expensetosales",
                         self.start_date, self.end_date, "Period=Q;Days=Alldays;PriceAdj=F")
            df = pd.DataFrame(data.Data).T
            df.index = pd.to_datetime(data.Times)
            df.columns = ['毛利率','经营利润率','净利率','ROA','ROE','ROIC','销售费用率','管理费用率','财务费用率','销售期间费用率']
            dic_profitability[self.dic_code[stock_id]] = df
        return dic_profitability

    def sortProfitabilityData(self, path):
        """
        :return: 一个excel中按照指标分为不同的sheet，sheet名称即是指标名称（如资产负债率），sheet中index是datetime，columns是公司名称。
        """
        dic_profitability = RatioAnalysis.extractProfitabilityData(self)
        writer = pd.ExcelWriter(path + '盈利能力.xlsx')
        df1 = dic_profitability[list(dic_profitability.keys())[0]]
        for column in df1.columns:
            data = pd.DataFrame(index=df1.index)
            for company_name in dic_profitability.keys():
                data[company_name] = dic_profitability[company_name][column]
            data['datetime'] = data.index
            data['datetime'] = data['datetime'].apply(lambda x: x.strftime('%Y-%m-%d'))
            data = data.set_index('datetime')
            data.to_excel(writer, sheet_name=column)
        writer.close()

    def extractActivityData(self)->dict:
       """
       It's used to extract activity data from Wind.
       Here we use
       1.总资产周转率(turnover=net revenue/assets),
       2.固定资产周转率(net revenue/average net fixed assets)，
       3.营运资本周转率(net revenue/average working capital,here WC=current assets-current liabilities)，
       4.应收账款周转天数
       5.应付账款周转天数
       6.存货周转天数
       7.营业周期(Operating cacle=应收账款周转天数+存货周转天数）
       8.现金循环周期，又名净营业周期(Cash conversion cycle=应收账款周转天数+存货周转天数-应付账款周转天数）

       :return: A dictionary whose key is the name of company and the value is the data of the company and it's a dataframe
                 whose index is datetime and columns are the indicators we want.
       """
       dic_activity = OrderedDict()
       for stock_id in self.dic_code.keys():
           data=w.wsd(stock_id,
                 "assetsturn1,faturn,operatecaptialturn,arturndays,apturndays,invturndays,turndays,netturndays",
                 self.start_date, self.end_date, "Period=Q;Days=Alldays;PriceAdj=F")
           df = pd.DataFrame(data.Data).T
           df.index = pd.to_datetime(data.Times)
           df.columns = ['总资产周转率','固定资产周转率','营运资本周转率','应收账款周转天数','应付账款周转天数','存货周转天数','营业周期','净营业周期']
           dic_activity[self.dic_code[stock_id]] = df
       return dic_activity

    def sortActivityData(self,path):
        """
        :return: 一个excel中按照指标分为不同的sheet，sheet名称即是指标名称（如资产负债率），sheet中index是datetime，columns是公司名称。
        """
        dic_acticity = RatioAnalysis.extractActivityData(self)
        writer = pd.ExcelWriter(path + '营运能力.xlsx')
        df1 = dic_acticity[list(dic_acticity.keys())[0]]
        for column in df1.columns:
            data = pd.DataFrame(index=df1.index)
            for company_name in dic_acticity.keys():
                data[company_name] = dic_acticity[company_name][column]
            data['datetime'] = data.index
            data['datetime'] = data['datetime'].apply(lambda x: x.strftime('%Y-%m-%d'))
            data = data.set_index('datetime')
            data.to_excel(writer, sheet_name=column)
        writer.close()

    def extractLiquidityData(self):
        """
        It's used to extract liquidity data from Wind.
        Here we use
        1.流动比率(current ratio):流动资产/流动负债
        2.速冻比率(quick ratio):(流动资产-存货)/流动负债
        3.现金比率(Cash ratio):(现金+交易性金融资产)/流动负债

        :return:A dictionary whose key is the name of company and the value is the data of the company and it's a dataframe
                 whose index is datetime and columns are the indicators we want.
        """
        dic_liquidity = OrderedDict()
        for stock_id in self.dic_code.keys():
            data = w.wsd(stock_id,
                         "current,quick,cashtocurrentdebt",
                         self.start_date, self.end_date,"Period=Q;Days=Alldays;PriceAdj=F")
            df = pd.DataFrame(data.Data).T
            df.index = pd.to_datetime(data.Times)
            df.columns = ['流动比率', '速动比率', '现金比率']
            dic_liquidity[self.dic_code[stock_id]] = df
        return dic_liquidity

    def sortLiquidityData(self,path):
        """
        :return:一个excel中按照指标分为不同的sheet，sheet名称即是指标名称（如资产负债率），sheet中index是datetime，columns是公司名称。
        """
        dic_liquidity= RatioAnalysis.extractLiquidityData(self)
        writer = pd.ExcelWriter(path + '流动性.xlsx')
        df1 = dic_liquidity[list(dic_liquidity.keys())[0]]
        for column in df1.columns:
            data = pd.DataFrame(index=df1.index)
            for company_name in dic_liquidity.keys():
                data[company_name] = dic_liquidity[company_name][column]
            data['datetime'] = data.index
            data['datetime'] = data['datetime'].apply(lambda x: x.strftime('%Y-%m-%d'))
            data = data.set_index('datetime')
            data.to_excel(writer, sheet_name=column)
        writer.close()

    def extractSolvencyData(self)->dict:
        """
        It's used to extract the data about solvency from Wind.
        Here we use
        1.有息负债/净资产，
        2.有息负债/总资产，
        3.利息保障倍数（EBIT/Interest),
        4.货币资金加上交易性金融资产/有息负债
        5.货币资金/有息负债
        to do analysis.

        :return: A dictionary whose key is the name of company and the value is the data of the company and it's a dataframe
                 whose index is datetime and columns are the indicators we want.
        """
        dic_solvency = OrderedDict()
        for stock_id in self.dic_code.keys():
            data =w.wsd(stock_id,
                        "interestdebt,tot_equity,tot_assets,ebittointerest,monetary_cap,tradable_fin_assets",
                        self.start_date, self.end_date, "unit=1;rptType=1;currencyType=;Period=Q;Days=Alldays;PriceAdj=F")
            df = pd.DataFrame(data.Data).T
            df.index = pd.to_datetime(data.Times)
            df.columns = ['带息债务','净资产','总资产','利息保障倍数','货币资金','交易性金融资产']
            df['有息负债净资产比']=df['带息债务']/df['净资产']
            df['有息负债总资产比']=df['带息债务']/df['总资产']
            df['货币加金融资产有息负债比']=(df['货币资金']+df['交易性金融资产'])/df['带息债务']
            df['货币资金有息负债比']=df['货币资金']/df['带息债务']
            df=df[['有息负债净资产比','有息负债总资产比','利息保障倍数','货币加金融资产有息负债比','货币资金有息负债比']]
            dic_solvency[self.dic_code[stock_id]] = df
        return dic_solvency

    def sortSolvencyData(self,path):
        """
        :return: 一个excel中按照指标分为不同的sheet，sheet名称即是指标名称（如资产负债率），sheet中index是datetime，columns是公司名称。
        """
        dic_solvency = RatioAnalysis.extractSolvencyData(self)
        writer = pd.ExcelWriter(path + '偿债能力.xlsx')
        df1 = dic_solvency [list(dic_solvency.keys())[0]]
        for column in df1.columns:
            data = pd.DataFrame(index=df1.index)
            for company_name in dic_solvency.keys():
                data[company_name] = dic_solvency[company_name][column]
            data['datetime'] = data.index
            data['datetime'] = data['datetime'].apply(lambda x: x.strftime('%Y-%m-%d'))
            data = data.set_index('datetime')
            data.to_excel(writer, sheet_name=column)
        writer.close()

    def extractValuationData(self)->dict:
        """
        It's used to extract the valuation data from Wind.
        Here we use
        1.PE
        2.PB
        3.PE历史分位数
        4.PB历史分位数

        :return:A dictionary whose key is the name of company and the value is the data of the company and it's a dataframe
                 whose index is datetime and columns are the indicators we want.
        """
        dic_valuation = OrderedDict()
        for stock_id in self.dic_code.keys():
            data = w.wsd(stock_id,
                         "pe_ttm,pb_lyr",
                         self.start_date, self.end_date, "PriceAdj=F")
            df = pd.DataFrame(data.Data).T
            df.index = pd.to_datetime(data.Times)
            df.columns = ['PE_TTM', 'PB']
            df_TTM=df[['PE_TTM']].dropna()
            size_TTM = len(df_TTM) - 1
            df['PE历史分位数'] = df['PE_TTM'].rank().apply(lambda x: 100 * (x - 1) / size_TTM)
            df_PB=df[['PB']].dropna()
            size_PB = len(df_PB) - 1
            df['PB历史分位数'] = df['PB'].rank().apply(lambda x: 100 * (x - 1) / size_PB)
            dic_valuation[self.dic_code[stock_id]] = df
        return dic_valuation

    def sortValuationData(self,path):
        """
        :return: 一个excel中按照指标分为不同的sheet，sheet名称即是指标名称（如资产负债率），sheet中index是datetime，columns是公司名称。
        """
        dic_valuation = RatioAnalysis.extractValuationData(self)
        writer = pd.ExcelWriter(path + '估值水平.xlsx')
        df1 = dic_valuation[list(dic_valuation.keys())[0]]
        for column in df1.columns:
            data = pd.DataFrame(index=df1.index)
            for company_name in dic_valuation.keys():
                data[company_name] = dic_valuation[company_name][column]
            data['datetime'] = data.index
            data['datetime'] = data['datetime'].apply(lambda x: x.strftime('%Y-%m-%d'))
            data = data.set_index('datetime')
            data.to_excel(writer, sheet_name=column)
        writer.close()

    def extractCFOData(self)->dict:
        """
        It's used to extract the data about CFO from Wind.
        Here we use
        I.Performance ratio
        1.CFO/revenue
        2.CFO/average total assets
        3.CFO/average total equity
        4.CFO/operating income
          CF0/net income
        5.(CFO-perferred dividends)/weighted average number of common shares
        II.Coverage ratios
        6.CFO/total debt(这里采用有息负债)
        7.CFO/cash paid for long-term assets(固定资产投资)
        8.CFO/cash long-term debt repayment
        9.CFO/dividend paid
        10.CFO/cash outflows from investing and financing activities
        11.(CFO+interest paid+taxes paid)/interest paid

        :return:A dictionary whose key is the name of company and the value is the data of the company and it's a dataframe
                 whose index is datetime and columns are the indicators we want.
        """
        dic_CFO = OrderedDict()
        for stock_id in self.dic_code.keys():
            data = w.wsd(stock_id,
                         "oper_rev,tot_assets,tot_equity,opprofit,ocfps_ttm,interestdebt,div_aualaccmdiv3,stot_cash_outflows_inv_act,stot_cash_outflows_fnc_act,net_cash_flows_oper_act,net_profit_is",
                         self.start_date, self.end_date, "unit=1;rptType=1;year=2019;currencyType=;Period=Q;Days=Alldays;PriceAdj=F")
            df = pd.DataFrame(data.Data).T
            df.index = pd.to_datetime(data.Times)
            df.columns = ['营业收入', '总资产','净资产','营业利润','每股经营活动现金流净额','带息债务','年度累积分红总额','投资活动流出','筹资活动流出','CFO','净利润']
            df['CFO_revenue']=df['CFO']/df['营业收入']
            df['CFO_total_assets']=df['CFO']/((df['总资产']+df['总资产'].shift())/2)
            df['CFO_book_value']=df['CFO']/((df['净资产']+df['净资产'].shift())/2)
            df['CFO_operating_income']=df['CFO']/df['营业利润']
            df['CFO_net_income']=df['CFO']/df['净利润']
            df['CFO_有息负债']=df['CFO']/df['带息债务']
            df['CFO_分红总额']=df['CFO']/df['年度累积分红总额']
            df['CFO_投资筹资现金流出']=df['CFO']/(df['投资活动流出']+df['投资活动流出'])
            df=df[['CFO_revenue','CFO_total_assets','CFO_book_value','CFO_operating_income','CFO_net_income','每股经营活动现金流净额','CFO_有息负债','CFO_分红总额','CFO_投资筹资现金流出']]
            dic_CFO [self.dic_code[stock_id]] = df
        return dic_CFO
    def sortCFOData(self,path):
        """
        :return: 一个excel中按照指标分为不同的sheet，sheet名称即是指标名称（如资产负债率），sheet中index是datetime，columns是公司名称。
        """
        dic_CFO = RatioAnalysis.extractCFOData(self)
        writer = pd.ExcelWriter(path + '现金流.xlsx')
        df1 = dic_CFO[list(dic_CFO.keys())[0]]
        for column in df1.columns:
            data = pd.DataFrame(index=df1.index)
            for company_name in dic_CFO.keys():
                data[company_name] = dic_CFO[company_name][column]
            data['datetime'] = data.index
            data['datetime'] = data['datetime'].apply(lambda x: x.strftime('%Y-%m-%d'))
            data = data.set_index('datetime')
            data.to_excel(writer, sheet_name=column)
        writer.close()

    def extractCreditData(self)->dict:
        """
        It's used to extract the data about credit from Wind.
        Here we use
        1.Z-score
        to do analysis.
        """
        dic_credit = OrderedDict()
        for stock_id in self.dic_code.keys():
            data = w.wsd(stock_id,
                         "z_score",
                         self.start_date, self.end_date, "Period=Q;Days=Alldays;PriceAdj=F")
            df = pd.DataFrame(data.Data).T
            df.index = pd.to_datetime(data.Times)
            df.columns = ['z_score']
            dic_credit[self.dic_code[stock_id]] = df
        return dic_credit


    def sortCreditData(self,path):
        """
        :return: 一个excel中按照指标分为不同的sheet，sheet名称即是指标名称（如资产负债率），sheet中index是datetime，columns是公司名称。
        """
        dic_credit = RatioAnalysis.extractCreditData(self)
        writer = pd.ExcelWriter(path + '信用评估.xlsx')
        df1 = dic_credit[list(dic_credit.keys())[0]]
        for column in df1.columns:
            data = pd.DataFrame(index=df1.index)
            for company_name in dic_credit.keys():
                data[company_name] = dic_credit[company_name][column]
            data['datetime'] = data.index
            data['datetime'] = data['datetime'].apply(lambda x: x.strftime('%Y-%m-%d'))
            data = data.set_index('datetime')
            data.to_excel(writer, sheet_name=column)
        writer.close()

    def extractGrowthRate(self)->dict:
        """
        It's used to extract the data about growth rate from Wind.
        Here we use
        1.营业收入同比
        2.营业利润同比
        3.净利润同比
        4.归母净利润同比
        5.扣非归母净利润同比
        6.CFO同比

        :return:A dictionary whose key is the name of company and the value is the data of the company and it's a dataframe
                 whose index is datetime and columns are the indicators we want.
        """
        dic_growth_rate = OrderedDict()
        for stock_id in self.dic_code.keys():
            data = w.wsd(stock_id,
                         "yoy_or,yoyop,yoyprofit,yoynetprofit,yoynetprofit_deducted,yoyocf",
                         self.start_date, self.end_date,
                         "Period=Q;Days=Alldays;PriceAdj=F")
            df = pd.DataFrame(data.Data).T
            df.index = pd.to_datetime(data.Times)
            df.columns = ['营业收入同比', '营业利润同比', '净利润同比', '归母净利润同比', '扣非归母净利润同比', 'CFO同比']
            dic_growth_rate[self.dic_code[stock_id]] = df
        return dic_growth_rate

    def sortGrowthRata(self,path):
        """
        :return: 一个excel中按照指标分为不同的sheet，sheet名称即是指标名称，sheet中index是datetime，columns是公司名称。
        """
        dic_growth_rate= RatioAnalysis.extractGrowthRate(self)
        writer = pd.ExcelWriter(path + '成长性.xlsx')
        df1 = dic_growth_rate[list(dic_growth_rate.keys())[0]]
        for column in df1.columns:
            data = pd.DataFrame(index=df1.index)
            for company_name in dic_growth_rate.keys():
                data[company_name] = dic_growth_rate[company_name][column]
            data['datetime'] = data.index
            data['datetime'] = data['datetime'].apply(lambda x: x.strftime('%Y-%m-%d'))
            data = data.set_index('datetime')
            data.to_excel(writer, sheet_name=column)
        writer.close()




