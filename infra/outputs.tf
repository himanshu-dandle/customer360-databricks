output "catalog_name" {
  value = databricks_catalog.main.name
}

output "schema_name" {
  value = databricks_schema.customer360.name
}

output "pipeline_name" {
  value = databricks_pipeline.customer360.name
}
