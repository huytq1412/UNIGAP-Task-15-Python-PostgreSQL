import psycopg2
from config import load_config

def get_parts(vendor_id):
    parts = []
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.callproc('get_parts_by_vendor', (vendor_id,))

                # Kiểu xử lý lặp qua từng dòng
                row = cur.fetchone()
                while row is not None:
                    parts.append(row)
                    row = cur.fetchone()

                # Kiểu xử lý lấy tất cả
                parts = cur.fetchall()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return parts

if __name__ == '__main__':
    parts = get_parts(1)
    print(parts)
