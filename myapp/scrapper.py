import requests
from bs4 import BeautifulSoup


def remove_u(text):
    string_encode = text.encode("ascii", "ignore")
    string_decode = string_encode.decode()
    return string_decode


def scrape():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }

    url = "https://www.amazon.in/s?bbn=976419031&rh=n%3A976419031%2Cp_89%3Arealme&dc&qid=1624216249&rnid=3837712031&ref=lp_976420031_nr_p_89_3"
    res = requests.post(url, headers=headers)
    if res.status_code != 200:
        return
    soup = BeautifulSoup(res.content, 'html.parser')
    all = soup.find_all(
        class_="sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col sg-col-4-of-20")

    main_l = []

    for el in all:
        detail_dict = {}
        soup_name = BeautifulSoup(str(el), 'html.parser')
        name = soup_name.find_all(
            class_="a-size-base-plus a-color-base a-text-normal")[0].get_text()
        link = 'https://www.amazon.in' + \
            soup_name.find_all(
                class_="a-link-normal s-no-outline", href=True)[0]['href']
        product_res = requests.post(link, headers=headers)
        if product_res.status_code != 200:
            pass
        product_soup = BeautifulSoup(product_res.content, 'html.parser')
        details_table = product_soup.find(
            id="productDetails_techSpec_section_1")
        details_soup = BeautifulSoup(str(details_table), 'html.parser')
        details = details_soup.find_all('tr')
        img_div = product_soup.find(id="imgTagWrapperId")
        img_soup = BeautifulSoup(str(img_div), 'html.parser')
        img = img_soup.find(id="landingImage", src=True)['src']
        try:
            rating = product_soup.find(
                class_='a-icon-alt').get_text().split(' ')[0]
        except:
            rating = '0'
        detail_dict['name'] = name
        detail_dict['link'] = link
        detail_dict['rating'] = float(rating)
        print(detail_dict['rating'])
        try:
            price = product_soup.find(id="priceblock_dealprice")
            detail_dict['price'] = price.get_text()
        except:
            try:
                price = product_soup.find(id="priceblock_ourprice")
                detail_dict['price'] = price.get_text()
            except:
                detail_dict['price'] = 'Not Available'
        detail_dict['img'] = img
        d = {}
        for detail in details:
            dsoup = BeautifulSoup(str(detail), 'html.parser')
            feature_name = remove_u(dsoup.find(
                'th').get_text()).rstrip('\n').replace('\n', '')
            feature_detail = remove_u(dsoup.find(
                'td').get_text()).rstrip('\n').replace('\n', '')
            d[feature_name] = feature_detail
            # print(feature_name,'-->', feature_detail)
            # break
        # print(details_table)
        detail_dict['features'] = d
        main_l.append(detail_dict)
        # break

    return main_l
