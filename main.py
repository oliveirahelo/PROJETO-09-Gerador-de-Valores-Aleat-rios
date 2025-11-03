# Projeto09_Gerando_valores_aleatórios
# 🐼 Exercícios de Pandas + Random
# Autor: Professor Ricardo Rodrigues Lima

import pandas as pd
import random

# Configurações para exibir todos os dados
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)

# Semente para gerar resultados reproduzíveis
random.seed(42)

print("="*70)
print("💡 1) GERADOR DE NOTAS ALEATÓRIAS")
print("="*70)

# --- 1) Gerador de Notas Aleatórias ---
alunos = [f"Aluno {i+1}" for i in range(10)]

notas = {
    "Aluno": alunos,
    "Matemática": [random.randint(0, 10) for _ in alunos],
    "Português": [random.randint(0, 10) for _ in alunos],
    "Ciências": [random.randint(0, 10) for _ in alunos],
}

df_notas = pd.DataFrame(notas)
df_notas["Média"] = df_notas[["Matemática", "Português", "Ciências"]].mean(axis=1)

print(df_notas)
print("\n🏆 Aluno com a maior média:")
print(df_notas.loc[df_notas["Média"].idxmax()])
print("\n")

# =================================================================
print("="*70)
print("📊 2) VENDAS ALEATÓRIAS DE LOJAS")
print("="*70)

# --- 2) Vendas Aleatórias ---
lojas = [f"Loja {i+1}" for i in range(5)]
dados_vendas = {loja: [random.randint(100, 1000) for _ in range(7)] for loja in lojas}

df_vendas = pd.DataFrame(dados_vendas, index=[f"Dia {i+1}" for i in range(7)])
df_vendas.loc["Total"] = df_vendas.sum()

print(df_vendas)
print("\n🏆 Loja com maior total semanal:")
print(df_vendas.loc["Total"].idxmax(), "-", df_vendas.loc["Total"].max(), "reais")

print("\n💰 Valor médio diário geral:", round(df_vendas.iloc[:-1].mean().mean(), 2))
print("\n")

# =================================================================
print("="*70)
print("📦 3) CONTROLE DE ESTOQUE ALEATÓRIO")
print("="*70)

# --- 3) Controle de Estoque ---
produtos = [f"Produto {i+1}" for i in range(8)]
quantidade = [random.randint(10, 100) for _ in produtos]
preco = [round(random.uniform(5.0, 100.0), 2) for _ in produtos]

df_estoque = pd.DataFrame({
    "Produto": produtos,
    "Quantidade": quantidade,
    "Preço": preco
})
df_estoque["Valor Total"] = df_estoque["Quantidade"] * df_estoque["Preço"]

print(df_estoque)

print("\n💰 Produto com maior valor total:")
print(df_estoque.loc[df_estoque["Valor Total"].idxmax()])

media_valor = df_estoque["Valor Total"].mean()
print("\n📦 Produtos com valor total acima da média:")
print(df_estoque[df_estoque["Valor Total"] > media_valor])
print("\n")

# =================================================================
print("="*70)
print("🎲 4) SORTEIO DE DADOS ALEATÓRIOS")
print("="*70)

# --- 4) Sorteio de Dados ---
resultados = [random.randint(1, 6) for _ in range(50)]
df_dados = pd.DataFrame({
    "Lançamento": range(1, 51),
    "Resultado": resultados
})
df_dados["Par/Ímpar"] = df_dados["Resultado"].apply(lambda x: "Par" if x % 2 == 0 else "Ímpar")

print(df_dados)

print("\n🎲 Quantidade de vezes que cada número saiu:")
print(df_dados["Resultado"].value_counts().sort_index())

print("\n⚖️ Quantidade de números pares e ímpares:")
print(df_dados["Par/Ímpar"].value_counts())

print("\n✅ Fim da execução do Projeto 09 - Gerando Valores Aleatórios ✅")