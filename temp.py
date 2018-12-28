import requests

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"
# }
#
# r= requests.get("http://www.zhihu.com/explore",headers = headers)
#
# print(r.text)



#
#
# data = {
#     "name": "czh",
#     "age": 18
# }
#
# r = requests.post("http://httpbin.org/post",data= data)
#
# print(r.text)
# print(r.cookies)



# files ={"file": open("G:/Git_Repository/spider/book_test/05.ico","rb")}
# r = requests.post("http://httpbin.org/post",files = files)
# print(r.text)



# r= requests.get("http://www.baidu.com")
# print(r.cookies)
# for key,value in r.cookies.items():
#     print(key + "=" + value)


headers = {
    "Cookie": '_xsrf=6GvCSxWl5soOXYD5Kd1rkYWvDRtfw4lL; _zap=ef494312-fc42-4386-b780-533f563764e0; d_c0="APCgqB6Stg6PTl833WXgoip-vsAqxmH1sQ0=|1545550286"; tgw_l7_route=e0a07617c1a38385364125951b19eef8; l_n_c=1; q_c1=e624add3e00d47f6a004090bcd1f03e7|1545704424000|1545704424000; r_cap_id="NzFhOWQzNjMzYmU3NGU1N2E4ZjUzMTIyOWE0ODIxNWQ=|1545704424|522c032e530e537ec756f037836590b4226e2836"; cap_id="ZGQ4NGMyZjQ3M2E4NDUyOWEzM2E2ZDk4ODBmYjgxMWE=|1545704424|f1ee0a1f2cef20ca8d2f24fb901947817093f5d5"; l_cap_id="MzAyYjViZGUxNTRhNDA0OGI4NGRkYzU1NTRmMWVjMmM=|1545704424|4f185e41d0d686b50ee6482d86bf0db20f8795b4"; n_c=1; __utma=51854390.939629086.1545704429.1545704429.1545704429.1; __utmb=51854390.0.10.1545704429; __utmc=51854390; __utmz=51854390.1545704429.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); capsion_ticket="2|1:0|10:1545704982|14:capsion_ticket|44:YzA5MWYwZGFkNTMzNDQ0ZDliOTg1NWM1NWNiZGVlMGY=|fedf7a69a618d3fca2633a4ea771577d2c47da1e1dce7e69594348d0db435a06"; z_c0="2|1:0|10:1545704999|4:z_c0|92:Mi4xUzdLUkNRQUFBQUFBOEtDb0hwSzJEaVlBQUFCZ0FsVk5KLVFPWFFEeGRkckV6cFVSLXM1dG9PN2QyZElnTnd5eE5R|c8d39cf88b55d40bbd9b57edb1c3f76eca8686ed3bb463a4e94937d40243807d"; unlock_ticket="AADjMuQ5oA0mAAAAYAJVTS-dIVxlOaESrShaRZrwcWNndlhr-A1Ikw=="; __utmv=51854390.100--|2=registration_date=20180521=1^3=entry_date=20180521=1',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36",
    "Host": "www.zhihu.com"
}

r= requests.get("http://www.zhihu.com",headers = headers)
print(r.text)