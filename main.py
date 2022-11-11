from repository import Repository
from termcolor import colored
from utils import Curency

def income(amount: int, deskripsi: str):
    Repository.add(amount=amount, deskripsi=deskripsi)

def spending(amount: int,deskripsi: str):
    Repository.min(amount=amount,deskripsi=deskripsi)

def update(id:int,amount:int,deskripsi:str):
    Repository.update(id=id,amount=amount,deskripsi=deskripsi)

def delete(id:int):
    Repository.delete(id=id)

def show(s:str=None):
    try:
        data = data = Repository.get(terms=s)
        if data == []:
            return print('no data')
        print(colored(f"""| {'ID'.ljust(5)} | {'TANGGAL'.ljust(20)} | {'DEBIT'.ljust(20)} | {'CREDIT'.ljust(20)}  | {'SALDO'.ljust(20)} | {'KETERANGAN'.ljust(50)} {'|'.ljust(0)}""",'white','on_grey',attrs=["bold"]))
        for i in data:
            print(colored(f"""| {str(i.id).ljust(5)} | {i.date.strftime("%m-%d-%Y %H:%M:%S").ljust(20)} | {Curency.convert(i.debit).ljust(20)} | {Curency.convert(i.credit).ljust(20)}  | {Curency.convert(i.saldo).ljust(20)} | {str(i.deskripsi).ljust(50)} {'|'.ljust(0)}""",'green','on_grey',attrs=["bold"])if i.credit != None else colored(f"""| {str(i.id).ljust(5)} | {i.date.strftime("%m-%d-%Y %H:%M:%S").ljust(20)} | {Curency.convert(i.debit).ljust(20)} | {Curency.convert(i.credit).ljust(20)}  | {Curency.convert(i.saldo).ljust(20)} | {str(i.deskripsi).ljust(50)} {'|'.ljust(0)}""",'red','on_grey'))
        
        total_saldo = data[0].saldo
        total_credit = sum([i.credit if i.credit else 0 for i in data])
        total_debit = sum([i.debit if i.debit else 0 for i in data])

        print(colored(f"""| {'***'.ljust(5)} | {'TOTAL'.ljust(20)} | {Curency.convert(total_debit).ljust(20)} | {Curency.convert(total_credit).ljust(20)}  | {Curency.convert(total_saldo).ljust(20)} | {'IS BALANCE'.ljust(50)} {'|'.ljust(0)}""",'cyan','on_grey')if (total_credit-total_debit) == total_saldo else colored(f"""| {'***'.ljust(5)} | {'TOTAL'.ljust(20)} | {Curency.convert(total_debit).ljust(20)} | {Curency.convert(total_credit).ljust(20)}  | {Curency.convert(total_saldo).ljust(20)} | {'NOT BALANCE (PLEASE CHECK YOUR TRANSACTION)'.ljust(50)} {'|'.ljust(0)}""",'white','on_red') )
        
    except Exception as e:
        return print(e)

if __name__ == "__main__":
    print(colored(f"""| {'***'.ljust(5)} | {'i => INCOME'.ljust(20)} | {'o => SPENDING'.ljust(20)} | {'s => SHOW'.ljust(20)}  | {'x => EXIT'.ljust(20)} | u => UPDATE | d => DELETE | {'YOU MAKE ME HAPPY 🥲'.ljust(22)} {'|'.ljust(0)}""",'white','on_grey',attrs=["bold"]))
    while True:
        text = input()
        match text:
            case 'i':
                x = input('input your income = ')
                y = input('input description = ')
                income(amount=int(x),deskripsi=y)
                show()
            case 'o':
                x = input('input your spending = ')
                y = input('input description = ')
                spending(amount=int(x),deskripsi=y)
                show()
            case 's':
                show()
            case 'u':
                z = input('input id = ')
                x = input('input your amount = ')
                y = input('input description = ')
                update(id=z,amount=int(x),deskripsi=y)
                show()
            case 'd':
                x = input('input id = ')
                delete(id=int(x))
                show()
            case 'x':
                break
            case _:
                print('none above')
