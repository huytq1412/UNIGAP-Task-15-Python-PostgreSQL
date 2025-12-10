from configparser import ConfigParser

def load_config(filename='database.ini', section='postgresql'):
    # Tạo một cái máy đọc (parser)
    parser = ConfigParser()

    # Đưa file 'database.ini' vào máy và bảo nó đọc đi.
    parser.read(filename)

    config = {}

    # Trong file ini có đoạn nào tên section là [postgresql] không?
    if parser.has_section(section):
        # Nếu có, hãy lôi hết đồ đạc trong mục đó ra (host, user, password...).
        # params lúc này là một danh sách các cặp, ví dụ: [('user', 'postgres'), ('password', '123456')]
        params = parser.items(section)

        # Vòng lặp: Nhặt từng món đồ bỏ vào dict config
        for param in params:
            # param[0] là tên món đồ (ví dụ: 'user')
            # param[1] là giá trị món đồ (ví dụ: 'postgres')
            # Dòng này nghĩa là: config['user'] = 'postgres's
            config[param[0]] = param[1]

    else:
        raise Exception('Không tìm thấy mục {0} trong file {1}'.format(section, filename))
    
    return config

if __name__ == "__main__":
    config = load_config()
    print(config)