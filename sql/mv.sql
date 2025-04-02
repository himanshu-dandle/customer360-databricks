CREATE OR REFRESH MATERIALIZED VIEW main.customer360_schema.mv_top_customers AS
SELECT customer_id, total_spent
FROM main.customer360_schema.gold_customer_summary
WHERE total_spent > 200
ORDER BY total_spent DESC;
