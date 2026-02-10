# Contract Revenue Databricks Asset Bundle

## Project Structure
- `databricks.yml`: Main bundle configuration and target definitions.
- `variables.yml`: Dynamic environment objects (SPN ID, Catalogs).
- `jobs/cosell_job/`: Workflow definition for the 3-notebook chain.
- `src/`: Notebook source code.

## Deployment CLI Commands

Since you’ve been working between **VS Code** and the **Databricks CLI**, here is a organized list of all the commands you used to set up, validate, and deploy your **Contract Revenue** bundle.

I've categorized them so you can copy-paste them into your **README.md** or keep them for your personal notes.

---

### 1. Authentication & Setup

Before the CLI can talk to Azure, you had to set these environment variables in your PowerShell terminal.

```powershell
# Set Service Principal Credentials
$env:ARM_CLIENT_ID = "d513eb19-9395-43a7-b447-b819afb57889"
$env:ARM_TENANT_ID = "569a4924-3fb4-46dd-a652-1cdbfb239032"
$env:ARM_CLIENT_SECRET = "YOUR_SECRET_VALUE"

# Optional: Set the specific profile to avoid 'multiple profiles' error
$env:DATABRICKS_CONFIG_PROFILE = "db-dev"

```

---

### 2. Validation Commands

You used these to check for errors (like the missing `.py` extensions) before actually pushing code to the workspace.

```bash
# Validate the development target
databricks bundle validate -t dev

# Validate the production target (checks SPN permissions)
databricks bundle validate -t prod

```

---

### 3. Deployment (The "Manual Release")

These commands upload your notebooks and create/update the Workflows in Databricks.

```bash
# Deploy to Dev (Schedules are automatically PAUSED by mode: development)
databricks bundle deploy -t dev

# Deploy to Prod (Schedules are ACTIVE and owned by the SPN)
databricks bundle deploy -t prod

```

---

### 4. Git & Branching Commands

To follow the professional **Azure DevOps** flow we discussed, you used these to manage your code history.

```powershell
# Initialize the repo and check version
git init
git --version

# Create and switch to a feature branch
git checkout -b feature/contract-revenue-dabs

# Stage and commit your changes
git add .
git commit -m "feat: initial migration of contract revenue from ADF to DABs"

# Link to GitHub and push
git remote add origin https://github.com/Neeha-Sultana/contract-revenue-dabs.git
git push -u origin feature/contract-revenue-dabs

```

---

### 5. Utility & Debugging

Useful commands to see what is happening inside your bundle.

```bash
# View a summary of the bundle (Who owns it, where it is deployed)
databricks bundle summary

# Trigger an immediate run of the job to test the 3-notebook chain
databricks bundle run -t prod contract_revenue_job1

```

---

### Summary Checklist for your README

If you want to make your **SaaSFactory** repository look professional, I recommend adding this "Quick Start" block to your README:

1. **Auth:** Set `ARM` environment variables.
2. **Validate:** `databricks bundle validate -t <target>`
3. **Deploy:** `databricks bundle deploy -t <target>`
4. **Verify:** Check the Workflows UI in Databricks.

**Since you've now mastered the deployment commands, would you like me to help you add a "Success Notification" to your `cosell_job.yml` so you get an email as soon as the Gold layer finishes building?**
