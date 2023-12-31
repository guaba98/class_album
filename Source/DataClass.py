import sqlite3
import pandas as pd
from datetime import datetime


class DataClass:
    def __init__(self):
        super().__init__()
        self.conn = None
        self.cur = None

        '''
        노트북 절대경로: "self.conn = sqlite3.connect("C:\\Users\\thdus\\PycharmProjects\\class_album\\Data\\data.db"
        개발원 절대경로: "C:\\Users\\KDT103\\Desktop\\coding\\0. 프로젝트\\개인프로젝트\\class_album\\Data\\data.db" 
        '''

    def connect_db(self):
        self.conn = sqlite3.connect("C:\\Users\\KDT103\\Desktop\\coding\\0. 프로젝트\\개인프로젝트\\class_album\\Data\\data.db") # 실습실 경로
        # self.conn = sqlite3.connect(
            # "C:\\Users\\KDT103\\Desktop\\coding\\0. 프로젝트\\개인프로젝트\\class_album\\Data\\data.db")  # 노트북 경로
        # self.conn = sqlite3.connect("C:\\Users\\thdus\\PycharmProjects\\class_album\\Data\\data.db")
        self.cur = self.conn.cursor()

    def close_db(self):
        self.conn.close()

    def commit_db(self):
        self.conn.commit()

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

    def check_user_email(self, email):
        """이메일이 존재하면 True값 반환"""
        self.connect_db()
        query = f'SELECT COUNT(*) FROM TB_USER WHERE USER_EMAIL = ?'
        self.cur.execute(query, (email,))
        result = self.cur.fetchone()[0]
        print('[dataclass.py] 결과값 확인', result, result > 0)
        self.close_db()

        return result > 0

    def return_datetime(self, type):
        """원하는 날짜/시간 포멧을 반환"""
        now = datetime.now()  # 시간
        if type == 'date':
            now_format = now.strftime("%Y-%m-%d")  # 년 월 일
        elif type == 'time':
            now_format = now.strftime("%Y-%m-%d %H:%M:%S")  # 년 월 일 시 분 초
        elif type == 'time_only':
            now_format = now.strftime("%H:%M:%S")  # 시 분 초

        # print('[dateimte.py]시간 포멧팅: ', now_format)
        return now_format

    def insert_user_info(self, user_nm, email, pw, rdate, user_num):
        """유저 정보 테이블에 회원정보를 기록합니다."""

        # db 연결
        self.connect_db()

        # 회원 정보 저장
        query = f"INSERT INTO TB_USER (USER_NAME, USER_EMAIL, USER_PW, USER_CREATE_DATE, USER_NUM) VALUES" \
                f"(?, ?, ?, ?, ?)"
        self.cur.execute(query, (user_nm, email, pw, rdate, user_num))

        # db 저장 및 닫기
        self.commit_db()
        self.close_db()

    def insert_user_commnets(self, title, user_name, commnets):
        """유저의 댓글을 저장함"""
        self.connect_db()
        # 1. 제목을 확인해서 board_id 확인하기'
        c = f"BOARD_TITLE = '{title}'"
        board_id = self.return_specific_data(table_name='TB_NOTICE_BOARD', column='BOARD_ID', conditon=c)
        print(board_id)
        user_email = self.return_user_email(user_name)
        c_time = self.return_datetime('time')

        query = f"INSERT INTO TB_COMMNET (BOARD_ID, USER_EMAIL, USER_NM, COMMNET, COMMENT_DATE, COMMENT_TYPE) VALUES" \
                f"(?, ?, ?, ?, ?, ?)"
        self.cur.execute(query, (board_id, user_email, user_name, commnets, c_time, 0))
        self.commit_db()
        self.close_db()

    def insert_user_log(self, email):
        """유저 접속기록을 삽입합니다."""

        # db 연결
        self.connect_db()

        # 조건
        c_ = f"USER_EMAIL = '{email}'"
        user_name = self.return_specific_data(table_name='TB_USER', column='USER_NAME', conditon=c_)  # 이름

        # 데이터 삽입
        query = f"INSERT OR IGNORE INTO TB_LOG (USER_EMAIL, USER_NM, USER_LOGIN_TIME) VALUES (?, ?, ?)"
        now_format = self.return_datetime('time')  # 현재 시간리턴
        print(email, user_name, now_format)

        self.cur.execute(query, (email, user_name, now_format))  # 유저 이메일, 이름, 접속시간 기록
        self.commit_db()  # 저장
        self.close_db()  # 닫아주기

    def return_user_email(self, name):
        """유저의 이름 확인해 이메일 반환"""
        self.connect_db()
        c_ = f"USER_NAME = '{name}'"
        user_email = self.return_specific_data(table_name='TB_USER', column='USER_EMAIL', conditon=c_)
        return user_email

    def return_user_name(self, email):
        """유저의 이메일 확인해 이름 반환"""
        self.connect_db()
        c_ = f"USER_EMAIL = '{email}'"
        user_name = self.return_specific_data(table_name='TB_USER', column='USER_NAME', conditon=c_)  # 이름
        return user_name

    def return_user_info(self, name_or_email):
        self.connect_db()
        condition = None
        column_to_return = None

        if '@' in name_or_email:  # Check if the input is an email
            condition = f"USER_EMAIL = '{name_or_email}'"
            column_to_return = 'USER_NAME'
        else:
            condition = f"USER_NAME = '{name_or_email}'"
            column_to_return = 'USER_EMAIL'

        user_info = self.return_specific_data(table_name='TB_USER', column=column_to_return, condition=condition)
        return user_info

    def insert_chat_log(self, name, chat):
        """채팅 기록 저장"""
        # db 연결
        self.connect_db()

        # 조건문 및 쿼리
        # c_ = f"USER_NAME = '{name}'"
        # user_email = self.return_specific_data(table_name='TB_USER', column='USER_EMAIL', conditon=c_)
        user_email = self.return_user_email(name)
        query = f"INSERT INTO TB_CHAT (USER_EMAIL, CHAT_TIME, CHAT_LOG) VALUES (?, ?, ?)"
        time_ = self.return_datetime('time')
        chat_ = chat[1]

        # 데이터 삽입(이메일, 시간, 채팅)
        self.cur.execute(query, (user_email, time_, chat_))

        # 데이터 저장 및 닫기
        self.commit_db()
        self.close_db()

    def insert_post_log(self, name, email, b_title, b_contents, time, img_path=None):
        """게시글 업로드 기록 저장"""
        self.connect_db()

        # 게시글 내용 저장
        query = f"INSERT INTO TB_NOTICE_BOARD (USER_EMAIL, USER_NAME, BOARD_TITLE," \
                f"BOARD_CONTENTS, BOARD_IMG, UPDATE_TIME) VALUES" \
                f"(?, ?, ?, ?, ?, ?)"
        self.cur.execute(query, (email, name, b_title, b_contents, img_path, time))

        # db 저장 및 닫기
        self.commit_db()
        self.close_db()
        query = f''

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

    def get_table_row_count(self, table_name):
        self.connect_db()

        # 특정 테이블의 행 개수 얻기
        sql_query = f"SELECT COUNT(*) FROM {table_name};"
        row_count = pd.read_sql_query(sql_query, self.conn)
        self.close_db()
        return row_count.iloc[0, 0]

    def check_login(self, id, pw):
        """로그인 데이터를 확인해서 데이터가 있는지 확인합니다."""
        self.connect_db()
        query = f"SELECT * FROM TB_USER WHERE USER_EMAIL = '{id}' AND USER_PW = '{pw}'"
        # print('[dataclass] 쿼리확인: ', query)
        df = pd.read_sql(query, self.conn)
        if len(df) > 0:
            name = df['USER_NAME'].values[0]
            return name
        else:
            return False



if __name__ == '__main__':
    # d = DataClass()
    # # c_ = "BOARD_TITLE = '야너두할수있어'"
    # # result = d.return_specific_data(table_name='TB_NOTICE_BOARD',
    # #                        column='BOARD_CONTENTS',
    # #                        conditon=c_)
    # # # print(result.values[0][0])
    # # print(result.values[0][0])
    # d.insert_user_info('소연', 'soyeon@soyeon.com', '1234', '2023-07-21', '111-111-1111')
    # # print(a)
    # d.insert_post_log('name', 'email', 'b_title', 'b_contents', 'time', 'img_path')
    # print(d.get_table_row_count('TB_USER'))

    pass
