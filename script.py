import json

import pandas as pd

df = pd.read_json("data.json")

df_valido = df[df['minutes'] > 0].copy()

total_original = len(df)
total_valido = len(df_valido)
registros_ignorados = total_original - total_valido 

print(f"Registros originais: {total_original}")
print(f"Registros válidos: {total_valido}")
print(f"Registros ignorados: {registros_ignorados}")

total_minutes = df_valido["minutes"].sum()
print(f"\nTotal de minutos gastos em todas as tarefas: {total_minutes}") 

tasks_agrupadas = df_valido.groupby(['taskId', 'taskName'])['minutes'].sum().reset_index()
tasks_agrupadas = tasks_agrupadas.rename(columns={'minutes': 'totalMinutes'})

print("\nMinutos totais gastos por tarefa:")
print(tasks_agrupadas.head())

tasks_ordenadas = tasks_agrupadas.sort_values(by=['totalMinutes', 'taskId'], ascending=[False, True])

tasks_ordenadas['percentage'] = tasks_ordenadas['totalMinutes'].apply(
    lambda x: f"{(x / total_minutes) * 100:.2f}%"
)

print("\n--- Tarefas Ordenadas com Porcentagem ---")
print(tasks_ordenadas.head())

task_mais_trabalhada = tasks_ordenadas.iloc[0].to_dict()
top_3_tarefas = tasks_ordenadas[['taskId', 'taskName', 'percentage']].head(3).to_dict(orient='records')

print("\n--- Tarefa Mais Trabalhada ---") 
print(task_mais_trabalhada)
print("\n--- Top 3 Tarefas ---")
print(top_3_tarefas) 

funcs_agrupadas = df_valido.groupby(['userId', 'userName']).agg( 
    totalMinutes = ('minutes', 'sum'),
    taskIds = ('taskId', lambda x: sorted([int(i) for i in x.unique()]))
).reset_index() 

funcs_agrupadas['distinctTasks'] = funcs_agrupadas['taskIds'].apply(len)

print("\n--- Funcionários Agrupados ---")
print(funcs_agrupadas.head())

funcs_por_minutos = funcs_agrupadas.sort_values(by=['totalMinutes', 'userId'], ascending=[False, True]) 
top_3_funcionarios = funcs_por_minutos[['userId', 'userName', 'totalMinutes']].head(3).to_dict(orient='records')    
funcs_por_tarefas = funcs_agrupadas.sort_values(by=['distinctTasks', 'userId'], ascending=[False, True])

usuarios_mais_tarefas = funcs_por_tarefas.iloc[0].to_dict()

print("\n--- Top 3 Funcionários ---")
print(top_3_funcionarios)
print("\n--- Funcionário com Mais Tarefas Distintas ---")
print(usuarios_mais_tarefas)

lista_tarefas_limpa = [int(x) for x in usuarios_mais_tarefas['taskIds']] 

usuarios_mais_tarefas_limpo = {
    "userId": int(usuarios_mais_tarefas['userId']),
    "userName": usuarios_mais_tarefas['userName'],
    "distinctTasks": int(usuarios_mais_tarefas['distinctTasks']),
    "taskIds": lista_tarefas_limpa
}

tarefa_mais_trabalhada_limpa = {
    "taskId": int(task_mais_trabalhada['taskId']),
    "taskName": task_mais_trabalhada['taskName'],
    "totalMinutes": int(task_mais_trabalhada['totalMinutes']),
    "percentage": task_mais_trabalhada['percentage']
}

tasks_ordenadas['taskId'] = tasks_ordenadas['taskId'].astype(int)
tasks_ordenadas['totalMinutes'] = tasks_ordenadas['totalMinutes'].astype(int)

top_3_funcionarios = [
    {
        "userId": int(f["userId"]),
        "userName": f["userName"],
        "totalMinutes": int(f["totalMinutes"])
    }
    for f in top_3_funcionarios
]

resultado_final = {
    "totalMinutes": int(total_minutes),
    "tasks": tasks_ordenadas.to_dict('records'),
    "mostWorkedTask": tarefa_mais_trabalhada_limpa,
    "top3TasksPercentage": top_3_tarefas,
    "top3Employees": top_3_funcionarios,
    "mostDistinctUserOnTasks": usuarios_mais_tarefas_limpo,
    "ignoredRecords": int(registros_ignorados)
}

with open("result.json", "w", encoding="utf-8") as f:
    json.dump(resultado_final, f, indent=2, ensure_ascii=False)

print("\n Arquivo result.json gerado com sucesso!")