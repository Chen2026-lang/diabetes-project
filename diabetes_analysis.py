from pyspark.sql import SparkSession
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. 初始化
spark = SparkSession.builder.appName("DiabetesAnalysis").getOrCreate()

# 2. 读取数据 (重用之前测试成功的路径)
file_path = "hdfs://localhost:9000/user/cxy/diabetes/data/diabetes_binary_health_indicators_BRFSS2015.csv"
df = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load(file_path)

# 3. 采样数据 (关键！只取 1% 或更少，防止内存爆炸)
print("正在采样并转换为 Pandas...")
pdf = df.sample(fraction=0.01, seed=42).toPandas()

# 4. 生成可视化图表
print("正在生成热力图...")
plt.figure(figsize=(14, 10))
sns.heatmap(pdf.corr(), annot=False, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Heatmap of Diabetes Health Indicators")
plt.savefig("/home/cxy/correlation_heatmap.png") # 保存图片，稍后你可以通过 SSH 下载查看
print("热力图已保存至: /home/cxy/correlation_heatmap.png")

print("正在生成 BMI 分布箱线图...")
plt.figure(figsize=(8, 6))
sns.boxplot(x='Diabetes_binary', y='BMI', data=pdf)
plt.title("BMI Distribution vs Diabetes Status")
plt.savefig("/home/cxy/bmi_distribution.png")
print("箱线图已保存至: /home/cxy/bmi_distribution.png")

spark.stop()
