frutas = 'morango', 'manga', 'laranja', 'jabuticaba', 'maçã'

print("opcoes de frutas:")
print('1:', frutas[0])
print('2:', frutas[1])
print('3:', frutas[2])
print('4:', frutas[3])
print('5:', frutas[4])

opcao = int(input('digite o numero da fruta que você escolheu:')) 

if opcao == 0:
    print('Você escolheu morango.')
    hec = int(input(f'digite a quantidade de hectares da {frutas[0]} que deseja produzir:'))
    gastos = (290 + 67 + 200 + 27 + 890) * hec  
    venda = 2500 
    lucro = venda - gastos 
    print(f'o valor do gasto foi: {gastos} R$') 
    print(f'valor da venda: {venda} R$')
    print(f' meu lucro foi: {lucro} R$') 
    

elif opcao == 1:
    print('você escolheu manga.')
    hec = int(input(f'digite a quantidade de hectares da {frutas[1]} que deseja produzir:'))
    gastos = (800 + 58 + 160 + 350 + 90) * hec
    venda = 3000
    lucro = venda - gastos
    print(f'o valor do gasto foi: {gastos} R$') 
    print(f'valor da venda: {venda} R$')
    print(f' meu lucro foi: {lucro} R$') 
    
elif opcao == 2:
    print('Você escolheu Laranja.')
    hec = int(input(f'digite a quantidade de hectares da {frutas[2]} que deseja produzir:'))
    gastos = (389 + 27 + 483 + 49 + 123) * hec
    venda = 1400
    lucro = venda - gastos
    print(f'o valor do gasto foi: {gastos} R$') 
    print(f'valor da venda: {venda} R$')
    print(f' meu lucro foi: {lucro} R$')

elif opcao == 3:
    print('você escolheu Jabuticaba.')
    hec = int(input(f'digite a quantidade de hectares da {frutas[3]} que deseja produzir:'))
    gastos = (200 + 100 + 65 + 178 + 400) * hec
    venda = 1800
    lucro = venda - gastos
    print(f'o valor do gasto foi: {gastos} R$') 
    print(f'valor da venda: {venda} R$')
    print(f' meu lucro foi: {lucro} R$')

elif opcao == 4:
    print('voce escolheu Maçã.')
    hec = int(input(f'digite a quantidade de hectares da {frutas[4]} que deseja produzir:'))
    gastos = (370 + 269 +854 + 214 + 190) * hec
    venda = 5000
    lucro = venda - gastos 
    print(f'o valor do gasto foi: {gastos} R$') 
    print(f'valor da venda: {venda} R$')
    print(f' meu lucro foi: {lucro} R$')



else: 
    print('opcao inválida.') 