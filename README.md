## End to End DataScience Project

import dagshub
dagshub.init(repo_owner='Arvind0-0', repo_name='ml_project_1', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)