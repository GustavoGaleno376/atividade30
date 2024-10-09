# crie uma funcao que calcule a nota a media de 3 notas em seguida verifique se ele esta aprovado ou reprovado para notas acima de 
nota1=int(input("digite a nota 1 "))
nota2=int(input("digite a nota 2 "))
nota3=int(input("digite a nota 3 "))

media=nota1+nota2+nota3/3

def media_de_notas(media):
    if media >=7:
        print("você está aprovado")
    else:
        print("você está reprovado")
    return media_de_notas

resultado=media_de_notas(media)     
print(resultado)
    