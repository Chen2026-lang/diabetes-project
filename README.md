# 糖尿病风险预测模型项目

## 项目简介
本项目基于大数据处理生态系统，利用分布式计算技术对 BRFSS 健康调查数据进行挖掘，旨在识别糖尿病的关键风险指标。

## 技术架构
- **分布式存储**: 使用 **HDFS** (Hadoop Distributed File System) 存储原始数据集。
- **数据仓库**: 使用 **Hive** 对数据进行预处理与清洗，进行初步的数据探索 (Data Exploration)。
- **机器学习**: 使用 **PySpark (MLlib)** 进行特征工程、模型训练与超参数调优。
- **可视化**: 利用 Python (Seaborn/Matplotlib) 进行数据关联性分析。

## 项目文件结构
- `diabetes_pipeline_rf.py`: 核心模型流水线（含特征提取与随机森林模型）。
- `diabetes_analysis.py`: 数据可视化分析脚本。
- `correlation_heatmap.png`: 特征相关性热力图（通过分析指标冗余，识别高共线性特征）。
- `bmi_distribution.png`: BMI 分布箱线图（验证 BMI 与糖尿病的显著相关性）。

## 实验总结
通过构建“Hadoop + Hive + Spark”完整大数据流水线，实验验证了模型在处理大规模健康数据集时的有效性。通过特征精炼（剔除 MentHlth/PhysHlth 等冗余项），模型准确率稳定，具有较好的临床解释性。
