# 糖尿病风险预测模型项目

## 项目简介
本项目基于 Spark MLlib 框架，利用 BRFSS 健康调查数据进行糖尿病风险的预测与分析。

## 包含文件
- `diabetes_pipeline_rf.py`: 核心模型训练流水线（随机森林）。
- `diabetes_analysis.py`: 数据特征相关性分析与可视化代码。
- `correlation_heatmap.png`: 特征相关性热力图（用于分析指标冗余）。
- `bmi_distribution.png`: BMI 分布箱线图（分析患病风险）。

## 实验结果
- 逻辑回归模型 AUC: 0.8240
- 随机森林模型 AUC: 0.8231
- 结论：通过特征精炼（剔除冗余项），模型效率得到提升，线性模型具备优异的解释性。
