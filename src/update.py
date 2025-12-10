import psycopg2
from suppliers.src.config import  load_config

def update_vendor(vendor_id, vendor_name):
    """ Cập nhật tên của một vendor dựa trên ID """

    sql = """UPDATE vendors
              SET vendor_name = %s
              WHERE vendor_id = %s"""

    updated_rows = 0
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (vendor_name, vendor_id))

                updated_rows = cur.rowcount

                conn.commit()
    except (psycopg2.DatabaseError, Exception) as e:
        print(e)

    return (updated_rows)

if __name__ == '__main__':
    count = update_vendor(1, "3M Corp")

    if count > 0:
        print(f"Thành công! Đã cập nhật {count} dòng.")
    else:
        print(f"Cập nhật thất bại.")