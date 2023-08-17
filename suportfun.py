def stringtotuple(tupple1):
    Pk2 = tupple1[1:-1]
    # Tách chuỗi thành danh sách các chuỗi con
    string_list = Pk2.split(", ")

    # Chuyển đổi các chuỗi con thành các số nguyên
    integer_list = [int(x) for x in string_list]

    # Chuyển đổi danh sách số nguyên thành tuple
    tupple2 = tuple(integer_list)
    return tupple2
def remove_minus_sign(hex_str):
    return hex_str.replace('-', '')
def tuple_to_hex_string(input_tuple):
    # Sử dụng list comprehension để áp dụng hàm format() cho từng phần tử trong tuple và loại bỏ tiền tố "0x"
    hex_list = [format(item, 'x') for item in input_tuple]
    
    # Bỏ dấu trừ khỏi các chuỗi hex âm
    hex_list = [remove_minus_sign(hex_str) for hex_str in hex_list]
    
    # Nối các giá trị hex lại với nhau thành một chuỗi
    hex_string = ''.join(hex_list)
    
    return hex_string
def stringtohex(tring1):
    tring1 = stringtotuple(tring1)
    tring1 = tuple_to_hex_string(tring1)
    return tring1
def doublestringtotuple(input_string):
    # Tách chuỗi thành hai chuỗi con tương ứng với hai danh sách
    chuoi_1, chuoi_2 = input_string.split("][")

    # Kết hợp hai chuỗi con thành một chuỗi mới
    chuoi_moi = chuoi_1 + ',' + chuoi_2

    # Xóa dấu ngoặc vuông đầu và cuối của chuỗi mới
    chuoi_moi = chuoi_moi.replace("[", "").replace("]", "")

    # Chuyển các số thành danh sách
    danh_sach = [int(x) for x in chuoi_moi.split(",")]

    # Chuyển danh sách thành tuple
    tuple_moi = tuple(danh_sach)
    
    return tuple_moi
def string_to_2tuples(input_string):
    # Tách chuỗi thành hai chuỗi con tương ứng với hai danh sách
    chuoi_1, chuoi_2 = input_string.split("][")

    # Xóa dấu ngoặc vuông ở đầu và cuối của chuỗi
    chuoi_1 = chuoi_1.replace("[", "")
    chuoi_2 = chuoi_2.replace("]", "")

    # Chuyển chuỗi thành danh sách
    danh_sach_1 = [int(x) for x in chuoi_1.split(",")]
    danh_sach_2 = [int(x) for x in chuoi_2.split(",")]

    # Chuyển danh sách thành tuple
    tuple_1 = tuple(danh_sach_1)
    tuple_2 = tuple(danh_sach_2)

    return tuple_1, tuple_2