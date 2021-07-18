# Financial_Analysis

该系统主要是为了解决行业研究在提取公司财务数据以及进行财务数据分析时过于繁琐的问题。由于目前金融业使用wind较多，故本系统暂时采用了wind接口，通过自动化从wind提取相关公司财务数据并自动进行财务分析，
最后会将得到的结果以excel的形式输出到本地。

## 功能特点

1. 提取数据。该系统目前主要整合了wind的python API接口，通过设定初始时间和结束时间及公司代码和名称，就可以直接通过wind的API提取财务数据。

2. 覆盖全方位财务分析指标
  
    * 盈利能力
    
       * 毛利率
       * 经营利润率(EBIT/net revenue)
       * 净利率
       * ROA
       * ROE
       * ROIC(投入资本回报率)
       * 销售费用率
       * 管理费用率
       * 财务费用率
       * 销售期间费用率（三费加上研发/营业收入）
       
     * 营运能力
       
       * 总资产周转率(turnover=net revenue/assets)
       * 固定资产周转率(net revenue/average net fixed assets)
       * 营运资本周转率(net revenue/average working capital,here WC=current assets-current liabilities)
       * 应收账款周转天数
       * 应付账款周转天数
       * 存货周转天数
       * 营业周期(Operating cacle=应收账款周转天数+存货周转天数）
       * 现金循环周期，又名净营业周期(Cash conversion cycle=应收账款周转天数+存货周转天数-应付账款周转天数）
       
     * 流动性
     
       * 流动比率(current ratio):流动资产/流动负债
       * 速冻比率(quick ratio):(流动资产-存货)/流动负债
       * 现金比率(Cash ratio):(现金+交易性金融资产)/流动负债
       
     * 偿债能力
     
       * 有息负债/净资产
       * 有息负债/总资产
       * 利息保障倍数（EBIT/Interest)
       * 货币资金加上交易性金融资产/有息负债
       * 货币资金/有息负债
      
     * 估值水平
     
       * PE
       * PB
       * PE历史分位数
       * PB历史分位数
       
     * 现金流数据
     
       * CFO/revenue
       * CFO/average total assets
       * CFO/average total equity
       * CFO/operating income
       * CF0/net income
       * (CFO-perferred dividends)/weighted average number of common shares
       * CFO/total debt(这里采用有息负债)
       * CFO/cash paid for long-term assets(固定资产投资)
       * CFO/cash long-term debt repayment
       * CFO/dividend paid
       * CFO/cash outflows from investing and financing activities
       * (CFO+interest paid+taxes paid)/interest paid
      
    * 信用水平
     
      * Z-score
   
    * 成长性
    
      * 营业收入同比
      * 营业利润同比
      * 净利润同比
      * 归母净利润同比
      * 扣非归母净利润同比
      * CFO同比

## 环境准备
  
* 推荐使用python 3.7及以上
* 推荐使用pycharm

## 使用方法

  1. 参数设定
   
  设定相应的公司代码和公司名称，名称一定要和代码相对应，并设定好路径，最后相关财务分析数据会导出到该路径下。

 <img src="https://github.com/Tsingchi-Chao/Financial_Analysis/blob/master/data/%E5%8F%82%E6%95%B0%E8%AE%BE%E5%AE%9A.png" width="800" height="200" /><br/>
 
 2. 调用相关函数
   
   调用相关函数，包括盈利能力、偿债能力、现金流等等。


<img src="https://github.com/Tsingchi-Chao/Financial_Analysis/blob/master/data/%E8%B0%83%E7%94%A8%E7%9B%B8%E5%85%B3%E5%87%BD%E6%95%B0.png" width="800" height="200" /><br/>

3. 得到结果
   
   结果会以excel的形式直接输出到相应路径下，每个文件是一个方面，如盈利能力， 在该文件中会以sheet形式分别储存各个细分类别。
 
 <img src="https://github.com/Tsingchi-Chao/Financial_Analysis/blob/master/data/%E7%BB%93%E6%9E%9C1.png" width="800" height="200" /><br/>
 <img src="https://github.com/Tsingchi-Chao/Financial_Analysis/blob/master/data/%E7%BB%93%E6%9E%9C2.png" width="800" height="200" /><br/>
 


