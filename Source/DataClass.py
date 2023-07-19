import sqlite3


class DataClass:
    def __init__(self):
        super().__init__()
        self.conn = None
        self.cur = None

    def connect_db(self):
        self.conn = sqlite3.connect('../Data/data.db')
        self.cur = self.conn.cursor()

    def close_db(self):
        # self.conn.commit()
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
            
            
            """,
        }

        self.cur(create_table_query)
        self.close_db()

    def insert_data_in_table(self, table):
        """특정 테이블에 데이터를 삽입합니다."""
        pass


if __name__ == '__main__':
    pass
