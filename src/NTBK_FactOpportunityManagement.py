# Databricks notebook source
from pyspark.sql.functions import sum, count, current_timestamp

# ----------------------------
# Read Processed Data
# ----------------------------

df = spark.table("silver.cosell_attachment_processed")

# ----------------------------
# Aggregations
# ----------------------------

df_fact = (
    df.groupBy("amount_category")
    .agg(
        count("*").alias("total_contracts"),
        sum("amount").alias("total_revenue")
    )
)

# ----------------------------
# Add Audit Column
# ----------------------------

df_fact = df_fact.withColumn(
    "load_timestamp",
    current_timestamp()
)

# ----------------------------
# Write Fact Table
# ----------------------------

df_fact.write \
    .mode("overwrite") \
    .saveAsTable("silver.fact_opportunity_management")

print("FactOpportunityManagement completed")
