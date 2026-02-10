# Databricks notebook source
from pyspark.sql.functions import col, round, current_timestamp

# ----------------------------
# Read Fact Table
# ----------------------------

df_fact = spark.table("silver.fact_opportunity_management")

# ----------------------------
# Business Calculations
# ----------------------------

df_gold = (
    df_fact
    .withColumn(
        "avg_revenue_per_contract",
        round(col("total_revenue") / col("total_contracts"), 2)
    )
)

# ----------------------------
# Add Gold Audit Column
# ----------------------------

df_gold = df_gold.withColumn(
    "gold_load_timestamp",
    current_timestamp()
)

# ----------------------------
# Write Gold Table
# ----------------------------

df_gold.write.mode("overwrite").option("mergeSchema", "true").saveAsTable("gold.contract_revenue")

print("Gold table created successfully")
