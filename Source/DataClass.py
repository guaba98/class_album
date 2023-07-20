import sqlite3
import pandas as pd


class DataClass:
    def __init__(self):
        super().__init__()
        self.conn = None
        self.cur = None

        # self.return_df('TB_NOTICE_BOARD')

    def connect_db(self):
        # self.conn = sqlite3.connect('../Data/data.db')
        self.conn = sqlite3.connect("C:\\Users\\KDT103\\Desktop\\coding\\0. 프로젝트\\개인프로젝트\\class_album\\Data\\data.db")
        self.cur = self.conn.cursor()

    def close_db(self):
        self.conn.close()

    def create_table(self):
        """여기에서 테이블을 생성합니다."""
        self.connect_db()
        create_table_query = {
            'TB_USER': """
            CREATE TABLE TB_USER (
            USER_NO INTEGER PRIMARY KEY,
            USER_NAME TEXT NOT NULL,
            USER_EMAIL TEXT NOT NULL,
            USER_PW TEXT NOT NULL,
            USER_NM TEXT NOT NULL,
            USER_CREATE_DATE NOT NULL );""",

            'TB_LOG': """
            CREATE TABLE TB_LOG(
            USER_EMAIL TEXT NOT NULL,
            USER_NM TEXT NOT NULL,
            USER_LOGIN_TIME TEXT NOT NULL);""",

            'TB_NOTICE_BOARD': """
            CREATE TABLE TB_NOTICE_BOARD(
            BOARD_ID INTEGER PRIMARY KEY AUTO_INCREMENT, 
            USER_EMAIL text,
            USER_NAME text,
            BOARD_TITLE text,
            BOARD_CONTENTS text,
            BOARD_IMG text,
            WRITE_TIME datetime,
            BOARD_READ int,
            UPDATE_TIME datetime,
            DELETE_TIME datetime
            );""",
        }

        self.cur.execute(create_table_query['TB_NOTICE_BOARD'])
        self.close_db()

    def insert_data_in_table(self, table):
        """특정 테이블에 데이터를 삽입합니다."""
        pass

    def return_df(self, table_name):
        """데이터프레임을 리턴합니다."""
        # self.conn = sqlite3.connect("C:\\Users\\KDT103\\Desktop\\coding\\0. 프로젝트\\개인프로젝트\\class_album\\Data\\data.db") # 노트북 경로
        # self.cur = self.conn.cursor()
        self.connect_db()
        query = f'SELECT * FROM {table_name}'
        df = pd.read_sql(query, self.conn)
        return df

    def return_specific_data(self, table_name, column, conditon):
        """특정 열 데이터만 반환합니다."""
        self.connect_db()
        query = f'SELECT {column} FROM {table_name}'
        if conditon is not None:
            query += ' WHERE ' + conditon

        r_data = pd.read_sql(query, self.conn)
        specific_data = r_data.values[0][0]
        return specific_data

    def check_login(self, id, pw):
        """로그인 데이터를 확인해서 데이터가 있는지 확인합니다."""
        self.connect_db()
        query = f"SELECT * FROM TB_USER WHERE USER_EMAIL = '{id}' AND USER_PW = '{pw}'"
        print('[dataclass] 쿼리확인: ', query)
        df = pd.read_sql(query, self.conn)
        if len(df) > 0:
            name = df['USER_NAME'].values[0]
            return name
        else:
            return False


    # def login(self, data: ReqLogin) -> PerLogin:
    #     print("[ login ]")
    #     """클라이언트 로그인 요청 -> 서버 로그인 허가 """
    #     result: PerLogin = PerLogin(rescode=2, user_id_=data.id_)
    #     sql = f"SELECT * FROM TB_USER WHERE USER_ID = '{data.id_}' AND USER_PW = '{data.password}'"
    #     print(sql)
    #     df = pd.read_sql(sql, self.conn)
    #     row = len(df)
    #     print("row", row)
    #
    #     if row in [None, 0]:
    #         result.rescode = 0
    #     # 입력한 아이디와 비밀번호, db에서 가진 아이디와 비밀번호
    #     # elif data.id_ != row[1] or data.password != row[2]:
    #     #     result.rescode = 1
    #     else:
    #         result.rescode = 2
    #     return result
if __name__ == '__main__':
    # d = DataClass()
    # c_ = "BOARD_TITLE = '야너두할수있어'"
    # result = d.return_specific_data(table_name='TB_NOTICE_BOARD',
    #                        column='BOARD_CONTENTS',
    #                        conditon=c_)
    # # print(result.values[0][0])
    # print(result.values[0][0])
    pass
