#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/10/16 9:27
# @Author : HyDady
# @Site : 
# @File : demo.py
# @Software: PyCharm
import json
json_part1 = {'北京': 'Beijing', '上海': 'Shanghai', '天津': 'Tianjin', '重庆': 'Chongqing', '大连': 'Dalian', '青岛': 'Qingdao', '西安': "Xi'an", '南京': 'Nanjing', '宿州': 'Suzhou', '杭州': 'Hangzhou', '厦门': 'Xiamen', '成都': 'Chengdu', '深圳': 'Shenzhen', '广州': 'Guangzhou', '三亚': 'Sanya', '台北': 'Taipei', '香港': 'Hong Kong', '济南': 'Jinan', '宁波': 'Ningbo', '沈阳': 'Shenyang', '武汉': 'Wuhan', '郑州': 'Zhengzhou', '阿坝': 'Abazhou', '阿克苏': 'Aksu', '阿勒泰': 'Aletai', '阿里': 'Ali', '阿拉善': 'Alxa', '安康': 'Ankang', '安庆': 'Anqing', '鞍山': 'Anshan', '安顺': 'Anshun', '安阳': 'Anyang', '澳门': 'Macau', '白城': 'Baicheng', '百色': 'Baise', '白沙': 'Baisha', '白山': 'Baishan', '白银': 'Baiyin', '保定': 'Baoding', '宝鸡': 'Baoji', '保山': 'Baoshan', '保亭': 'Baoting', '包头': 'Baotou', '巴彦淖尔': 'Bayan Nur', '巴音郭楞': 'Bayinguoleng', '巴中': 'Bazhong', '北海': 'Beihai', '蚌埠': 'Bengbu', '本溪': 'Benxi', '毕节': 'Bijie', '滨州': 'Binzhou', '博尔塔拉': 'Boertala', '亳州': 'Bozhou', '沧州': 'Cangzhou', '长春': 'Changchun', '常德': 'Changde', '昌吉': 'Changji', '昌江': 'Changjiang', '长沙': 'Changsha', '长治': 'Changzhi', '常州': 'Changzhou', '朝阳': 'Chaoyang', '潮州': 'Chaozhou', '承德': 'Chengde', '澄迈': 'Chengmai', '郴州': 'Chenzhou', '嘉义': 'Chiayi', '赤峰': 'Chifeng', '池州': 'Chizhou', '崇左': 'Chongzuo', '楚雄': 'Chuxiong', '滁州': 'Chuzhou', '大理市': 'Dali', '丹东': 'Dandong', '儋州': 'Danzhou', '大庆': 'Daqing', '大同': 'Datong', '大兴安岭': "Daxing'anling", '达州': 'Dazhou', '德宏': 'Dehong', '德阳': 'Deyang', '德州': 'Dezhou', '定安': "Ding'an", '定西': 'Dingxi', '迪庆': 'Diqing', '东方': 'Dongfang', '东莞': 'Dongguan', '东营': 'Dongying', '恩施': 'Enshi', '鄂州': 'Ezhou', '防城港': 'Fangchenggang', '佛山': 'Foshan', '抚顺': 'Fushun', '阜新': 'Fuxin', '阜阳': 'Fuyang', '福州': 'Fuzhou', '甘南': 'Gannan', '赣州': 'Ganzhou', '甘孜': 'Ganzizhou', '高雄': 'Kaohsiung', '果洛': 'Golog', '广安': "Guang'an", '广元': 'Guangyuan', '贵港': 'Guigang', '桂林': 'Guilin', '贵阳': 'Guiyang', '固原': 'Guyuan', '海北': 'Haibei', '海东': 'Haidong', '海口': 'Haikou', '海南': 'Hainan', '海西': 'Haixizhou', '邯郸': 'Handan', '汉中': 'Hanzhong', '哈尔滨': 'Harbin', '鹤壁': 'Hebi', '河池': 'Hechi', '合肥': 'Hefei', '鹤岗': 'Hegang', '黑河': 'Heihe', '衡水': 'Hengshui', '衡阳': 'Hengyang', '和田': 'Hetian', '河源': 'Heyuan', '菏泽': 'Heze', '贺州': 'Hezhou', '呼和浩特': 'Hohhot', '红河': 'Honghe', '新竹': 'Hsinchu', '淮安': "Huai'an", '淮北': 'Huaibei', '怀化': 'Huaihua', '淮南': 'Huainan', '花莲': 'Hualien', '黄冈': 'Huanggang', '黄南': 'Huangnan', '黄山': 'Huangshan', '黄石': 'Huangshi', '惠州': 'Huizhou', '葫芦岛': 'Huludao', '呼伦贝尔': 'Hulunbuir', '湖州': 'Huzhou', '佳木斯': 'Jiamusi', '吉安': "Ji'an", '江门': 'Jiangmen', '焦作': 'Jiaozuo', '嘉兴': 'Jiaxing', '嘉峪关': 'Jiayuguan', '揭阳': 'Jieyang', '吉林市': 'Jilin', '基隆': 'Jilong', '金昌': 'Jinchang', '晋城': 'Jincheng', '景德镇': 'Jingdezhen', '荆门': 'Jingmen', '荆州': 'Jingzhou', '金华': 'Jinhua', '济宁': 'Jining', '晋中': 'Jinzhong', '锦州': 'Jinzhou', '九江': 'Jiujiang', '酒泉': 'Jiuquan', '鸡西': 'Jixi', '济源': 'Jiyuan', '开封': 'Kaifeng', '克拉玛依': 'Karamay', '喀什': 'Kashi', '克孜勒苏': 'Kezilesu', '昆明': 'Kunming', '来宾': 'Laibin', '莱芜': 'Laiwu', '廊坊': 'Langfang', '兰州': 'Lanzhou', '乐东': 'Ledong', '乐山': 'Leshan', '拉萨': 'Lhasa', '凉山': 'Liangshanzhou', '连云港': 'Lianyungang', '聊城': 'Liaocheng', '辽阳': 'Liaoyang', '辽源': 'Liaoyuan', '丽江': 'Lijiang', '临沧': 'Lincang', '临汾': 'Linfen', '临高': 'Lingao', '陵水': 'Lingshui', '临夏': 'Linxia', '临沂': 'Linyi', '丽水': 'Lishui', '六盘水': 'Liupanshui', '柳州': 'Liuzhou', '陇南': 'Longnan', '龙岩': 'Longyan', '娄底': 'Loudi', '六安': 'Luan', '漯河': 'Luohe', '洛阳': 'Luoyang', '泸州': 'Luzhou', '吕梁': 'Lvliang', '马鞍山': "Ma'anshan", '茂名': 'Maoming', '眉山': 'Meishan', '梅州': 'Meizhou', '绵阳': 'Mianyang', '牡丹江': 'Mudanjiang', '南昌': 'Nanchang', '南充': 'Nanchong', '南宁': 'Nanning', '南平': 'Nanping', '南通': 'Nantong', '南阳': 'Nanyang', '那曲': 'Naqu', '内江': 'Neijiang', '新北': 'New Taipei City', '宁德': 'Ningde', '怒江': 'Nujiang', '林芝': 'Nyingchi', '鄂尔多斯': 'Ordos', '盘锦': 'Panjin', '攀枝花': 'Panzhihua', '澎湖': 'Penghu', '平顶山': 'Pingdingshan', '平凉': 'Pingliang', '屏东': 'Pingtung', '萍乡': 'Pingxiang', '普洱': "Pu'er", '莆田': 'Putian', '濮阳': 'Puyang', '昌都': 'Qamdo', '黔东南': 'Qiandongnan', '黔南': 'Qiannan', '黔西南': 'Qianxinan', '庆阳': 'Qingyang', '清远': 'Qingyuan', '秦皇岛': 'Qinhuangdao', '钦州': 'Qinzhou', '琼海': 'Qionghai', '琼中': 'Qiongzhong', '齐齐哈尔': 'Qiqihar', '七台河': 'Qitaihe', '泉州': 'Quanzhou', '曲靖': 'Qujing', '衢州': 'Quzhou', '日喀则': 'Rikaze', '日照': 'Rizhao', '三门峡': 'Sanmenxia', '三明': 'Sanming', '商洛': 'Shangluo', '商丘': 'Shangqiu', '上饶': 'Shangrao', '山南': 'Shannan', '汕头': 'Shantou', '汕尾': 'Shanwei', '韶关': 'Shaoguan', '绍兴': 'Shaoxing', '邵阳': 'Shaoyang', '石家庄': 'Shijiazhuang', '十堰': 'Shiyan', '石嘴山': 'Shizuishan', '双鸭山': 'Shuangyashan', '朔州': 'Shuozhou', '四平': 'Siping', '松原': 'Songyuan', '绥化': 'Suihua', '遂宁': 'Suining', '随州': 'Suizhou', '宿迁': 'Suqian', '塔城': 'Tacheng', '泰安': 'Taian', '台中': 'Taichung', '台南': 'Tainan', '太原': 'Taiyuan', '台州': 'Taizhou', '唐山': 'Tangshan', '桃园市': 'Taoyuan', '天水': 'Tianshui', '铁岭': 'Tieling', '铜川': 'Tongchuan', '通化': 'Tonghua', '通辽': 'Tongliao', '铜陵': 'Tongling', '铜仁': 'Tongren', '屯昌': 'Tunchang', '乌兰察布': 'Ulanqab', '乌鲁木齐': 'Urumqi', '万宁': 'Wanning', '潍坊': 'Weifang', '威海': 'Weihai', '渭南': 'Weinan', '文昌': 'Wenchang', '文山': 'Wenshan', '温州': 'Wenzhou', '乌海': 'Wuhai', '芜湖': 'Wuhu', '武威': 'Wuwei', '无锡': 'Wuxi', '五指山': 'Wuzhishan', '吴忠': 'Wuzhong', '梧州': 'Wuzhou', '湘潭': 'Xiangtan', '湘西': 'Xiangxi', '襄阳': 'Xiangyang', '咸宁': 'Xianning', '咸阳': 'Xianyang', '孝感': 'Xiaogan', '锡林郭勒盟': 'Xilinguole', '兴安盟': 'Xinganmeng', '邢台': 'Xingtai', '西宁': 'Xining', '新乡': 'Xinxiang', '信阳': 'Xinyang', '新余': 'Xinyu', '忻州': 'Xinzhou', '西双版纳': 'Xishuangbanna', '宣城': 'Xuancheng', '许昌': 'Xuchang', '徐州': 'Xuzhou', '雅安': "Ya'an", '延安': "Yan'an", '延边': 'Yanbian', '盐城': 'Yancheng', '阳江': 'Yangjiang', '阳泉': 'Yangquan', '扬州': 'Yangzhou', '烟台': 'Yantai', '宜宾': 'Yibin', '宜昌': 'Yichang', '宜春': 'Yichun', '银川': 'Yinchuan', '营口': 'Yingkou', '鹰潭': 'Yingtan', '益阳': 'Yiyang', '永州': 'Yongzhou', '岳阳': 'Yueyang', '榆林': 'Yulin', '运城': 'Yuncheng', '云浮': 'Yunfu', '云林市': 'Yunlin', '玉树': 'Yushu', '玉溪': 'Yuxi', '枣庄': 'Zaozhuang', '张家界': 'Zhangjiajie', '张家口': 'Zhangjiakou', '张掖': 'Zhangye', '漳州': 'Zhangzhou', '湛江': 'Zhanjiang', '肇庆': 'Zhaoqing', '昭通': 'Zhaotong', '镇江': 'Zhenjiang', '中山': 'Zhongshan', '中卫': 'Zhongwei', '周口': 'Zhoukou', '舟山': 'Zhoushan', '珠海': 'Zhuhai', '驻马店': 'Zhumadian', '株洲': 'Zhuzhou', '淄博': 'Zibo', '自贡': 'Zigong', '资阳': 'Ziyang', '遵义': 'Zunyi'}

json_part2 = {'北京': '1', '上海': '2', '天津': '3', '重庆': '4', '大连': '6', '青岛': '7', '西安': '10', '南京': '12', '苏州': '14', '杭州': '17', '厦门': '25', '成都': '28', '深圳': '30', '广州': '32', '三亚': '43', '台北': '617', '香港': '58', '济南': '144', '宁波': '375', '沈阳': '451', '武汉': '477', '郑州': '559', '阿坝': '1838', '阿克苏': '173', '阿勒泰': '175', '阿里': '97', '阿拉善': '7548', '安康': '171', '安庆': '177', '鞍山': '178', '安顺': '179', '安阳': '181', '澳门': '59', '白城': '1116', '百色': '1140', '白沙': '21025', '白山': '3886', '白银': '1541', '保定': '185', '宝鸡': '112', '保山': '197', '保亭': '54', '包头': '141', '巴彦淖尔': '3887', '巴音郭楞': '21130', '巴中': '3966', '北海': '189', '蚌埠': '182', '本溪': '1155', '毕节': '22031', '滨州': '1820', '博尔塔拉': '21468', '亳州': '1078', '沧州': '216', '长春': '158', '常德': '201', '昌吉': '22032', '昌江': '56', '长沙': '206', '长治': '137', '常州': '213', '朝阳': '211', '潮州': '215', '承德': '562', '澄迈': '20836', '郴州': '612', '嘉义': '5152', '赤峰': '202', '池州': '218', '崇左': '1896', '楚雄': '21658', '滁州': '214', '大理市': '36', '丹东': '221', '儋州': '57', '大庆': '231', '大同': '136', '大兴安岭': '7663', '达州': '1233', '德宏': '365', '德阳': '237', '德州': '1370', '定安': '50', '定西': '1021', '迪庆': '93', '东方': '48', '东莞': '223', '东营': '236', '恩施': '245', '鄂州': '992', '防城港': '1677', '佛山': '251', '抚顺': '252', '阜新': '254', '阜阳': '257', '抚州': '3884', '福州': '258', '甘南': '7844', '赣州': '268', '甘孜': '4124', '高雄': '720', '果洛': '21862', '广安': '1100', '广元': '267', '贵港': '1518', '桂林': '33', '贵阳': '38', '固原': '321', '海北': '7807', '海东': '7752', '海口': '42', '海南': '7794', '海西': '7589', '邯郸': '275', '汉中': '129', '哈尔滨': '5', '鹤壁': '951', '河池': '3969', '合肥': '278', '鹤岗': '1611', '黑河': '281', '衡水': '290', '衡阳': '297', '和田': '20931', '河源': '693', '菏泽': '1074', '贺州': '4146', '呼和浩特': '103', '红河': '1341', '新竹': '3845', '淮安': '577', '淮北': '272', '怀化': '282', '淮南': '287', '花莲': '6954', '黄冈': '3885', '黄南': '7802', '黄山': '23', '黄石': '292', '惠州': '299', '葫芦岛': '1050', '呼伦贝尔': '4255', '湖州': '86', '佳木斯': '317', '吉安': '933', '江门': '316', '焦作': '1093', '嘉兴': '571', '嘉峪关': '326', '揭阳': '956', '吉林市': '159', '基隆': '7810', '金昌': '1158', '晋城': '1092', '景德镇': '305', '荆门': '1121', '荆州': '328', '金华': '308', '济宁': '318', '晋中': '1453', '锦州': '327', '九江': '24', '酒泉': '662', '鸡西': '157', '济源': '1454', '开封': '331', '克拉玛依': '166', '喀什': '21358', '克孜勒苏': '21482', '昆明': '34', '来宾': '1892', '莱芜': '1452', '廊坊': '340', '兰州': '100', '乐东': '49', '乐山': '345', '拉萨': '41', '凉山': '7537', '连云港': '353', '聊城': '1071', '辽阳': '351', '辽源': '352', '丽江': '37', '临沧': '1236', '临汾': '139', '临高': '20868', '陵水': '55', '临夏': '21892', '临沂': '569', '丽水': '346', '六盘水': '605', '柳州': '354', '陇南': '7707', '龙岩': '348', '娄底': '918', '六安': '1705', '漯河': '1088', '洛阳': '350', '泸州': '355', '吕梁': '7631', '马鞍山': '1024', '茂名': '1105', '眉山': '1148', '梅州': '3053', '绵阳': '370', '牡丹江': '150', '南昌': '376', '南充': '377', '南宁': '380', '南平': '606', '南通': '82', '南阳': '385', '那曲': '3839', '内江': '1597', '新北': '7662', '宁德': '378', '怒江': '1806', '林芝': '108', '鄂尔多斯': '3976', '盘锦': '387', '攀枝花': '1097', '澎湖': '7805', '平顶山': '3222', '平凉': '388', '屏东': '5589', '萍乡': '1840', '普洱': '3996', '莆田': '667', '濮阳': '1232', '昌都': '575', '黔东南': '21778', '黔南': '21179', '黔西南': '21613', '庆阳': '404', '清远': '1422', '秦皇岛': '147', '钦州': '1899', '琼海': '52', '琼中': '53', '齐齐哈尔': '149', '七台河': '1599', '泉州': '406', '曲靖': '985', '衢州': '407', '日喀则': '92', '日照': '1106', '三门峡': '436', '三明': '437', '商洛': '7551', '商丘': '441', '上饶': '411', '山南': '439', '汕头': '447', '汕尾': '1436', '韶关': '422', '绍兴': '22', '邵阳': '1111', '石家庄': '428', '十堰': '452', '石嘴山': '4216', '双鸭山': '1617', '朔州': '1317', '四平': '440', '松原': '1303', '绥化': '1128', '遂宁': '1371', '随州': '1117', '宿迁': '1472', '宿州': '521', '塔城': '455', '泰安': '454', '台中': '3849', '台南': '3847', '太原': '105', '泰州': '579', '台州': '578', '唐山': '468', '桃园市': '7570', '天水': '464', '铁岭': '1048', '铜川': '118', '通化': '456', '通辽': '458', '铜陵': '459', '铜仁': '22033', '屯昌': '47', '乌兰察布': '7518', '乌鲁木齐': '39', '万宁': '45', '潍坊': '475', '威海': '479', '渭南': '1030', '文昌': '44', '文山': '20963', '温州': '491', '乌海': '1133', '芜湖': '478', '武威': '664', '无锡': '13', '五指山': '46', '吴忠': '7587', '梧州': '492', '湘潭': '598', '湘西': '3910', '襄阳': '496', '咸宁': '937', '咸阳': '111', '孝感': '1490', '锡林郭勒盟': '7576', '兴安盟': '21021', '邢台': '947', '西宁': '124', '新乡': '507', '信阳': '510', '新余': '603', '忻州': '513', '西双版纳': '35', '宣城': '1006', '许昌': '1094', '徐州': '512', '雅安': '3277', '延安': '110', '延边': '867', '盐城': '1200', '阳江': '692', '阳泉': '907', '扬州': '15', '烟台': '533', '宜宾': '514', '宜昌': '515', '伊春': '517', '宜春': '518', '银川': '99', '营口': '1300', '鹰潭': '534', '益阳': '1125', '永州': '970', '岳阳': '539', '玉林': '1113', '榆林': '527', '运城': '140', '云浮': '3933', '云林市': '7523', '玉树': '21114', '玉溪': '186', '枣庄': '614', '张家界': '27', '张家口': '550', '张掖': '663', '漳州': '560', '湛江': '547', '肇庆': '552', '昭通': '555', '镇江': '16', '中山': '553', '中卫': '556', '周口': '3221', '舟山': '19', '珠海': '31', '驻马店': '551', '株洲': '601', '淄博': '542', '自贡': '544', '资阳': '1560', '遵义': '558'}

str1 = json.dumps(json_part1,ensure_ascii=False)

str2 = json.dumps(json_part2,ensure_ascii=False)
with open('pingyin_city.txt','w') as f:
    f.write(str1)
#
# with open('number_city.txt','w') as g:
#     g.write(str2)

# with open('pingyin_city.txt','r') as f:
#     data = f.read()
#
# dict_new = json.loads(data)
# print(dict_new)
# print(type(data))