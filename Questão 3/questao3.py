#3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, 
#faça um programa, na linguagem que desejar, que calcule e retorne:
#• O menor valor de faturamento ocorrido em um dia do mês;
#• O maior valor de faturamento ocorrido em um dia do mês;
#• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

#IMPORTANTE:
#a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
#b) Podem existir dias sem faturamento, como nos finais de semana e feriados. 
# Estes dias devem ser ignorados no cálculo da média;

import json 

with open('dados.json', 'r') as file:
    faturamento_distribuidora = json.load(file)

faturamento = [f['valor'] for f in faturamento_distribuidora if f ['valor'] > 0]

faturamento_min = min(faturamento)
faturamento_max = max(faturamento)

faturamento_medio = sum(faturamento)/ len(faturamento)

faturamento_acima_media = [f['dia'] for f in faturamento_distribuidora if f ['valor'] > faturamento_medio]

print(f"O menor faturamento ocorrido no mes foi R${faturamento_min}")
print(f"O maior faturamento ocorrido no mes foi R${faturamento_max}")
print(f"Dias em que o faturamento foi maior que a media mensal: {faturamento_acima_media}")
