import requests
import csv
from datetime import *
import json
import time
import math

#Sraping Proagram for Naukri
#We have searched for PythonDeveloper and have scraped first 10pages and extracted data in csv format
#Some fix needs to be done

dat= date.today()


with open('Naukri_PythonDev_'+str(dat)+'.csv','a',newline='',encoding='UTF-8') as fp:
    writer=csv.writer(fp)
    writer.writerow(['PageNumber','Record_no','Website','Job_Title','Company','Job_Description','Required_Skills','Details1','Details2','Posted','Url'])

with open('Naukri_excetpionFile_'+str(dat)+'.csv','a',newline='',encoding='UTF-8') as fp:
    writer=csv.writer(fp)
    writer.writerow(['url','Exception'])

def header():
    headers={
        'authority': 'www.naukri.com',
        'method': 'GET',
        'scheme': 'https',
        'accept': 'application/json',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'en-US,en;q=0.9',
        'appid': '109',
        'cache-control': 'no-cache',
        'clientid': 'd3skt0p',
        'content-type': 'application/json',
        'cookie': '_t_s=seo; _t_sd=google; _t_ds=15cb933b1675195889-415cb933b-015cb933b; _t_us=63D975FC; _t_ds=15cb933b1675195889-415cb933b-015cb933b; bm_sz=E5D104C8BB3EA8D3E4769BFAF500C5B5~YAAQj/7UF5KMBcmFAQAA+7V0CRKKcOLShMsS+8C19eV5uJD8XQXrmp03RUpzHnvqA0zi/4kG7v31zyoS8AsnwK79Ymxc7LHIvH9DR4FNJJ3AqOlgnOx985RMn8RUrTxDvvir6qh+pC9E08Z1XJ1MRzLCIgwAoZpVjMxAYfCrY8i5BhdUreaU38V0l5jcaWhlwoAkYHLw8UyDsE/XhLAIEHuhe+nzo56VebW9lqBA6YB7nGLF/qHGcD3jPnb1FL4RJQipuD50TAepOrsVVL7ducD/tN5Jx79lGrxdk4KtrFac7Bs=~3359297~3618871; test=naukri.com; _t_s=seo; _t_sd=google; _t_r=1030%2F%2F; persona=default; bm_mi=127AC3E6899BF7340456F8984D5BF000~YAAQj/7UF4+NBcmFAQAA1OB0CRI0ArPaKdBWHSR7hTGTfooNEPS728VYLQs8qyHpr7HTqeyIM7eaTbPP9nQDA8H/uvl2G1+g9eUh/3MqyAdOliEif7kYX7vjW8FeGF5dJbF1SoEhIGz7H/bGpnKw8h2lyVlkIW8YuhAb4m0LJsMBZSMiztfneEAzqKpIcpiKML75wiGbXgz5QXTNiZrY/hvJIAmg/BvrLezP9plBEjTtPb8bdpHQ9YjiKLkV3nPEXIhx6dMQvcEIescw2UPFnjvAmI9HJGup6kySbThyocjiW+LQNa3a3e6ucetZwQ==~1; _gcl_au=1.1.956252220.1675195904; _gid=GA1.2.1276671754.1675195904; _gac_UA-182658-1=1.1675195904.CjwKCAiAleOeBhBdEiwAfgmXfy8bLT_J_p6SknBBnWsGSbO_b2L7LeUSCUwDZP99f7oHHnF1TVTCuRoCB20QAvD_BwE; _abck=B38A9A04582991D90C3CD51924B3951F~0~YAAQj/7UF86NBcmFAQAAovN0CQkoe14FepM6ak54HF7H+iv0oUJHaewJmuQl5fKWZdO3dQkT1rzINGs2s5Y94N+B76POFSGZOgZ3uDWozSM2MyviK88eIHmCMHVInjAYPU6R0YMXxiZvyHkTAzf5ouUL6hrZri8aK4T/HrEFx1CDhtM744VdP+lu6MRNqe0g7Yog3u70mmtGWSyKpO+MByiOSe1rFhm8p1V3uisaOKzFzIUnFnSXpgycRxfVQiFki3hi5zw8RDLe2W8isApA8a+wNWehUJEcyLj6/X0LAvarmIUmw5+IOHgdL2R5E+GbV2gMChXs7mQkgpLYrKonJq6bRJa0R8e+uNMzeL5qhLe0CzpJPNVY1ZjTX2EO/sMOO7VBqzadirWmiX4QL4gCUaEkECJox+zF~-1~||-1||~-1; ak_bmsc=87D98D43E6A45487703C49204F9C507D~000000000000000000000000000000~YAAQj/7UF9iNBcmFAQAAtPR0CRJea+l73M05K04TAPjhBXMfytrttj2PPeKcG/WpqEDvGpJKyV1SFG8wDkzZTnJy2FP0ExZjyzQdftRbrmtlj7ew5s262UQYbx+DIdLi6OAtmtu+ZK0pwqU9BEo9S0oq0oJxp6ShwJl2RaMxyj9/w5lBBoXOZ4lhAV9oT5aXnQdT5Vp03owlVJRt9PL0aQ+SAP9i3KQT+7xdqzRcl/9vORwuZ4B5+2ir/kbHntXpAG9v3cl2VRPP0nC6hOab3wr53Zmz8LbyYFghh+aWYCamjwkveS3P+q9ZuxsCRvBts6zZsuEu49G7wwZ2A21CwRPrZal3oManVx2qYTMyHiNCRU840HZfvmAdOW94YAcOeqxdZ7BmB1MFY+9P3x2eQIAc8TGFR++FKLw=; __insp_wid=22757929; __insp_slim=1675195905427; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly93d3cubmF1a3JpLmNvbS9yZWdpc3RyYXRpb24vY3JlYXRlQWNjb3VudD9vdGhlcnNyY3A9MjM1MzEmd0V4cD1OJnV0bV9zb3VyY2U9Z29vZ2xlJnV0bV9tZWRpdW09Y3BjJnV0bV9jYW1wYWlnbj1CcmFuZCZnY2xpZD1DandLQ0FpQWxlT2VCaEJkRWl3QWZnbVhmeThiTFRfSl9wNlNrbkJCbldzR1NiT19iMkw3TGVVU0NVd0RaUDk5ZjdvSEhuRjFUVlRDdVJvQ0IyMFFBdkRfQndFJmdjbHNyYz1hdy5kcw%3D%3D; __insp_targlpt=UmVnaXN0ZXIgb24gTmF1a3JpLmNvbTogQXBwbHkgdG8gTWlsbGlvbnMgb2YgSm9icyBPbmxpbmU%3D; __insp_norec_sess=true; _fbp=fb.1.1675195907455.17579891; _ga=GA1.2.1855441798.1675195904; _ga_K2YBNZVRLL=GS1.1.1675195947.1.0.1675195955.0.0.0; __gads=ID=3271c113fedae1b3:T=1675195958:S=ALNI_MbJ_n_CiD4gIoPpJ5WRQbVUlBsKww; __gpi=UID=00000bb1c9498a01:T=1675195958:RT=1675195958:S=ALNI_MYRTbvW4-8vfWBaUXBaA4kiwunvLA; cto_bundle=DjJ3Gl9uJTJGa3RmSWdCdmI2ZUkxeDJ4TGZkb1M2Z052YUZBdXFRRjJ4U2F3ZEdwNENwNGNlb2gxUU9PcENNYk1ZaHBvaFptUzg0Z3RqSjFWOWVjdTl6JTJGcUFRT0UlMkZCcHQyOXplZ2wydGlNOVQ3YUlzV2VXZ2Z5b0kxVmpJSVV3JTJCV1JEZHo4bGJ4elo0bGFTVWhWTzZrUm1DMklJUSUzRCUzRA; _gat_UA-182658-1=1; bm_sv=519B1F798D21D260AF31FEF631F1576F~YAAQj/7UFw8dBsmFAQAA9GSYCRJ1p/19nUVCdfy681tiVc3LecP04e5xJ6tFEWJFXIqpQ886bKllPotcG0Bc5IPwqZUN2rSVCNOccT04ek6hblAMpGBJb1GLxLiddGNzSZj0nIj3O3F6H+YuVtS+Xjv1+CNOwrWZaw5FdkEJqd2l7X52U9I8WS6VFnNvgRrSbXXNoUCXVFXwuJr/7GqchW62rEIZ3Af9sBf0AKudneJG8pBIVmm1UD7+09190xc/uA==~1; HOWTORT=ul=1675198221643&r=https%3A%2F%2Fwww.naukri.com%2Fpython-jobs-2%3Fk%3Dpython&hd=1675198221841&cl=1675198241604&nu=https%3A%2F%2Fwww.naukri.com%2Fpython-jobs-3',
        'gid': 'LOCATION,INDUSTRY,EDUCATION,FAREA_ROLE',
        # 'referer': 'https://www.naukri.com/python-jobs-3?k=python',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'systemid': '109',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
        }
    return headers

def make_request(url,headers):

    response = requests.get(url,headers=headers,timeout=30)
    print(response.status_code)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        pass
        with open('Naukri_excetpionFile_' + str(dat) + '.csv', 'a', newline='', encoding='UTF-8') as fp:
            writer = csv.writer(fp)
            writer.writerow([url, 'status!=200'])

def page_count(data):

    try:
        pagenumber = math.ceil(int(data['noOfJobs'])/20)
    except:
        pagenumber = 1

    return pagenumber

def get_product_data(data,recordno,page):

    try:
        for item in data['jobDetails']:
            recordno+=1
            global exp,exp1
            print(f'Overall_Record_Number: {recordno}')
            try:
                name = (item['title'])
            except:
                name=''
            try:
                companyname = (item['companyName'])
            except:
                companyname=''
            try:
                jobdescription = (item['jobDescription'])
            except:
                jobdescription=''
            try:
                posted = (item['footerPlaceholderLabel'])
            except:
                posted=''
            try:
                joburl = (item['jdURL'])
            except:
                joburl=''
            try:
                tag = (item['tagsAndSkills'])
            except:
                tag=''
            finalurl = f'https://www.naukri.com{joburl}'
            print(f'JobTitle: {name}')
            print(f'Name of the company: {companyname}')
            print(f'Description: {jobdescription}')
            print(f'Skilled Required: {tag}')
            for holder in (item['placeholders']):
                try:
                    exp = (holder['label'])
                except:
                    exp=''
                try:
                    exp1 = (holder['type'])
                except:
                    exp1=''
                print(f'More details: {exp},{exp1}')
            print(finalurl)
            print(f'Job Posted: {posted}')

            with open('Naukri_PythonDev_' + str(dat) + '.csv', 'a', newline='', encoding='UTF-8') as fp:
                writer = csv.writer(fp)
                writer.writerow([page, recordno,'naukri.com', name,companyname,jobdescription,tag,exp,exp1,posted,finalurl])
    except Exception as e:
        with open('Naukri_excetpionFile_' + str(dat) + '.csv', 'a', newline='', encoding='UTF-8') as fp:
            writer = csv.writer(fp)
            writer.writerow([url, str(e)])

def main(url):
    try:
        headers =header()
        response = make_request(url,headers)
        pagenumber = page_count(response)
        recordno = 0
        for page in range(1,pagenumber+1):
            url = f'https://www.naukri.com/jobapi/v3/search?noOfResults=20&urlType=search_by_keyword&searchType=adv&keyword=python&pageNo={page}&sort=r&k=python&seoKey=python-jobs-3&src=jobsearchDesk&latLong=&sid=16751982235515507'
            response = make_request(url,headers)
            get_product_data(response,recordno,page)
    except Exception as e:
        print(e)
        with open('Naukri_excetpionFile_' + str(dat) + '.csv', 'a', newline='', encoding='UTF-8') as fp:
            writer = csv.writer(fp)
            writer.writerow([url, str(e)])

if __name__ == '__main__':

    url = 'https://www.naukri.com/jobapi/v3/search?noOfResults=20&urlType=search_by_keyword&searchType=adv&keyword=python&pageNo=1&sort=r&k=python&seoKey=python-jobs-3&src=jobsearchDesk&latLong=&sid=16751982235515507'
    main(url)
