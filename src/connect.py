import psycopg2
from config import load_config

def connect(config):
    try:
        # **config là cú pháp đặc biệt, bao gồm các nội dung kết nối trong file ini
        # Thay vì viết dài dòng: connect(host='localhost', user='postgres'...)
        # Python tự hiểu là lấy key trong file làm tên tham số
        with psycopg2.connect(**config) as conn:
            print('Connected to the PostgreSQL server.')\
            # Trả về cái "chìa khóa" (conn) để các hàm khác dùng (như tạo bảng, thêm dữ liệu...).
            return conn
    except (psycopg2.DatabaseError, Exception) as e:
        print(e)

if __name__ == "__main__":
    config = load_config()
    connect(config)