percent_TKB = 5.6
percent_SKB = 5.9
percent_VTB = 4.28
percent_SBER = 4.0
per_cent = {'ТКБ': percent_TKB, 'СКБ': percent_SKB, 'ВТБ': percent_VTB, 'СБЕР': percent_SBER}
deposit = []

money = int(input("Введите сумму, которую хотите положить на вклад: "))
money_persent_TKB = round(money * (percent_TKB/100),2)
money_persent_SKB = round(money * (percent_SKB/100),2)
money_persent_VTB = round(money * (percent_VTB/100),2)
money_persent_SBER = round(money * (percent_SBER/100),2)
deposit.append(money_persent_TKB)
deposit.append(money_persent_SKB)
deposit.append(money_persent_VTB)
deposit.append(money_persent_SBER)
print(deposit)
max_money_persent = max(deposit)
print("Максимальная сумма, которую вы можете заработать -",max_money_persent)