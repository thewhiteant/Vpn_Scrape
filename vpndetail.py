from bs4 import BeautifulSoup as soup
import requests
import readchar


#vpnbook

html = requests.get("https://www.vpnbook.com/freevpn").text
file = soup(html,'lxml')
alllinks = file.find('ul', class_='disc')
link = alllinks.find_all('li')
print("All Vpn Links")
for i in link:
    print(i.text)

passw = link[-1].img['src']
print(f"https://www.vpnbook.com/{passw}")



#vertual location
html1 = requests.get("https://www.virtuallocation.com/vpn/free-pptp-vpn.html").text
page = (html,"lxml")
table_data = page.find("table", class_="table table-inner-middle table-responsive-md table-bordered table-striped-light font-size-large")
tr = table_data.find_all("tr")
tr.pop(0)
for i in tr:
    data = i.find_all("td")
    print(
        f"Address :  {data[1].text} \nuser:{data[2].text} \npassword: {data[3].text}")





print("Press Any Key To Exit")
k = readchar.readchar()
