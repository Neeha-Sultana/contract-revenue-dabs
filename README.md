# SaaSFactory: Contract Revenue Databricks Asset Bundle

This repository manages the Medallion Gold Layer migration from ADF to Databricks Workflows.

## Project Structure
- `databricks.yml`: Main bundle configuration and target definitions.
- `variables.yml`: Dynamic environment objects (SPN ID, Catalogs).
- `jobs/cosell_job/`: Workflow definition for the 3-notebook chain.
- `src/`: Notebook source code.

## Deployment CLI Commands

### 1. Authentication
Before running commands, set the Service Principal credentials in your terminal:
```powershell
$env:ARM_CLIENT_ID = ""
$env:ARM_TENANT_ID = ""
$env:ARM_CLIENT_SECRET = "YOUR_SECRET_VALUE"
