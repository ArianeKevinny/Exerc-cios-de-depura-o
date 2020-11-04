def media_100():
    media = 0
    for i in range(0, 100):
        numero = float(input("Digite um número: "))
        media += numero
    media = media/100
    print("A média é {}".format(media))

media_100()