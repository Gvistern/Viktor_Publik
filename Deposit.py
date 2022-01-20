money = float(input("Введите сумму которую вы хотите внести на счет"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0} # Дан словарь с банками и процентными ставками.
deposit = []
for key in per_cent:
    [deposit.append(money * per_cent[key] / 100)]
    deposit1 = list(map(int,deposit))
print('deposit =' ,(deposit))
print("Максимальная сумма, которую вы можете заработать -", (max(deposit)))