import psycopg2
from suppliers.src.config import load_config

def insert_vendor(vendor_name):
    # Bình thường: "INSERT ... VALUES (...)" -> Chạy xong là im lặng, không trả về gì.
    # Thêm "RETURNING vendor_id": -> Chạy xong, trả cái ID vừa tạo ra đây cho tôi.
    sql = "INSERT INTO vendors(vendor_name) VALUES(%s) RETURNING vendor_id;"

    config = load_config()
    vendor_id = None

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Python gửi lệnh sang DB. DB tạo dòng mới, tự tăng ID lên (ví dụ là 10).
                # Nhờ câu RETURNING, DB gửi ngược số 10 về cho Python.
                # Lúc này số 10 đang nằm tạm trong bộ nhớ của con trỏ (cur).
                cur.execute(sql, (vendor_name,))

                # cur.fetchone(): Lấy dòng kết quả đầu tiên từ bộ nhớ ra.
                # Kết quả luôn luôn là một Tuple (bộ dữ liệu), ví dụ: (10, )
                row = cur.fetchone()

                # Vì biến 'row' đang là: (10, )
                # Muốn lấy số 10 để dùng, ta phải móc phần tử đầu tiên ra: row[0]
                if row:
                    vendor_id = row[0]

                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return vendor_id

if __name__ == '__main__':
    insert_vendor("3M Co.")