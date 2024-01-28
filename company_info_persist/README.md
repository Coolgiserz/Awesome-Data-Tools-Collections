# 企业信息解析与企业画像构建工具
在以下流程中，本项目着重第二点：
- 数据获取（暂略）
- 数据入库
- 数据信息抽取
- 数据检索

## 功能
项目实现了将企查查数据字段解析入库的功能，可针对多个数据文件多进程并行解析入库。

## 技术栈
- pandas
- SQLAlchemy
- postgreSQL

## 难点
- 数据对齐、标准化
- 实体名称消歧

## TODO
- 优化公司简称生成逻辑
- 完善海外企业入库一致性检查逻辑
目前，数据库通过对企业全程、统一社会信用代码建立联合唯一索引保证数据不重复，但对于部分海外公司（包括台湾公司），企查查数据源不一定提供统一社会信用代码数据，因此此类数据可能出现重复
- 