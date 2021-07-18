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
      
      
  


## 环境准备

## 使用方法
