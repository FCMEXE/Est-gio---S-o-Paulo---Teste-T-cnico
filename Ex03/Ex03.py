# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora,
#  faça um programa, na linguagem que desejar, que calcule e retorne: 
# • O menor valor de faturamento ocorrido em um dia do mês; 
# • O maior valor de faturamento ocorrido em um dia do mês; 
# • Número de dias no mês em que o valor de faturamento diário foi superior à média
#  mensal. 

# IMPORTANTE: 
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal; 
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. 
# Estes dias devem ser ignorados no cálculo da média; 



def calcular_faturamento(faturamento):
    faturamento_valido = [valor for valor in faturamento if valor > 0]

    menor_faturamento = min(faturamento_valido)
    maior_faturamento = max(faturamento_valido)

    media_mensal = sum(faturamento_valido) / len(faturamento_valido)

    dias_acima_da_media = sum(1 for valor in faturamento if valor > media_mensal)

    return menor_faturamento, maior_faturamento, dias_acima_da_media

faturamento_diario = [
    220, 340, 0, 310, 450, 0, 300, 280, 320, 0, 500, 0, 410, 290, 600,
    0, 0, 470, 0, 480, 550, 330, 400, 310, 0, 390, 450, 370, 0, 0
]

menor, maior, dias_acima_media = calcular_faturamento(faturamento_diario)

print(f"Menor valor de faturamento: {menor}")
print(f"Maior valor de faturamento: {maior}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_media}")
