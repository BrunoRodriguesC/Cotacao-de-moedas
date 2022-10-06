while True:

    import requests
    from bs4 import BeautifulSoup
    import os


    # Valor do Dolar
    headers = {'User-Agent':"user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"}
    requisicao = requests.get("https://www.google.com/search?client=opera-gx&q=dolar&sourceid=opera&ie=UTF-8&oe=UTF-8",headers=headers)
    soup = BeautifulSoup(requisicao.content, 'html.parser')
    valor_dolar = soup.find_all("span",class_="DFlfde SwHCTb")[0]
    cotacao_dolar = valor_dolar.text


    #Valor do Dolar Canadence
    headers = {'User-Agent':"user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"}
    requisicao = requests.get("https://www.google.com/search?client=opera-gx&q=Dólar+canadense&sourceid=opera&ie=UTF-8&oe=UTF-8",headers=headers)
    soup = BeautifulSoup(requisicao.content, 'html.parser')
    valor_dolar_canadence = soup.find_all("span",class_="DFlfde SwHCTb")[0]
    cotacao_dolar_canadence = valor_dolar_canadence.text


    #Euro
    headers = {'User-Agent':"user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"}
    requisicao = requests.get("https://www.google.com/search?q=euro&client=opera-gx&hs=Xgz&sxsrf=ALiCzsaRe6G2z97Fm9vi2GZB26J1n2KBmg%3A1665022128165&ei=sDg-Y-nLCc2E5OUPjKCxKA&ved=0ahUKEwjp4_fjwsr6AhVNArkGHQxQDAUQ4dUDCA0&uact=5&oq=euro&gs_lcp=Cgdnd3Mtd2l6EAMyDwgAELEDEIMBEEMQRhCCAjILCAAQgAQQsQMQgwEyBAgAEEMyCwgAEIAEELEDEIMBMgQIABBDMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATIOCC4QgAQQsQMQgwEQ1AI6BAgjECc6CggAELEDEIMBEEM6CAguELEDEIMBOgUIABCABEoECEEYAEoECEYYAFAAWIoKYNoOaABwAXgAgAFxiAG1A5IBAzAuNJgBAKABAcABAQ&sclient=gws-wiz",headers=headers)
    soup = BeautifulSoup(requisicao.content, 'html.parser')
    valor_euro = soup.find_all("span",class_="DFlfde SwHCTb")[0] 
    cotacao_euro = valor_euro.text


    #Libra esterlina
    headers = {'User-Agent':"user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"}
    requisicao = requests.get("https://www.google.com/search?client=opera-gx&q=Libra+esterlina&sourceid=opera&ie=UTF-8&oe=UTF-8",headers=headers)
    soup = BeautifulSoup(requisicao.content, 'html.parser')
    valor_libra = soup.find_all("span",class_="DFlfde SwHCTb")[0]
    cotacao_libra = valor_libra.text


    #Franco suico
    headers = {'User-Agent':"user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"}
    requisicao = requests.get("https://www.google.com/search?client=opera-gx&q=Franco+suíço&sourceid=opera&ie=UTF-8&oe=UTF-8",headers=headers)
    soup = BeautifulSoup(requisicao.content, 'html.parser')
    valor_franco = soup.find_all("span",class_="DFlfde SwHCTb")[0]
    cotacao_franco = valor_franco.text


    def Cotacao():
        print(10*"-",'Bem vindo ao Moedas Hoje',10*"-","\n")
        print('1 - Dólar')
        print('2 - Dólar Canadense')
        print('3 - Euro')
        print('4 - Libra esterlina')
        print('5 - Franco suíço')
        print('6 - Sair'"\n")
        conversor = int(input("Digite apenas o numero correspondente a moeda \nPara qual voce deseja ver a cotação?  ""\n"))


        if conversor == 1:
            os.system("cls")
            print(f"A cotação atual do Dólar é: {cotacao_dolar} em Reais")
            voltar = input("Para voltar aperte  1""\n")
            if voltar == 1:
                return Cotacao()


        elif conversor == 2:
            os.system("cls")
            print(f"A cotação atual do Dólar é: {cotacao_dolar_canadence} em Reais")
            voltar = input("Para voltar aperte  1""\n")
            if voltar == 1:
                return Cotacao()

        elif conversor == 3:
            os.system("cls")
            print(f"A cotação atual do Dólar é: {cotacao_euro} em Reais")
            voltar = input("Para voltar aperte  1""\n")
            if voltar == 1:
                return Cotacao()

        elif conversor == 4:
            os.system("cls")
            print(f"A cotação atual do Dólar é: {cotacao_libra} em Reais")
            voltar = input("Para voltar aperte  1""\n")
            if voltar == 1:
                return Cotacao()

        elif conversor == 5:
            os.system("cls")
            print(f"A cotação atual do Dólar é: {cotacao_franco} em Reais")
            voltar = input("Para voltar aperte  1""\n")
            if voltar == 1:
                return Cotacao()


        elif conversor == 6:
            exit()

        else:
            os.system("cls")
            print("Opção Invalida!""\n")
            return Cotacao

    Cotacao()
