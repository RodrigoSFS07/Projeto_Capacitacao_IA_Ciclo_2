import mlflow
import pandas as pd

#3.10) Escrever um código Cliente para carregar os modelos registrados e exibir as informações desses modelos com a sua descrição.

# Configura o cliente MLflow com o URL fornecido pelo NGROK
mlflow.set_tracking_uri("https://ef00-35-231-71-79.ngrok-free.app/")

# Definir o nome do experimento no MLflow
exp_mlflow_ciclo2 = "exp_projeto_ciclo_2"

# Acessa todos os runs do experimento específico
runs = mlflow.search_runs(experiment_ids=mlflow.get_experiment_by_name(exp_mlflow_ciclo2).experiment_id)

# Verifica se há runs com métricas
if runs.empty:
    raise ValueError("Nenhum run encontrado.")

# Ordena os runs pela métrica de acurácia em ordem decrescente
runs_sorted = runs.sort_values(by='metrics.accuracy', ascending=False)

# Recupera os três melhores runs
top_3_runs = runs_sorted.head(3)

# Lista para armazenar as informações dos modelos
model_info_list = []

# Dicionário de descrições dos modelos
model_descriptions = {
    "RandomForest_OLA_var1": "RandomForest OLA variação 1",
    "RandomForest_KNORAE_var1": "RandomForest KNORAE variação 1",
    "RandomForest_KNORAU_var1": "RandomForest KNORAU variação 1",
}

# Loop sobre os três melhores runs
for idx, row in top_3_runs.iterrows():
    run_id = row['run_id']
    run_info = mlflow.get_run(run_id)
    model_name = run_info.data.tags.get("mlflow.runName")
    accuracy = row['metrics.accuracy']
    description = model_descriptions.get(model_name, 'N/A')
    model_info_list.append({"Modelo": model_name, "Descrição": description, "Acurácia": accuracy})

# Cria um DataFrame com as informações dos modelos
model_df = pd.DataFrame(model_info_list)

# Exibe as informações dos modelos
print(model_df)
