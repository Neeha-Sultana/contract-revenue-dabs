# Databricks notebook source
from pyspark.sql.functions import col, when, current_timestamp

# ----------------------------
# Read Silver Data
# ----------------------------

df_contract = spark.table("silver.contract_l2")

print("Initial Count:", df_contract.count())

# ----------------------------
# Data Cleaning
# ----------------------------

df_clean = (
    df_contract
    .filter(col("amount").isNotNull())
    .withColumn(
        "amount_category",
        when(col("amount") >= 2000, "HIGH")
        .when(col("amount") >= 1500, "MEDIUM")
        .otherwise("LOW")
    )
)

# ----------------------------
# Add Audit Columns
# ----------------------------

df_clean = df_clean.withColumn(
    "processed_timestamp",
    current_timestamp()
)

print("After Cleaning:", df_clean.count())

# ----------------------------
# Write Intermediate Table
# ----------------------------

df_clean.write \
    .mode("overwrite") \
    .saveAsTable("silver.cosell_attachment_processed")

print("NB_Cosell_Attachment completed")
