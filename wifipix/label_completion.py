#!/usr/bin/env pthon3
# __*__ coding=utf-8 __*__

__author__ = "Code_like_wind"

'''
    标签补全:补全imei号，标签号替换为标签名称
'''

from  wifipix.wifipix_utils import *
from wifipix.w_excel import *


def get_name_by_tag_and_xhz(tag):
    tag_l = tag.split('|')
    tag_names = ''
    count = 0
    # print('tag01_l.len=', len(tag01_l))
    for tag_id_and_xhz in tag_l:
        count += 1
        t_id_and_xhz_l = tag_id_and_xhz.split(";")
        t_id = 0
        try:
            if len(t_id_and_xhz_l) == 2:
                t_id = int(t_id_and_xhz_l[0])
        except Exception as e:
            print(e)

        t_name = tag_dict.get(t_id)
        if t_name is not None:
            if count != len(tag_l):
                tag_names = tag_names + t_name + "|"
            else:
                tag_names = tag_names + t_name
    return tag_names


if __name__ == '__main__':
    # 获取标签字典和imei号字典
    tag_dict = get_tag_dict()  # 753
    # print(tag_dict.get(int('010305')))
    # print(tag_dict)
    imei_tict = analsysImeiTdid_to_dict()  # 114231
    print('tag_dict.size=', len(tag_dict))
    print('imei_tict.size=', len(imei_tict))
    count = 0  # 121531
    f = xlwt.Workbook()  # 创建工作簿
    sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=False)  # 创建sheet
    row0 = [u'tdid', u'imei', u'macs', u'01tag', u'02tag', u'03tag', u'04tag', u'06tag', u'city', u'community', u'os',
            u'pixel', u'other']
    for i in range(0, len(row0)):
        sheet1.write(0, i, row0[i], set_style('Times New Roman', 220, True))
    print('len(row0)=', len(row0))
    ex_out = open('tag_comletion.txt', 'a')
    with open('wifipix_tag.txt', 'r', encoding='utf-8') as file:
        for line in file:
            count += 1
            line_l = line.split('\t')
            if len(line_l) == 13:
                tdid = line_l[0]
                imei = imei_tict.get(line_l[0], None)
                macs = line_l[1]
                tag_01 = get_name_by_tag_and_xhz(line_l[2])
                tag_02 = get_name_by_tag_and_xhz(line_l[3])
                tag_03 = get_name_by_tag_and_xhz(line_l[4])
                tag_04 = get_name_by_tag_and_xhz(line_l[5])
                tag_06 = get_name_by_tag_and_xhz(line_l[6])
                city = line_l[7]
                community = line_l[8]
                j = line_l[9]  # 空列
                os = line_l[10]  # 空列
                pixel = line_l[11]  # 空列
                other = line_l[12]  # 空列
                # tag_completion = [tdid, imei, macs, tag_01, tag_02, tag_03, tag_04, tag_06, city, community, os, pixel,
                # other]
                # for i in range(0, len(row0)):
                # sheet1.write(0, i, row0[i], set_style('Times New Roman', 220, True))
                ex_out.write(
                    tdid + "\t" + imei + "\t" + macs + "\t" + tag_01 + "\t" + tag_02 + "\t" + tag_03 + "\t" + tag_04 + "\t" + tag_06 + "\t" + city + "\t" + community + "\t" + os + "\t" + pixel + "\t" + other)
                #     if tdid.strip():
                #         sheet1.write(count, 0, tdid)
                #         sheet1.write(count, 1, imei)
                #         sheet1.write(count, 2, macs)
                #         sheet1.write(count, 3, tag_01)
                #         sheet1.write(count, 4, tag_02)
                #         sheet1.write(count, 5, tag_03)
                #         sheet1.write(count, 6, tag_04)
                #         sheet1.write(count, 7, tag_06)
                #         sheet1.write(count, 8, city)
                #         sheet1.write(count, 9, community)
                #         sheet1.write(count, 10, os)
                #         sheet1.write(count, 11, pixel)
                #         sheet1.write(count, 12, other)
                # f.save('tag_completion.xlsx')
                # if city:
                #     print(city)
                # if j:
                #     print(j)
        ex_out.close()
