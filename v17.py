'''
破解有道词典

'''
from urllib import request,parse

def youdao(key):

    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

    data = {
        "i": " girl",
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "15456407690273",
        "sign": "24503 fc8df77e56ca0f4ff0ebdc71640",
        "ts": "1545640769027",
        "bv": "1c13ced10aeceb64c3dd73719a38cbcd",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTIME",
        "typoResult": "false"
    }
    # 直接变成bytes
    data = parse.urlencode(data).encode()

    headers = {
                "Accept": "application / json, text / javascript, * / *; q = 0.01",
                "Accept - Encoding": "gzip, deflate"
                "Accept - Language": "zh - CN, zh;"
                "q" = "0.9"
                "Connection": "keep - alive"
                "Content - Length": "254"
                "Content - Type": "application / x - www - form - urlencoded;"
                "charset" = "UTF - 8"
                Cookie: OUTFOX_SEARCH_USER_ID = -109631377 @ 10.168.8.76;
                JSESSIONID = aaa6MmhJ5sPQaachfxFFw;
                OUTFOX_SEARCH_USER_ID_NCOO = 1695312360.5301702;
                ___rl__test__cookies = 1545640769024
                Host: fanyi.youdao.com
                Origin: http: // fanyi.youdao.com
                Referer: http: // fanyi.youdao.com /
                User - Agent: Mozilla / 5.0(WindowsNT10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 65.0.3325.146Safari / 537.36
    X           - Requested - With: XMLHttpRequest
    }
