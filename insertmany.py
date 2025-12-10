import psycopg2
from psycopg2 import extras  # Phải import thêm cái này
from config import load_config


def insert_many_vendors(vendor_list):
    # Câu lệnh SQL đặc biệt hơn một chút
    # %s ở đây đại diện cho CẢ MỘT DÒNG dữ liệu (không phải từng ô)
    sql = "INSERT INTO vendors(vendor_name) VALUES %s RETURNING vendor_id;"

    config = load_config()
    ids = []

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Quan trọng: Thêm tham số fetch=True
                # Hàm này sẽ trả về ngay một list chứa TẤT CẢ kết quả đã gộp lại
                results = extras.execute_values(
                    cur,
                    sql,
                    vendor_list,
                    page_size=100,
                    fetch=True
                )

                # results lúc này là: [(1,), (2,), (3,), ...]
                for row in results:
                    ids.append(row[0])

                conn.commit()
                print(f"Đã thêm thành công và lấy về được {len(ids)} IDs.")

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return ids

if __name__ == '__main__':
    # Danh sách cần thêm
    data = [
        ('AKM Semiconductor Inc.',),
        ('Asahi Glass Co Ltd.',),
        ('Daikin Industries Ltd.',),
        ('Dynacast International Inc.',),
        ('Foster Electric Co. Ltd.',),
        ('Murata Manufacturing Co. Ltd.',)
    ]

    vendor_ids = insert_many_vendors(data)
    print("Danh sách ID vừa tạo:", vendor_ids)