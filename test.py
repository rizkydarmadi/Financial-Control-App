# from repository import Repository
# from termcolor import colored
# data = Repository.get(limit=10)

# print(colored(f"""| {'TANGGAL'.ljust(20)} | {'DEBIT'.ljust(20)} | {'CREDIT'.ljust(20)}  | {'SALDO'.ljust(20)} | {'KETERANGAN'.ljust(50)} {'|'.ljust(0)}""",'white','on_grey',attrs=["bold"]))
# for i in data:
#     print(colored(f"""| {i.date.strftime("%m-%d-%Y %H:%M:%S").ljust(20)} | {str(i.debit).ljust(20)} | {str(i.credit).ljust(20)}  | {str(i.saldo).ljust(20)} | {str(i.deskripsi).ljust(50)} {'|'.ljust(0)}""",'green','on_grey',attrs=["bold"])if i.credit != None else colored(f"""| {i.date.strftime("%m-%d-%Y %H:%M:%S").ljust(20)} | {str(i.debit).ljust(20)} | {str(i.credit).ljust(20)}  | {str(i.saldo).ljust(20)} | {str(i.deskripsi).ljust(50)} {'|'.ljust(0)}""",'red','on_grey'))

# total_saldo = 12000000
# total_credit = sum([i.credit if i.credit else 0 for i in data])
# total_debit = sum([i.debit if i.debit else 0 for i in data])



# print(colored(f"""| {'TOTAL'.ljust(20)} | {str(total_debit).ljust(20)} | {str(total_credit).ljust(20)}  | {str(total_saldo).ljust(20)} | {'IS BALANCE'.ljust(50)} {'|'.ljust(0)}""",'cyan','on_grey')if (total_credit+total_debit) == total_saldo else colored(f"""| {'BALANCE'.ljust(20)} | {str(total_debit).ljust(20)} | {str(total_credit).ljust(20)}  | {str(total_saldo).ljust(20)} | {'NOT BALANCE (PLEASE CHECK YOUR TRANSACTION)'.ljust(50)} {'|'.ljust(0)}""",'white','on_red') )

while True:
    data = input('enter you name')

    match data:
        case 'loop':
            print('loop')
        case 'br':
            break
