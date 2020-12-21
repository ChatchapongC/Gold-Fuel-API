import sys
import pymysql as mysql

from flask import abort
from config import OPENAPI_AUTOGEN_DIR, DB_HOST, DB_USER, DB_PASSWD, DB_NAME


sys.path.append(OPENAPI_AUTOGEN_DIR)
from openapi_server import models



def db_cursor():
    return mysql.connect(host=DB_HOST,user=DB_USER,passwd=DB_PASSWD,db=DB_NAME).cursor()

def get_gold_price():
    with db_cursor() as cs:
        cs.execute("SELECT month,times,price FROM gold")
        months = ['Jan','Feb','Mar','Apr','May','Jun',
                  'Jul','Aug','Sep','Oct','Nov','Dec']
        result = [
                models.Gold(months[month-1],month,times,round(price,2))
                for month,times,price in cs.fetchall()
            ]
        return result

def get_gold_price_in_month(monthId):
    with db_cursor() as cs:
        cs.execute("""
            SELECT month, times, price
            FROM gold
            WHERE month = %s
            """, [monthId])
        months = ['Jan','Feb','Mar','Apr','May','Jun',
                  'Jul','Aug','Sep','Oct','Nov','Dec']
        result = [
                models.Gold(months[month-1],month,times,round(amount,2))
                for month,times,amount in cs.fetchall()
            ]
        return result
        
def get_average_gold_price(monthId):
    with db_cursor() as cs:
        cs.execute("""
            SELECT month, AVG(price)
            FROM gold
            WHERE month = %s
            """, [monthId])

        months = ['Jan','Feb','Mar','Apr','May','Jun',
                  'Jul','Aug','Sep','Oct','Nov','Dec']
        result = cs.fetchone()
    if result:
        month = result[0]
        price = round(result[1],2)
        return models.GoldAverage(month, months[month-1], price)
    else:
        abort(404)

def get_average_monthly_gold_price():
    with db_cursor() as cs:
        cs.execute("""
            SELECT month, AVG(price)
            FROM gold
            GROUP BY month
            """)
        months = ['Jan','Feb','Mar','Apr','May','Jun',
                  'Jul','Aug','Sep','Oct','Nov','Dec']
        result = [
                models.GoldAverage(months[month-1],month,round(amount,2))
                for month,amount in cs.fetchall()
            ]
        return result

def get_highest_gold_price():
    with db_cursor() as cs:
        cs.execute("""
            SELECT month, price
            FROM gold
            ORDER BY price DESC
            LIMIT 1
            """)
        months = ['Jan','Feb','Mar','Apr','May','Jun',
                  'Jul','Aug','Sep','Oct','Nov','Dec']
        result = [
                models.Gold(months[month-1],month,round(amount,2))
                for month,amount in cs.fetchall()
            ]
        return result

def get_lowest_gold_price():
    with db_cursor() as cs:
        cs.execute("""
            SELECT month, price
            FROM gold
            ORDER BY price 
            LIMIT 1
            """)
        months = ['Jan','Feb','Mar','Apr','May','Jun',
                  'Jul','Aug','Sep','Oct','Nov','Dec']
        result = [
                models.Gold(months[month-1],month,round(amount,2))
                for month,amount in cs.fetchall()
            ]
        return result

def get_fuel():
    with db_cursor() as cs:
        cs.execute("""
            SELECT fp.fuel_id, f.fuel
            FROM fuel_price fp
            INNER JOIN fuel f ON fp.fuel_id = f.ID
            GROUP BY f.ID
        """)
        result = [
                models.Fuel(fuelId,fname)
                for fuelId,fname in cs.fetchall()
            ]
        return result

def get_all_fuel_price():
    with db_cursor() as cs:
        cs.execute("""
            SELECT fuel, month, day, price
            FROM fuel_price fp
            INNER JOIN fuel f ON f.ID = fp.fuel_id
            """)
        months = ['Jan','Feb','Mar','Apr','May','Jun',
                  'Jul','Aug','Sep','Oct','Nov','Dec']
        result = [
                models.FuelPrice(fname,month,months[month-1],day,round(price,2))
                for fname,month,day,price in cs.fetchall()
                ]
        return result

def get_fuel_price(fuelId):
    with db_cursor() as cs:
        cs.execute("""
            SELECT fuel, month, day, price
            FROM fuel_price fp
            INNER JOIN fuel f ON f.ID = fp.fuel_id
            WHERE fp.fuel_id=%s 
            ORDER BY month
            """,[fuelId])
        months = ['Jan','Feb','Mar','Apr','May','Jun',
                  'Jul','Aug','Sep','Oct','Nov','Dec']
        result = [
                models.FuelPrice(fname,month,months[month-1],day,round(price,2))
                for fname,month,day,price in cs.fetchall()
                ]
        return result

def get_fuel_price_by_month(monthId):
    with db_cursor() as cs:
        cs.execute("""
            SELECT fuel_id,fuel, month, day, price
            FROM fuel_price fp
            INNER JOIN fuel f ON f.ID = fp.fuel_id
            WHERE month=%s 
            """,[monthId])
        months = ['Jan','Feb','Mar','Apr','May','Jun',
                  'Jul','Aug','Sep','Oct','Nov','Dec']
        result = [
                models.FuelDetail(fuelID,fname,month,months[month-1],day,round(price,2))
                for fuelID,fname,month,day,price in cs.fetchall()
                ]
        return result

def get_monthly_average_fuel_price(fuelId):
    with db_cursor() as cs:
        cs.execute("""
            SELECT fuel,month, AVG(price)
            FROM fuel_price fp
            INNER JOIN fuel f ON f.ID = fp.fuel_id
            WHERE fp.fuel_id = %s
            GROUP BY month 
            ORDER BY month 
            """,[fuelId])
        months = ['Jan','Feb','Mar','Apr','May','Jun',
                  'Jul','Aug','Sep','Oct','Nov','Dec']

        result = [
                models.FuelMonthlyAverage(fuel,months[month-1],month,round(price,2))
                for fuel,month,price in cs.fetchall()
            ]
        return result

def get_fuel_changing():
    with db_cursor() as cs:
        cs.execute("""
            SELECT COUNT(price) as changing 
            FROM fuel_price
            WHERE fuel_id = 2
        """)
        result = cs.fetchone()
    if result: 
        value = result[0]
        return value
    else:
        abort(404)

