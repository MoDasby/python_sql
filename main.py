import os
import sqlite3
import sys

db = sqlite3.connect('productsDB.db')

cursor = db.cursor()

def clear():
    os.system('clear')

def handleError(err):
    print(err)
    clear()
    input('enter to continue')
    sys.exit()

def createDatabase():
    cursor.execute(f'create table if not exists produtos(nome text, preco real)')

def insertProduct(name, price):
    try:
        cursor.execute(f'insert into produtos values("{name}", "{price}")')
        db.commit()
        print('atualizado com sucesso')
        init()
    except Exception as err:
        print(err)
        clear()
        input('enter to continue')
        handleError(err)

def init():
    clear()
    createDatabase()

    action = str(input('digite a ação que deseja fazer:\n\n1 - inserir um novo produto\n2 - atualizar um produto existente\n3 - Ver produtos existentes\n\n-> '))

    if action == '1':
        productName = input('digite o nome do produto -> ')
        productPrice = int(input('digite o preço do produto -> ')) 

        insertProduct(productName, productPrice)
    elif action == '2':
        try:
            cursor.execute('select * from produtos')
            
            rows = cursor.fetchall()

            for r in rows:
                print(f'Nome: {r[0]}\nPreço: {r[1]}\n\n')
                
            productNameToUpdate = str(input('Digite o nome do produto que deseja atualizar -> '))
        except Exception as err:
            handleError(err)

        updateAction = input('o que deseja atualizar?\n\n1 - nome\n2 - preço\n3 - tudo\n\n-> ')

        if updateAction == '1':
            productNewName = str(input('Digite o novo nome -> '))
            try:
                cursor.execute(f'update produtos set nome = "{productNewName}" where nome = "{productNameToUpdate}"')
                db.commit()
                print('dados atualizados!')
                init()
            except Exception as err:
                handleError(err)
        elif updateAction == '2':
            productNewPrice = float(input('Digite o novo preço -> '))
            try:
                cursor.execute(f'update produtos set preco = "{productNewPrice}" where nome = "{productNameToUpdate}"')
                db.commit()
                print('dados atualizados!')
                init()
            except Exception as err:
                handleError(err)
        elif updateAction == '3':
            productNewName = str(input('Digite o novo nome -> '))
            productNewPrice = float(input('Digite o novo preço -> '))
            try:
                cursor.execute(f'update produtos set nome = "{productNewName}" where nome = "{productNameToUpdate}"')
                cursor.execute(f'update produtos set preco = "{productNewPrice}" where nome = "{productNameToUpdate}"')
                db.commit()
            except Exception as err:
                handleError(err)
    
    elif action == '3':
        try:
            cursor.execute('select * from produtos')
            
            rows = cursor.fetchall()

            names = []
            prices = []
            table = 'Nome\t\tPreço\n\n'
            for r in rows:
                names.append(r[0])
                prices.append(r[1])

            for i in range(0, (len(names) -1)):
                table += f'{names[i]}\t\t{prices[i]}\n'
            
            print(table)
            input('aperte enter para continuar')
            init()
        except Exception as err:
            handleError(err)
init()