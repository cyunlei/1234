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
    tca = 0.1  # ��˾�̶����
    sdi = 0.3  # �̻��ֳɱ���
    msp = 0.1  # �м��̷ֳɱ���
    ssf = 0.15  # �̻�����ѱ���
    msf = 0.15  # �м��̷���ѱ���

    print('=====��ˮΪ %s Ԫʱ=====' % rw)
    # ��˾����
    num = round(rw * tca, 2)
    print('��˾����Ϊ: %s Ԫ��' % num)

    # �̻�˰
    num2 = round((1 - tca) * rw * 0.06 * sdi, 2)
    print('�̻�˰Ϊ: %s Ԫ' % num2)

    # �м���˰
    num3 = round((1 - tca) * rw * 0.06 * msp, 2)
    print('�м��̷ֳ�����˰Ϊ: %s Ԫ' % num3)

    # �̻�����
    num4 = round((rw - rw * tca) * sdi * (1 - ssf), 2)
    print('�̻�����Ϊ: %s Ԫ' % num4)
    # �м�������
    num5 = round((rw - rw * tca) * msp * (1 - ssf), 2)
    print('�м�������Ϊ: %s Ԫ' % num5)

    # �ϻ���˰
    num6 = round((rw - rw * tca - (rw - rw * tca) * sdi * (1 - ssf) - (rw - rw * tca) * sdi * 0.06 - (
            rw - rw * tca) * msp * (1 - msf) - (rw - rw * tca) * msp * 0.06) * 0.06, 2)
    print('�ϻ���˰Ϊ: %s Ԫ' % num6)
    # �ϻ�������
    num7 = round(rw - num - num2 - num3 - num4 - num5 - num6,2)
    print('�ϻ�������Ϊ: %s Ԫ' % num7)


num1(100)
