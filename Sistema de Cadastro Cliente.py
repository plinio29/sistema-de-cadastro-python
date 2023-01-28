#Importando as Principais Bibliotecas
from PyQt5 import uic,QtWidgets
from PyQt5.QtWidgets import QMessageBox
from pathlib2 import Path


#Primeiro botão tela1
def funcao_principal():
    print('teste1')
    #Iniciando a segunda tela
    tela2.show()
#Segundo botão tela1
def funcao_principal2():
    #inicia a terceira tela
    tela3.show()
    tela3.frame_2.close()
    print('teste2')

#botão tela2
def funcao_secundaria():
    print('teste3')

    nome = tela2.nome.text()
    dat1dia = tela2.datdia.text()
    dat1mes = tela2.datmes.text()
    dat1ano = tela2.datano.text()
    debitoreal = tela2.debitoreal.text()
    debitocentavos = tela2.debitocentavos.text()
    #LIMPANDO CAIXAS DE TEXTO
    tela2.nome.setText('')
    tela2.datdia.setText('')
    tela2.datmes.setText('')
    tela2.datano.setText('')
    tela2.debitoreal.setText('')
    tela2.debitocentavos.setText('')
        
    #Checando as caixas de digitação
    if nome == '' and dat1dia == '' and dat1mes == '' and dat1ano == '' and debitoreal == '' and debitocentavos == '':
        QMessageBox.about(tela2,'Resultado', 'ERRO!')
    else:
        QMessageBox.about(tela2,'Resultado', 'NOME: ' + nome + '\n' + 'DATA: ' + dat1dia +'/'+ dat1mes +'/'+ dat1ano + '\n' + 'DÉBITO: ' + debitoreal +','+ debitocentavos + '\n' 'CADASTRO CONCLUÍDO!')

        #Abrindo Arquivo e Salvando em um Documento txt.
        arquivo = open("C:\\Users\\Admin\\Documents\\Projetos Github\\sistema-de-cadastro-python\\duastelasteste.txt", "a")

        arquivo.write('NOME:' + nome + '  ' + 'DATA: ' + dat1dia +'/'+ dat1mes +'/'+ dat1ano + '  ' + '\n\n')
        arquivo.close()
        
        #Abrindo e salvando um segundo arquivo
        arquivo2 = open("C:\\Users\\Admin\\Documents\\Projetos Github\\sistema-de-cadastro-python\\duastelasteste2.txt", "a")
        arquivo2.write('NOME:' + nome + '  ' + 'DÉBITO: R$' + ' ' + debitoreal + ',' + debitocentavos + '\n\n')
        arquivo2.close()
    
#botão tela3        
def funcao_secundaria2():
    print('teste4')
    pnome = tela3.pnome.text()

    if pnome == '':
        QMessageBox.about(tela3,'Resultado', 'ERRO!')
    else:
        pnome = (str(pnome))
        #Abrindo Arquivo e lendo em um Documento txt.
        arquivo = open("C:\\Users\\Admin\\Documents\\Projetos Github\\sistema-de-cadastro-python\\duastelasteste.txt", "r")
        contador = 0
        for linha in arquivo:
            linha = linha.rstrip()
            if pnome in linha:
                contador = contador + 1
                print(linha)
                QMessageBox.about(tela3,'Resultado', linha)
        
                #brindo frame depois de pesquisar
                tela3.frame_2.show()
                arquivo2 = open("C:\\Users\\Admin\\Documents\\Projetos Github\\sistema-de-cadastro-python\\duastelasteste2.txt", "r")
                contador = 0
                for linha in arquivo2:
                    linha = linha.rstrip()
                    if pnome in linha:
                        contador = contador + 1
                        print(linha)

                        tela3.label_2.setText('\n' + linha)

                arquivo2.close()

                #LIMPANDO CAIXA DE TEXTO
                tela3.pnome.setText('')
                
        #printando quantos nomes foram encontrados           
        contador = (str(contador))
        QMessageBox.about(tela3,'Resultado', 'NOMES ENCONTRADOS: ' + contador)

        arquivo.close()

#Abrindo Tela 4
def funcao_editar():
    tela4.show()
    print('teste5')

#Editando arquivo texto2 com text replace    
def funcao_concluir_edicao():
    print('teste7')
    novnome = tela4.novonome.text()
    datadia = tela4.datadia.text()
    datames = tela4.datames.text()
    dataano = tela4.dataano.text()
    novvalorreal = tela4.novovalorreal.text()
    novvalorcentavos = tela4.novovalorcentavo.text()
   
    if novnome == '' and novvalorreal == '' and novvalorcentavos == '' and datadia == '' and datames == '' and dataano == '':
        print('Erro!')
        #QMessageBox.about(tela4,'Resultado', 'ERRO!')
    else:
        editarquivo = open('C:\\Users\\Admin\\Documents\\Projetos Github\\sistema-de-cadastro-python\\duastelasteste2.txt', 'r')

        contador = 0
        for linha in editarquivo:
            linha = linha.rstrip()
            if novnome in linha:
                contador = contador + 1
                print(linha)

                def replacetext(search_text, replace_text):
                    file = Path(r'duastelasteste2.txt')

                    data = file.read_text()

                    data = data.replace(search_text, replace_text)

                    file.write_text(data)

                    return 'Text replaced'

                search_text = (linha)

                replace_text = ('NOME: ' + novnome + ' ' + 'DÉBITO: R$ ' + novvalorreal + ',' + novvalorcentavos)

                print(replacetext(search_text, replace_text))
                #QMessageBox.about(tela4,'Resultado', 'NOME: ' + novnome + '\n' + 'NOVO VALOR: ' + novvalor + '\n' + 'EDIÇÃO CONCLUIDA!')


#Editando o arquivo texto1 com text replace
def funcao_concluir_edicao2():
    print('teste8')
    novnome = tela4.novonome.text()
    datadia = tela4.datadia.text()
    datames = tela4.datames.text()
    dataano = tela4.dataano.text()
    novvalorreal = tela4.novovalorreal.text()
    novvalorcentavos = tela4.novovalorcentavo.text()
    
    if novnome == '' and novvalorreal == '' and novvalorcentavos == '' and datadia == '' and datames == '' and dataano == '':
        print('Erro!')
        QMessageBox.about(tela4,'Resultado', 'ERRO!')
    else:
        editarquivo = open('C:\\Users\\Admin\\Documents\\Projetos Github\\sistema-de-cadastro-python\\duastelasteste.txt', 'r')
        
        tela4.novonome.setText('')
        tela4.datadia.setText('')
        tela4.datames.setText('')
        tela4.dataano.setText('')
        tela4.novovalorreal.setText('')
        tela4.novovalorcentavo.setText('')
        
        contador = 0
        for linha in editarquivo:
            linha = linha.rstrip()
            if novnome in linha:
                contador = contador + 1
                print(linha)

                def replacetext(search_text, replace_text):
                    file = Path(r'duastelasteste.txt')

                    data = file.read_text()

                    data = data.replace(search_text, replace_text)

                    file.write_text(data)

                    return 'Text replaced'

                search_text = (linha)

                replace_text = ('NOME: ' + novnome + ' ' + 'DATA: ' + datadia +'/'+ datames +'/'+ dataano)

                print(replacetext(search_text, replace_text))
                QMessageBox.about(tela4,'Resultado', 'NOME: ' + novnome + '\n' + 'NOVO VALOR: ' + novvalorreal +','+novvalorcentavos + '\n' + 'DATA: ' + datadia +'/'+ datames +'/'+ dataano +'\n' + 'EDIÇÃO CONCLUIDA!')

#Fechando o frame 2 da tela 3
def funcao_secundaria3():
    print('teste6')
    tela3.frame_2.close()

#Abrindo a tela 5
def funcao_exluir():
    tela5.show()
    print('teste9')

#Excluindo o nome do arquivo texto2
def funcao_excluir2():
    confirmenome = tela5.confirmanome.text()
    print('teste10')

    if confirmenome == '':
        print('Erro!')
        #QMessageBox.about(tela5,'Resultado', 'ERRO!')

    else:
        print('Acerto!')
        excluirarquivo = open('C:\\Users\\Admin\\Documents\\Projetos Github\\sistema-de-cadastro-python\\duastelasteste2.txt', 'r')

        contador = 0
        for linha in excluirarquivo:
            linha = linha.rstrip()
            if confirmenome in linha:
                contador = contador + 1
                print(linha)

                def replacetext(search_text, replace_text):
                    file = Path(r'duastelasteste2.txt')

                    data = file.read_text()

                    data = data.replace(search_text, replace_text)

                    file.write_text(data)

                    return 'Text replaced'

                search_text = (linha)

                replace_text = ('')

                print(replacetext(search_text, replace_text))
                #QMessageBox.about(tela4,'Resultado', 'NOME EXCLUÍDO COM SUCESSO!')

#Excluindo o nome do arquivo texto1
def funcao_excluir3():
    confirmenome = tela5.confirmanome.text()
    print('teste11')

    if confirmenome == '':
        print('Erro!')
        QMessageBox.about(tela5,'Resultado', 'ERRO!')

    else:
        excluirarquivo = open('C:\\Users\\Admin\\Documents\\Projetos Github\\sistema-de-cadastro-python\\duastelasteste.txt', 'r')

        tela5.confirmanome.setText('')
        
        contador = 0
        for linha in excluirarquivo:
            linha = linha.rstrip()
            if confirmenome in linha:
                contador = contador + 1
                print(linha)

                def replacetext(search_text, replace_text):
                    file = Path(r'duastelasteste.txt')

                    data = file.read_text()

                    data = data.replace(search_text, replace_text)

                    file.write_text(data)

                    return 'Text replaced'

                search_text = (linha)

                replace_text = ('')

                print(replacetext(search_text, replace_text))
                QMessageBox.about(tela4,'Resultado', 'NOME EXCLUÍDO COM SUCESSO!')

#Base do codigo com botões e chamada de telas
app=QtWidgets.QApplication([])
tela1=uic.loadUi('tela1.ui')
tela2=uic.loadUi('tela2.ui')
tela3=uic.loadUi('tela3.ui')
tela4=uic.loadUi('tela4.ui')
tela5=uic.loadUi('tela5.ui')
tela1.pushButton.clicked.connect(funcao_principal)
tela1.pushButton_2.clicked.connect(funcao_principal2)
tela2.pushButton.clicked.connect(funcao_secundaria)
tela3.pushButton.clicked.connect(funcao_secundaria2)
tela3.pushButton_4.clicked.connect(funcao_secundaria3)
tela3.pushButton_2.clicked.connect(funcao_editar)
tela3.pushButton_3.clicked.connect(funcao_exluir)
tela5.pushButton.clicked.connect(funcao_excluir2)
tela5.pushButton.clicked.connect(funcao_excluir3)
tela4.pushButton.clicked.connect(funcao_concluir_edicao)
tela4.pushButton.clicked.connect(funcao_concluir_edicao2)

#Abrindo a tela1
tela1.show()
#execultando o APP
app.exec()

#Criado por: Plínio Ramos, email: plinio206@live.com, Linkedn: https://www.linkedin.com/in/pl%C3%ADnio-ramos-3a1543229/