# Scrapy Shell
   - 交互终端
   - python开发环境下
   - ipython
## 启动 scrapy shell
   - scrapy shell "www.baidu.com" ：请求页面
   - response.body.decode("utf-8") ：页面源码

## Scrapy 提供的选择器
   - 基本选择器
       - xpath(): 传入xpath选择器，得到selector列表
       - 得到的selector列表 通过 extract()来转换陈字符串
       
       - css():同xpath()
 
## scrapy 快速存储方式
   - scrapy crawl xxx -o filename.json/csv
   - mingyan_spider

## scrapy 日志等级
   - DEBUG:调试信息
   - INFO：一般信息
   - WARNING:警告信息
   - ERROR：一般错误
   - CRITICAL：严重错误
   
## scrapy 日志设置（在setting里设置）
   - LOG_ENABLED：默认True，启用
   - LOG_ENCODING：编码类型 默认utf-8
   - LOG_FILE：日志的输出文件 默认当前路径 
   - LOG_LEVEL:日志等级 默认DEBUG