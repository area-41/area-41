import js
import pandas as pd
from pyodide.ffi import to_js

def atualizar_status(texto, cor="#22c55e"):
    elem = js.document.getElementById("wasm-status")
    if elem:
        elem.innerText = texto
        elem.style.color = cor

# Atualiza status inicial quando o script Python é carregado pelo navegador
atualizar_status("Pronto (Wasm Ativo)")

def analisar_dados(event):
    atualizar_status("Processando Pandas...", "#eab308")
    
    # Criando um DataFrame de exemplo simulando dados demográficos
    dados = {
        "Região": ["Curitiba", "Londrina", "Maringá", "Cascavel", "Ponta Grossa"],
        "População": [1773733, 555937, 409657, 348051, 358364],
        "IDH": [0.823, 0.778, 0.808, 0.786, 0.763]
    }
    
    df = pd.DataFrame(dados)
    
    # Operações com Pandas
    media_idh = df["IDH"].mean()
    populacao_total = df["População"].sum()
    maior_cidade = df.loc[df["População"].idxmax()]["Região"]
    
    # Montando o resultado formatado
    resultado = f"""[PANDAS EXECUTADO COM SUCESSO NO NAVEGADOR]

--- Amostra do DataFrame ---
{df.to_string(index=False)}

--- Métricas Calculadas ---
• População Total Analisada: {populacao_total:,} habitantes
• IDH Médio das Cidades: {media_idh:.3f}
• Cidade mais populosa: {maior_cidade}
"""
    
    # Exibindo no elemento HTML
    output_elem = js.document.getElementById("output")
    if output_elem:
        output_elem.innerText = resultado
        
    atualizar_status("Concluído", "#22c55e")