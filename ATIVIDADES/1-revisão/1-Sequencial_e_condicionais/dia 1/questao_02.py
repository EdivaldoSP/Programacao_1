hora = int(input("Digite a hora: "))
minuto = int(input("Digite o minuto: "))

minuto_segundo = minuto * 60
hora_segundo = 60 * 60

hora_convertida = hora * hora_segundo

total = minuto_segundo + hora_convertida

print(f"Hora e minutos convertido em segundos: {total}")