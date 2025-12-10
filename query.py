import psycopg2
from config import  load_config

def get_vendors_one(vendor_id):
    sql = "SELECT vendor_id, vendor_name FROM vendors WHERE vendor_id = %s"
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (vendor_id,))
                row = cur.fetchone()

                if row is not None:
                    print(f"Tìm thấy: ID={row[0]}, Name={row[1]}")
                    print(row)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def get_vendors_all():
    sql = "SELECT vendor_id, vendor_name FROM vendors"
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                rows = cur.fetchall()

                print(f"Tổng số vendor: {cur.rowcount}")
                for row in rows:
                    print(row)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def get_vendors_batch(batch_size=5):
    sql = "SELECT vendor_id, vendor_name FROM vendors"
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql)

                while True:
                    # Lấy 5 dòng một lần
                    rows = cur.fetchmany(batch_size)

                    if not rows:
                        break  # Hết dữ liệu thì dừng

                    print(f"Đang xử lý lô {batch_size} dòng")
                    for row in rows:
                        print(row)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    print(f"--- Query xử lý 1 dòng---")
    get_vendors_one(1)

    print(f"--- Query xử lý all ---")
    get_vendors_all()

    print(f"--- Query xử lý theo lô ---")
    get_vendors_batch()

