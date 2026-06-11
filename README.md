基于 Spark 的城市居民慢病风险评估系统——以糖尿病健康指标分析为例
本项目基于大数据技术栈，针对 BRFSS 居民健康调查数据集，实现了从 HDFS 数据存储、Hive 数据探索到 Spark MLlib 分布式模型训练的完整大数据开发流程。


项目背景
随着慢病防治工作的推进，通过数据驱动手段进行风险评估已成为趋势。本项目通过分析 25 万条慢病指标数据，探索生活习惯（吸烟、BMI 等）对糖尿病风险的影响，旨在验证大数据分布式计算在智慧医疗领域的工程价值。

技术栈
开发环境: Ubuntu 伪分布式集群

数据存储: HDFS

数据处理: Hive, Spark SQL

机器学习: Spark MLlib (Logistic Regression, Random Forest)

可视化分析: Python (Matplotlib, Seaborn)

目录结构
Plaintext
/
├── dataset/                原始数据文件
├── images/                 分析图表（热力图、分布图）
├── scripts/                
│   ├── diabetes_pipeline_rf.py    # 机器学习建模流水线
│   └── diabetes_analysis.py       # 多维特征可视化分析脚本
├── docs/                   期末作品报告.docx
└── README.md               项目说明
系统功能模块
数据分层治理 (Data Pipeline):

ODS层: 原始数据存储。

DWD层: 完成缺失值处理与特征清洗。

DWS层: 整合向量化后的模型输入数据。

多维特征关联分析:

识别特征共线性，剔除冗余指标（如 MentHlth, PhysHlth）。

分布式风险评估模型:

通过 5 折交叉验证调优随机森林与逻辑回归参数，确保模型在 25 万条数据上的高效计算与高预测精度 (AUC > 0.82)。

运行说明
数据清洗与分析:

Bash
python3 diabetes_analysis.py
模型训练 (提交至 Spark 集群):

Bash
spark-submit /home/cxy/diabetes_pipeline_rf.py
实验结果展示
通过相关性热力图发现 BMI 与高血压是糖尿病的关键风险因子。

模型在测试集上 AUC 表现稳定，满足临床辅助评估的需求。
