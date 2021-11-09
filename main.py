# coding=gbk
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

def num1(rw):
    tca = 0.1  # 公司固定抽成
    sdi = 0.3  # 商户分成比例
    msp = 0.1  # 中间商分成比例
    ssf = 0.15  # 商户服务费比例
    msf = 0.15  # 中间商服务费比例

    print('=====流水为 %s 元时=====' % rw)
    # 公司收入
    num = round(rw * tca, 2)
    print('公司收入为: %s 元！' % num)

    # 商户税
    num2 = round((1 - tca) * rw * 0.06 * sdi, 2)
    print('商户税为: %s 元' % num2)

    # 中间商税
    num3 = round((1 - tca) * rw * 0.06 * msp, 2)
    print('中间商分成收益税为: %s 元' % num3)

    # 商户收入
    num4 = round((rw - rw * tca) * sdi * (1 - ssf), 2)
    print('商户收入为: %s 元' % num4)
    # 中间商收入
    num5 = round((rw - rw * tca) * msp * (1 - ssf), 2)
    print('中间商收入为: %s 元' % num5)

    # 合伙人税
    num6 = round((rw - rw * tca - (rw - rw * tca) * sdi * (1 - ssf) - (rw - rw * tca) * sdi * 0.06 - (
            rw - rw * tca) * msp * (1 - msf) - (rw - rw * tca) * msp * 0.06) * 0.06, 2)
    print('合伙人税为: %s 元' % num6)
    # 合伙人收入
    num7 = round(rw - num - num2 - num3 - num4 - num5 - num6,2)
    print('合伙人收入为: %s 元' % num7)


num1(100)
