CREATE OR REPLACE FUNCTION main.customer360_schema.fn_get_customer_summary()
RETURNS TABLE (customer_id INT, total_spent DOUBLE)
RETURN
SELECT * FROM main.customer360_schema.gold_customer_summary;
