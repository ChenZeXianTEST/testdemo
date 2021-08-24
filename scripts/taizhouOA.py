import requests
from lxml import etree


class Taizou:
    bm_list = ['排污权储备中心', '五水共治办', '总量控制处', '局领导', '办公室', '项目处', '创模办', '污控处', '固废中心', '监察支队',
               '宣教法制处', '宣教信息中心', '监测中心站',
               '环科院', '环境简报', '生态简报', '创模简报', '信息简报', '部门文件', '省厅文件', '专报信息', '污染源普查',
               '国家环保总局', {'县市区环保局': ['椒江环保局', '玉环环保局', '三门环保局', '天台环保局', '仙居环保局', '临海环保局', '温岭环保局', '路桥环保局', '黄岩环保局']},
               '在线监控', '法律法规', {'法律法规': ['法律', '省规章', '地方性法规', '行政法规']}, '生态处', '在线监控系统巡检月报']
    k = 1

    def k_count(self):
        print(self.k)
        self.k += 1

    def add_information(self):
        html_token = self.get_html_token()
        xh = 338524357708033

        for i in self.bm_list:
            if isinstance(i, (str, list)):
                xh += 1
                html_token = self.get_html_token()
                data = {'org.apache.struts.taglib.html.TOKEN': html_token, 'method': 'save', 'XH': xh, 'XL': '',
                        'pagePath': '//pages/zhbg/ggxx/ggxxEdit.jsp', 'BT': str(i)+'test001', 'DJR': '系统管理员',
                        'DJRQ': '2021-07-22', 'SSBM': 'tzhbj_xjxxzx', 'NGBMMC': '市环境宣教信息中心', 'DL': i, 'NR': '7895'}
                self.post_requests(data)
            else:
                for ii in i:
                    for iii in i[ii]:
                        xh += 1
                        html_token = self.get_html_token()
                        data = {'org.apache.struts.taglib.html.TOKEN': html_token, 'method': 'save', 'XH': xh,
                                'XL': iii, 'pagePath':'//pages/zhbg/ggxx/ggxxEdit.jsp', 'BT': str(iii)+'test001',
                                'DJR': '系统管理员', 'DJRQ': '2021-07-22', 'SSBM': 'tzhbj_xjxxzx', 'NGBMMC': '市环境宣教信息中心', 'DL': ii, 'NR': '7895'}
                        self.post_requests(data)
                        print(data)

    def post_requests(self, data):
        url = 'http://192.168.0.212:8080/zhbg/pages/form.do'
        headers = {
            'Cookie': 'JSESSIONID=8F423FC219AC692FE0C4E77B6107B9B5; reloginCk=mrjvcb4EKAfdDLYNgItphUBb2HdbmuSCTEpnwSprie6pdraH44hlZcbmP3huYhKsp3zkLDqCKcPn_eEdhV4r8PPv5mRP5Mrhd6pZjvbnCuN4reduR-jTDNpOY3WUjQINjJpZQTyHJR88DAL1AKY9UztcZFWZF9JVmMOD3ufZkxSF4-CKUAzBfwCINzKZ56AXMY5uevKP0CSU9ncNrIx7SPb92Qc8eqymM5-OKmf2hs9uMiU-AxBZz0oe9rEyRrloVxLeX6rbC-rCbQNFGWRnXUlFX2fwxPm6O8r77N0jHX7D1z0R9zWk7YucpesjTZaErcNb3OCuWN3GCcpX0_GzsgC1_nHFWeqchdexNSOEhPI='}
        result = requests.post(url=url, data=data, headers=headers).text
        self.set_html_token(result)

    def set_html_token(self, result):
        root = etree.HTML(result.text)
        html_token = root.xpath("//input[@name='org.apache.struts.taglib.html.TOKEN']/@value")
        filepath = './html_token.txt'
        with open(filepath, 'w+', encoding='utf-8') as f:
            f.writelines(html_token[0])

    def get_html_token(self):
        filepath = './html_token.txt'
        with open(filepath, 'r', encoding='utf-8') as f:
            html_token = f.readline()
        return html_token


if __name__ == '__main__':
    a = Taizou()
    a.add_information()
