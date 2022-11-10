from model import Session,Finance
from sqlalchemy import Select
from utils import dateUtil
from datetime import datetime

class Repository:
    @staticmethod
    def get(limit:int=None,stardate:str=None,enddate:str=None,terms:str=None):
        with Session() as session:
            stmt = Select(Finance).order_by(Finance.date.desc())

            if (stardate and enddate) != None:
                stmt = stmt.filter(Finance.date >= stardate,Finance.date <= enddate)
            else:
                d = dateUtil()
                stardate = d.get_first_day_of_month()
                enddate = d.get_last_day_of_month()
                stmt = stmt.filter(Finance.date >= stardate,Finance.date <= enddate)
            
            if terms != None:
                stmt = stmt.filter(Finance.deskripsi.like(f'%{terms}%'))
            
            if limit != None:
                stmt = stmt.limit(limit=limit)
            
            data = session.execute(stmt).scalars().all()
        return data
    
    @staticmethod
    def add(amount:int=None,deskripsi:str=None):
        with Session() as session:
            # get last saldo
            stmt = Select(Finance).order_by(Finance.date.desc())
            data = session.execute(stmt).scalar()
            if data != None:
                last_saldo = data.saldo
            else:
                last_saldo = 0

            new_data = Finance(
                saldo = last_saldo + amount,
                credit = amount,
                deskripsi = deskripsi,
                date = datetime.now()
            )
            session.add(new_data)
            session.commit()
    
    @staticmethod
    def min(amount:int=None,deskripsi:str=None):
        with Session() as session:
            # get last saldo
            stmt = Select(Finance).order_by(Finance.date.desc())
            data = session.execute(stmt).scalar()

            new_data = Finance(
                saldo = data.saldo - amount,
                debit = amount,
                deskripsi = deskripsi,
                date = datetime.now()
            )
            session.add(new_data)
            session.commit()
    
    @staticmethod
    def update(id:int,amount:int=None,deskripsi:str=None):
        with Session() as session:
            # get last saldo
            stmt = Select(Finance).where(Finance.id==id)
            data = session.execute(stmt).scalar()

            before_stmt = Select(Finance).where(Finance.id<id).order_by(Finance.id.desc())
            before_ = session.execute(before_stmt).scalar()
            last_saldo = before_.saldo if before_ else 0
            now_saldo = data.saldo

            if data.credit != None:
                data.credit = amount
                data.deskripsi = deskripsi
                data.saldo = last_saldo + amount

            else:
                data.debit = amount
                data.deskripsi = deskripsi
                data.saldo = last_saldo - amount

            session.commit()
            
            gap = data.saldo - now_saldo
            after_stmt = Select(Finance).where(Finance.id>id).order_by(Finance.id.desc())
            after_ = session.execute(after_stmt).scalars().all()

            for i in after_:
                i.saldo += gap
                session.commit()
    
    staticmethod
    def delete(id:int):
        with Session() as session:
            # get now saldo
            stmt = Select(Finance).where(Finance.id==id)
            data = session.execute(stmt).scalar()

            credit = data.credit
            debit = data.debit

            session.delete(data)
            session.commit()

            after_stmt = Select(Finance).where(Finance.id>id).order_by(Finance.id.desc())
            after_ = session.execute(after_stmt).scalars().all()

            if credit != None:
                for i in after_:
                    if i.saldo == None:
                        i.saldo = 0
                    i.saldo = i.saldo - credit
                    session.commit()
            else:
                for i in after_:
                    if i.saldo == None:
                        i.saldo = 0
                    i.saldo = i.saldo + debit
                    session.commit()












