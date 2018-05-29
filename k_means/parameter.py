# -*- coding:utf-8 -*-
# 参数设置


from sqlalchemy import create_engine
import pymysql

engine_demo = create_engine('mysql+pymysql://wu:root@192.168.1.97/demo?charset=utf8')
engine_exhi = create_engine('mysql+pymysql://wu:root@192.168.1.97/exhi_info?charset=utf8')
engine = create_engine('mysql+pymysql://wu:root@192.168.1.97/exhi?charset=utf8')


cj = r'D:\原始展会处理\2017cjgs.xlsx'
cj_t = r'D:\原始展会处理\2017cjgst.xlsx'

qj = r'D:\原始展会处理\2017qj.xlsx'

cjry = r'D:\原始展会处理\2017cjry.xlsx'

qjry = r'D:\原始展会处理\2017qjry.xlsx'

l = [
    '销售',
    '技术开发',
    '开发',
    '零售',
    '生产',
    '加工',
    '批发',
    '制造',
    '研发',
    '设计',
    '制作',
    '代理',
    '收购',
    '印染',
    '自营',
    '经销',
    '产销',
    '购销',
    '投资',
    '服务',
    '进出口'
]

l2 = [
    '和', '与', '及', '兼'
]

l3 = [
    '一般经营项目',
    '许可经营项目：无',
    '其他无需报经审批的一切合法项目',
    '但国家限制经营或禁止进出口的货物和技术除外',
    '含下属分支机构的经营范围',
    '从事',
    '业务',
    '但国家限定公司经营或禁止进出口的商品及技术除外',
    '其他无需报经审批的合法项目'
]

col = ['ComID', 'Scope']

t = {
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',

}

company_field = {
     '单位中文名称': 'ComName',
     '完整中文地址': 'ComAddress',
     '邮编': 'ComZipCode',
     '完整英文名称': 'ComEName',
     '完整英文地址': 'ComEAddress',
     '英文地址1': 'ComEAddress1',
     '英文地址2': 'ComEAddress2',
     '英文地址3': 'ComEAddress3',
     '网址': 'ComWebUrl',
     '产品': 'ComProduct',
     '品牌': 'ComBrand',
     '国家中文': 'ComCountry',
     '国家英文': 'ComECountry',
     '地区': 'ComArea',
     '省份': 'ComProvince',
     '城市': 'ComCity',
     '洲别': 'ComContinent',
     '状态': 'ComState'
}

person_field = {
     '姓名': 'PsnName',
     '称谓': 'PsnAppellation',
     '部门': 'PsnDept',
     '职务': 'PsnRank',
     '手机': 'PsnMobile',
     '电话': 'PsnTel',
     '传真': 'PsnFax',
     'Email': 'PsnEmail'
}

"查询公司名称", "公司名称", "电话号码", "邮箱", "公司主页", "行业", "实际地址", "注册地址", "公司状态", "法人名称",
"注册资本", "注册时间", "核准时间", "工商注册号", "组织机构代码", "信用识别代码",
"公司类型", "纳税人识别号", "营业期限", "登记机关", "经营范围"

_field = {
     '查询公司名称': '',
     '公司名称': 'ComSName',
     '电话号码': 'ComSTel',
     '邮箱': 'ComSZipCode',
     '公司主页': 'ComSWebUrl',
     '行业': 'ComSTrade',
     '实际地址': 'ComSAcAddress',
     '注册地址': 'ComSReAddress',
     '公司状态': 'ComSSysState',
     '法人名称': 'ComSLegalPerson',
     '注册资本': 'ComSIntegral',
     '注册时间': 'ComSReTime',
     '核准时间': 'ComSChTime',
     '工商注册号': 'ComSRegisNum',
     '组织机构代码': 'ComSOrganCode',
     '信用识别代码': 'ComSCredit',
     '公司类型': 'ComSType',
     '纳税人识别号': 'ComSTaxpayer',
     '营业期限': 'ComSDeadline',
     '登记机关': 'ComSAuthority',
     '经营范围': 'ComSScope',
     '': '',
     '': '',
     '': '',
     '': '',
     '': '',
     '': '',
     '': '',
     '': '',
     '': '',

     }