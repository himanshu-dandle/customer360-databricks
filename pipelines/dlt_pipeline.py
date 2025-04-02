import dlt
from pyspark.sql.functions import col, to_date

@dlt.table(comment="Raw customer data ingested via Autoloader")
def bronze_customer():
    return (
        spark.readStream.format("cloudFiles")
        .option("cloudFiles.format", "csv")
        .option("header", "true")
        .load("/mnt/data/customer.csv")
    )

@dlt.table(comment="Raw transaction data ingested via Autoloader")
def bronze_transaction():
    return (
        spark.readStream.format("cloudFiles")
        .option("cloudFiles.format", "csv")
        .option("header", "true")
        .load("/mnt/data/transaction.csv")
    )

@dlt.table(comment="Cleansed customer data with expectations")
@dlt.expect("valid_email", "email LIKE '%@%.%'")
def silver_customer():
    return (
        dlt.read("bronze_customer")
        .withColumn("signup_date", to_date(col("signup_date"), "yyyy-MM-dd"))
    )

@dlt.table(comment="Cleansed transaction data with positive amounts")
@dlt.expect("positive_amount", "amount > 0")
def silver_transaction():
    return (
        dlt.read("bronze_transaction")
        .withColumn("transaction_date", to_date(col("transaction_date"), "yyyy-MM-dd"))
    )

@dlt.table(comment="Aggregated customer transaction summary")
def gold_customer_summary():
    transactions = dlt.read("silver_transaction")
    return (
        transactions.groupBy("customer_id")
        .agg({"amount": "sum"})
        .withColumnRenamed("sum(amount)", "total_spent")
    )
