import psycopg2
from psycopg2 import extras
from suppliers.src.config import load_config


def bulk_update_vendors(update_data):
    """
    update_data là list các tuple: [(id_1, new_name_1), (id_2, new_name_2), ...]
    Lưu ý: Tôi để ID lên trước cho dễ nhìn, nhưng thực ra thứ tự do bạn quy định trong SQL.
    """

    # --- CÂU LỆNH SQL THẦN THÁNH ---
    # 1. UPDATE vendors AS v: Định danh bảng chính là v
    # 2. SET vendor_name = data.new_name: Lấy tên từ bảng tạm 'data' đắp vào
    # 3. FROM (VALUES %s): Chỗ này execute_values sẽ điền cả nghìn dòng vào đây
    # 4. AS data (id, new_name): Đặt tên cho bảng tạm là 'data' có 2 cột
    # 5. WHERE v.vendor_id = data.id: Điều kiện để khớp đúng ông nào sửa ông đó

    sql = """
        UPDATE vendors AS v
        SET vendor_name = data.new_name
        FROM (VALUES %s) AS data (vendor_id, new_name) 
        WHERE v.vendor_id = data.vendor_id
    """

    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Dùng execute_values y hệt như lúc Insert
                extras.execute_values(
                    cur,
                    sql,
                    update_data,
                    template=None,
                    page_size=1000
                )

                conn.commit()
                print(f"Đã Update siêu tốc {cur.rowcount} dòng!")

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


if __name__ == '__main__':
    # Tạo dữ liệu giả lập: [(ID, Tên Mới)]
    # Lưu ý: ID phải là Integer, Tên là String
    data = [
        (1, 'Vendor 1 Updated by Bulk'),
        (2, 'Vendor 2 Updated by Bulk'),
        (55, 'Asus Updated by Bulk')
    ]

    bulk_update_vendors(data)