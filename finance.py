class Finance:

    def __init__(self,nama,saldo) -> None:
        self.nama = nama
        self.saldo = saldo
    
    def debt(self,amount) -> None:
        first_saldo = self.saldo
        self.saldo -= amount
        print(f'{self.saldo}')

    def credit(self,amount) -> None:
        self.saldo += amount
        print(self.saldo)
    
    def my_saldo(self):
        print(f'{self.saldo}')
