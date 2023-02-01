import requests
import json
import csv
from datetime import *
import time
import random

dat= date.today()
with open('Olxfz_MH_search'+str(dat)+'.csv','a',newline='',encoding='UTF-8') as fp:
    writer=csv.writer(fp)
    writer.writerow(['PageNumber','Record_no','Website','Product_Title','Product_Description','Short_Info','Brand','Model','Manufacture Year','Kilometer','Date of Posting','Price','State','city','pincode','Full Address','Sample Image Links','url'])

headers = {
    'authority': 'www.olx.in',
    'method': 'GET',
    'scheme': 'https',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'laquesis=pan-48200@a#pan-48658@b#pan-55076@b#pan-59446@b; laquesisff=pan-36788#pan-38000#pan-42665; bm_sz=24E217A5E77F83427F3177DB4CEF690C~YAAQZk/IF13WveR7AQAADDziKA0CnPjLnfdy7tjtVBCDR8cDGsdU9AFg3bqa06bHKnO//ySJnBQVJTV7gpp9JoeUKevCMQ+PCWD0cwoFxmOpUWrpmiyuXkUdpF3e8y+l6VIaizVUltRMRl8R6gyUS/3fo+35XdjUb4ZrMg8RO/mMjRvP37KPM8CKCcCff/KDSJep0WV++sDIQCdIT9xy/au24OJITY32w/E7Vt4zHaoKfeoj3YbDgHiolq0VYdB5J45q7PbJkhmO4UPQalHzjqlCYR2fzg3IlhIZzKNpJg==~3555635~3749424; ak_bmsc=92377648F0890DD8C3C1F6B9593C4E09~000000000000000000000000000000~YAAQZk/IFz/XveR7AQAANVPiKA1I7SuJia1q39aIv39rHtoVWcjOY258+JZhaVQiZuNedSxS4vWCQtUzBVybK8zph7MLGO0zDGuyyrllDSXNIba+WJZGnBwEuLLHcUOi+dEob8oo6yQ+dWzuDI6ZeNlLAk3C6snUS5VHBMdOXjVj7++/338nds1z1rc1rAOP37wvZqIqUEuoJy75FT8vEMX6MUo98iHEDNF95PImmV3LucyTGnN41Zc4lLXQnfdAvpuFZXfCefn0n282a1OHue/6V+3c16LX5UuZZx1OofAJoINpv8a/vusLDmt6g8PJMy60L2ROfYFb4noXIeNnFEARVWKqZIJZxAr5kKS5B7JX46RJ6Nm90t71yMn7zI0EeofXE9IARatlHD9CEittXhz+BU+dsQK2r4mil1sAemn20HE0t7AvsInyjmHoezt298jCheLw+rgEO6aUk/GKkPT3l/lJ/Im4W+Hl9jyDQAC28QSACpZrh/kdZw==; _abck=9CBA2E07763E98674DE3A4D8BA85035A~0~YAAQZk/IF1DYveR7AQAA2XLiKAY3hjn0pmRc9+FOWHDOvGQV9B7QM0469/ZK+rKX//cpD18NXlcRsqyKkQdYWRXcse7LXVKA4Tre+7BviZmhI3U4xrkcVVtWbZn0gzCi6msDVgwK2fabeYsnGtjNL4eZQg8eyNMUMzpB5Uvhd1s5y5/JbPZCg/JRkVui8c4kbNVPc5EFc+sNiuPnBMXuHKjHTn/jUGItnPIVT4t9rriVD2BnArNgf/iVDObFHWqF8qkHUqHOjScV1nGCKPvjnPZixQ/MJCNKBsEcU08P+PJCuqcQp22H4Ey3gw/kiNxzn6lEz4CEcM7e6e9w6FbSqfFjMtFZzwnJLxixvCh1T2+JChgyZ5gTBh0hnHTUrpllY0I1RxVRmo21yI4OaJex6U+35o0=~-1~||-1||~-1; ldTd=true; lqstatus=1632774687|17c28e23a37x667f7481|pan-48200; _ga=GA1.2.2012471199.1632773489; _gid=GA1.2.1036346873.1632773489; _gcl_au=1.1.1123564328.1632773489; WZRK_G=7de728cd2a354a75b296abbcbf05843b; __gads=ID=8b094ff6c3e97624:T=1632773503:S=ALNI_MYgQ5pqDLwVLrJd4Ys15fC0VHxY1g; AMP_TOKEN=%24NOT_FOUND; _fbp=fb.1.1632773491619.965949548; locationPath=%5B%7B%22id%22%3A4058997%2C%22name%22%3A%22Mumbai%22%2C%22type%22%3A%22CITY%22%2C%22longitude%22%3A72.86049%2C%22latitude%22%3A19.05911%2C%22parentId%22%3A2001163%7D%5D; WZRK_S_848-646-995Z=%7B%22p%22%3A1%2C%22s%22%3A1632773503%2C%22t%22%3A1632773526%7D; onap=17c28e23a37x667f7481-1-17c28e23a37x667f7481-24-1632775327; bm_sv=D0B15660CA0974D5F8EBAB87171252A3~HyjAc+FW7KqK0biIj2ukJhzWDTalgZtpRRKb0ZFeNOMoE5oeHCalqG7RBP9MPR0HEZfYTXj4KXMXTM+SsQ9dzlZt3ay+A4Fux44s7ERLp5/s1L6N2U1YMiOm0Hht77xpR5PQ8Vf7bXvVwwDEhx2E8USsplBkFmLFYxPFiBXaJL8=',
    'referer': 'https://www.olx.in/mumbai_g4058997/q-Fz?isSearchCall=true',
    'sec-ch-ua': '',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
    'x-newrelic-id': 'VQMGU1ZVDxABU1lbBgMDUlI=',
    'x-panamera-fingerprint': '1b4e4a5ba64611f2d0f6efd9a230c05c#1632773485132'
}
Browser_url = 'https://www.olx.in/maharashtra_g2001163/q-Fz?isSearchCall=true'
recordno = 0
for pageno in range(0, 25):
    print('Random sleep time Between 5,10')
    time.sleep(random.choice(range(5,10)))
    url = f'https://www.olx.in/api/relevance/v2/search?facet_limit=100&lang=en&location=2001163&location_facet_limit' \
          f'=20&page={pageno}&platform=web-desktop&query=Fz&spellcheck=true&user=17c28e23a37x667f7481 '
    try:
        source = requests.get(url, headers=headers, timeout=30)
        print(source.status_code)
        data = json.loads(source.text)          #Json response
        for item in data['data']:               #list data extraction
            print(f'---------Page{pageno}---------')
            recordno = recordno + 1
            print(f'Overall_Record_Number: {recordno}')
            try:
                title = item['title'].replace(" , ", ",").replace(", ", ",").replace(", ", ",").replace("'",
                                                                                                        "").replace(".",
                                                                                                                    "")
                print(title)
            except:
                title = ''
            try:
                description = item['description'].strip()
                print(description)
            except:
                description = ''
            try:
                main_info = item['main_info']
                # substr1 = ' -'
                # main_slice_info = main_info[:main_info.index(substr1) + len(substr1)]
                # main_slice_final = main_slice_info.replace(" -", "")
                # print(main_slice_final)
            except:
                main_info = ''
                # main_slice_final = ''
            print(main_info)
            try:
                dop = item['created_at']   #Remove after Substring in string,Using index() + len()+slicing
                substr = 'T'                #Initializing sub_strting
                res = dop[:dop.index(substr) + len(substr)]        #slicing off after length computation
                resfinal = res.replace("T", "")
                print(resfinal)
            except:
                dop = ''
                resfinal = ''
            try:
                id = item['id']
                print(id)
            except:
                id = ''
            try:
                url_product = title.replace(",", "-").replace(" ", "-").replace("(", "").replace(")", "").replace("%","").replace("*","").lower()
                product_url = (f'https://www.olx.in/item/{url_product}-iid-{id}')           #Manually creating product link
                print(product_url)
            except:
                url_product = ''
            try:
                price = item['price']['value']['display'].replace("₹ ", "")
                print(price)
            except:
                price = ''
            try:
                country = item['locations_resolved']['COUNTRY_name']
            except:
                country = ''
            try:
                state = item['locations_resolved']['ADMIN_LEVEL_1_name']
            except:
                state = ''
            try:
                city = item['locations_resolved']['ADMIN_LEVEL_3_name']
            except:
                city = ''
            try:
                subcity = item['locations_resolved']['SUBLOCALITY_LEVEL_1_name']
            except:
                subcity = ''
            try:
                pincode = item['locations_resolved']['ADMIN_LEVEL_3_id']
            except:
                pincode = ''
            fulladdress = f'{subcity},{city},{state},{country}{pincode}'
            print(fulladdress)
            try:
                brand = item['parameters'][0]['formatted_value']
            except:
                brand = ''
            print(brand)
            try:
                name_of_product = item['parameters'][1]['formatted_value']
            except:
                name_of_product = ''
            print(name_of_product)
            try:
                mfy = item['parameters'][2]['formatted_value']
            except:
                mfy = ''
            print(mfy)
            try:
                kilometer = item['parameters'][3]['formatted_value']
            except:
                kilometer = ''
            print(kilometer)
            try:
                for image in item['images']:
                    try:
                        imageurl = image['url']         #We can do a join here and extract all links , for sample i am just taking 1 link
                        print(imageurl)
                    except:
                        imageurl = ''
            except:
                pass
            with open('Olxfz_MH_search' + str(dat) + '.csv', 'a', newline='', encoding='UTF-8') as fp:
                writer = csv.writer(fp)
                writer.writerow(
                    [pageno, recordno,'olx.in',title,description,main_info,brand,name_of_product,mfy,kilometer,resfinal,price,state,city,pincode,fulladdress,imageurl,product_url])

    except Exception as e:
        with open('Olxfz_MH_Exception' + str(dat) + '.csv', 'a', newline='', encoding='UTF-8') as fp:
            writer = csv.writer(fp)
            writer.writerow([url,str(e)])
