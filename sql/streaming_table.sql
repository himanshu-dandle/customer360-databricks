
CREATE OR REFRESH STREAMING TABLE customer_stream AS
SELECT * FROM main.customer360_schema.silver_customer;

