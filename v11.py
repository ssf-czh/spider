from urllib import request, error

if __name__ == '__main__':
    url = "http://www.renren.com/969221230/profile"
    #
    # rsp = request.urlopen(url)
    #
    # html = rsp.read().decode()
    #
    # with open("renrenwang.html","a+") as f:
    #     f.write(html)
    #
    headers={
        "Cookie":"anonymid=jq1rg88yrrv3fi; depovince=FJ; _r01_=1; JSESSIONID=abcnfXSHbGxqgaXSiqEFw; ick_login=94e7d4d0-c13e-438f-84bc-24a856c921eb; ick=4223a12a-33e7-4e2c-9761-32be3f846a5b; t=2638ba63cb8287fa9b51b0b4e63237bf0; societyguester=2638ba63cb8287fa9b51b0b4e63237bf0; id=969221230; xnsid=21be1de1; XNESSESSIONID=c7e13f271af6; WebOnLineNotice_969221230=1; jebecookies=a74e0531-d128-4636-b7e0-ff22f134d789|||||; ver=7.0; loginfrom=null; jebe_key=bd81b656-8149-46fc-a062-67d65d514eb3%7C51e5ab6560b3a3316112deb4e4e66b49%7C1545622161205%7C1%7C1545622161462; wp_fold=0"

    }
    rqs = request.Request(url, headers = headers)
    rsp = request.urlopen(rqs)
    html = rsp.read().decode()

    with open("renrenwang1.html","a+") as f:
        f.write(html)



