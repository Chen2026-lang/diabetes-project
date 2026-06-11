from pyspark.sql import SparkSession
from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator
from pyspark.ml.evaluation import BinaryClassificationEvaluator

# 1. 初始化
spark = SparkSession.builder.appName("DiabetesPredictor_RF").getOrCreate()

# 2. 读取数据
file_path = "hdfs://localhost:9000/user/cxy/diabetes/data/diabetes_binary_health_indicators_BRFSS2015.csv"
df = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load(file_path)

# 3. 特征精炼 (剔除冗余项)
exclude_cols = ['Diabetes_binary', 'MentHlth', 'PhysHlth']
feature_cols = [col for col in df.columns if col not in exclude_cols]

assembler = VectorAssembler(inputCols=feature_cols, outputCol="features")

# 4. 定义随机森林模型
rf = RandomForestClassifier(featuresCol="features", labelCol="Diabetes_binary")

# 5. 构建流水线 (注意：这里不再需要 StandardScaler)
pipeline = Pipeline(stages=[assembler, rf])

# 6. 配置超参数调优
paramGrid = ParamGridBuilder() \
    .addGrid(rf.numTrees, [20, 50]) \
    .addGrid(rf.maxDepth, [5, 10]) \
    .build()

evaluator = BinaryClassificationEvaluator(labelCol="Diabetes_binary", metricName="areaUnderROC")

# 7. 交叉验证
crossval = CrossValidator(estimator=pipeline,
                          estimatorParamMaps=paramGrid,
                          evaluator=evaluator,
                          numFolds=5)

# 8. 训练模型
print("正在使用随机森林进行训练，这可能需要一点时间...")
train_data, test_data = df.randomSplit([0.8, 0.2], seed=42)
cvModel = crossval.fit(train_data)

# 9. 评估
auc = evaluator.evaluate(cvModel.transform(test_data))
print(f"随机森林模型测试集 AUC 评分: {auc:.4f}")

# 10. 输出最优参数
best_rf = cvModel.bestModel.stages[-1]
print(f"最优参数: numTrees={best_rf._java_obj.getNumTrees()}, maxDepth={best_rf._java_obj.getMaxDepth()}")
