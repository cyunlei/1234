import random
from urllib3 import encode_multipart_formdata


def create_name():
    """
    :return:自动生成姓名
    """
    firstname = """
    李，王，张，刘，陈，杨，黄，赵，周，吴，徐，孙，朱，马，胡，郭，林，何，高，梁，郑，罗，宋，谢，唐，韩，曹，许，邓，萧，冯，曾，程，蔡，彭，潘，袁，於，董，余，苏，叶，吕，魏，蒋，田，杜，丁，沈，姜，范，江，傅，钟，卢，汪，戴，崔，任，陆，廖，姚，方，金，邱，夏，谭，韦，贾，邹，石，熊，孟，秦，阎，薛，侯，雷，白，龙，段，郝，孔，邵，史，毛，常，万，顾，赖，武，康，贺，严，尹，钱，施，牛，洪，龚，司马，公孙，长孙，诸葛，东方
    """
    Blastname = """
    豪、言、玉、意、泽、彦、轩、景、正、程、诚、宇、澄、安、青、泽、轩、旭、恒、思、宇、嘉、宏、皓、成、宇、轩、玮、桦、宇、达、韵、磊、泽、博、昌、信、彤、逸、柏、新、劲、鸿、文、恩、远、翰、圣、哲、家、林、景、行、律、本、乐、康、昊、宇、麦、冬、景、武、茂、才、军、林、
    茂、飞、昊、明、明、天、伦、峰、志、辰、亦
    """
    Glastname = """
    佳、彤、自、怡、颖、宸、雅、微、羽、馨、思、纾、欣、元、凡、晴、玥、宁、佳、蕾、桑、妍、萱、宛、欣、灵、烟、文、柏、艺、以、如、雪、璐、言、婷、青、安、昕、淑、雅、颖、云、艺、忻、梓、江、丽、梦、雪、沁、思、羽、羽、雅、访、烟、萱、忆、慧、娅、茹、嘉、幻、辰、妍、雨、蕊、欣、芸、亦
    """
    f2 = []
    b2 = []
    g2 = []
    f = firstname.replace('，', '').split()
    b = Blastname.replace('、', '').split()
    g = Glastname.replace('、', '').split()
    for f1, b1, g1 in zip(f[0], b[0], g[0]):
        f2.append(f1)
        b2.append(b1)
        g2.append(g1)

    name_first = random.choice(f2)
    name_blast = random.choice(b2)
    name_glast = random.choice(g2)

    return name_first + name_blast + name_glast


def create_phone():
    """
    :return: 随机生成手机号
    """
    # 第二位数字
    second = [3, 4, 5, 7, 8][random.randint(0, 4)]

    # 第三位数字
    third = {
        3: random.randint(0, 9),
        4: [5, 7, 9][random.randint(0, 2)],
        5: [i for i in range(10) if i != 4][random.randint(0, 8)],
        7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
        8: random.randint(0, 9),
    }[second]

    # 最后八位数字
    suffix = random.randint(9999999, 100000000)

    # 拼接手机号
    return "1{}{}{}".format(second, third, suffix)


def send_img(img_name,img_path):
    with open(img_path, mode='rb', ) as f:
        file = (img_name, f.read())

        return file
