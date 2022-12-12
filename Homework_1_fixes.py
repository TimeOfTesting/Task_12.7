per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []

money = int(input("Введите сумму, которую хотите положить на вклад: "))
money_persent_TKB = round(money * (per_cent.get('ТКБ')/100),2)
money_persent_SKB = round(money * (per_cent.get('СКБ')/100),2)
money_persent_VTB = round(money * (per_cent.get('ВТБ')/100),2)
money_persent_SBER = round(money * (per_cent.get('СБЕР')/100),2)
deposit.append(money_persent_TKB)
deposit.append(money_persent_SKB)
deposit.append(money_persent_VTB)
deposit.append(money_persent_SBER)
print(deposit)
max_money_persent = max(deposit)
print("Максимальная сумма, которую вы можете заработать -",max_money_persent)