#Calculadora de Consumo Energético
#Cálculo de Consumo de Energia Elétrica
#Autora: Sarah Pitanga

  # --- Cálculo de Consumo de Energia ---
print("Calculadora de Consumo Elétrico")
print("="*30)

    # Entradas de dados
aparelho = "Geladeira"  # Exemplo de aparelho
potencia = 100 #Watts
horas_dia = 24 #horas por dia

    # Cálculo do consumo mensal (kWh)
    # Fórmula: (Watts * Horas * Dias) / 1000
consumo_mensal = (potencia * horas_dia * 30) / 1000

    # Bônus: Cálculo de custo (Baseado na dica de R$ 0,75 por kWh)
valor_kwh = 0.75
custo_estimado = consumo_mensal * valor_kwh

    # Exibição dos resultados
print("\n" + "-"*30)
print(f"Aparelho: {aparelho}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print(f"Custo estimado: R$ {custo_estimado:.2f} (Tarifa: R$ {valor_kwh}/kWh)")
print("-"*30)