from database.DB_connect import DBConnect
from model.team import Team
from model.salario import Salario

class DAO:
    @staticmethod
    def query_esempio():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query= """ SELECT * FROM esempio """

        cursor.execute(query)

        for row in cursor:
            result.append(row)

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_team(year):

        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query= """ SELECT * 
                    FROM team
                    WHERE year = %s """
        cursor.execute(query, (year,))
        for row in cursor:
            team = Team(row["id"], row["team_code"], row["name"])
            result.append(team)

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_years_from_1980():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT DISTINCT year FROM team
                 WHERE year >= 1980
                  ORDER BY year """
        cursor.execute(query)
        for row in cursor:
            years = row["year"]
            result.append(years)


        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_all_coppie(year):
        conn = DBConnect.get_connection()
        result = []

        cursor = conn.cursor(dictionary=True)
        query ="""SELECT t1.id AS id1, t2.id AS id2
                    FROM team t1, team t2
                    WHERE t1.id < t2.id  AND t1.year = t2.year AND t1.year = %s
                    GROUP BY t1.id, t2.id"""

        cursor.execute(query,(year,))

        for row in cursor:
            coppie = row["id1"], row["id2"]
            result.append(coppie)

        cursor.close()
        conn.close()
        return result

    def calcola_salario_per_anno(year):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ SELECT team_id, SUM(salary) AS total
                         FROM salary
                         WHERE year =%s 
                         GROUP BY team_id"""
        #for row in cursor:
            #salario = Salario(row["team_id"], row["total"])
            #result.append(salario)
        cursor.execute(query,(year,))

        result = {} # dizionario {teamID: totale_salari}
        for row in cursor:
            result[row["team_id"]] = row["total"]
        cursor.close()
        conn.close()
        return result


