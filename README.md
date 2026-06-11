# 基于 Spark 的城市居民慢病风险评估系统 —— 以糖尿病健康指标分析为例

本项目基于大数据技术栈，针对 BRFSS 居民健康调查数据集，实现了从 HDFS 数据存储、Hive 数据探索到 Spark MLlib 分布式模型训练的完整大数据开发流程。

---

## 项目背景
随着慢病防治工作的推进，通过数据驱动手段进行风险评估已成为趋势。本项目通过分析 25 万条慢病指标数据，探索生活习惯（如吸烟、BMI 等）对糖尿病风险的影响，旨在验证大数据计算在智慧医疗领域的工程价值。

---

## 技术栈
- **开发环境**: Ubuntu 伪分布式环境
- **数据存储**: HDFS
- **数据处理**: Hive, Spark SQL
- **机器学习**: Spark MLlib（逻辑回归、随机森林）
- **可视化分析**: Python（Matplotlib, Seaborn）

---

## 目录结构
```text
/
├── dataset/                # 原始数据文件
├── images/                 # 分析图表（热力图、分布图）
├── scripts/                
│   ├── diabetes_pipeline_rf.py    # 机器学习建模流水线
│   └── diabetes_analysis.py       # 多维特征可视化分析脚本
├── docs/                   # 期末作品报告.docx
└── README.md               # 项目说明
