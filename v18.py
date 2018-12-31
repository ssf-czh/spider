from lxml import  etree

html = etree.parse("etree.html",etree.HTMLParser())

# rst = html.xpath("//div")
# rst = html.xpath("//div/ul/li/@class")
# rst = html.xpath("//div/ul[@class]")
rst = html.xpath("//div/ul/li[@class='3']/text()")

print(rst)



# print(type(html))
# rst = etree.tostring(html)
# print(rst.decode())
