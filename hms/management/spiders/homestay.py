import logging

import scrapy
import re
from hms.models import Homestay


class HomestayDotCom(scrapy.Spider):
    name = 'homestay'
    reup_database = True
    DEBUG = False
    post_header = {'Host': 'secure.homestaymanager.com',
                   'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0',
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                   'Accept-Language': 'en-US,en;q=0.5',
                   'Accept-Encoding': 'gzip, deflate, br',
                   'Connection': 'keep-alive',
                   # 'Cookie': '__cfduid=d9616cf74d78a86b22a18b7be8042ee821586833240; cf_clearance=e52920e300d688afc773c90a3f64d97a2bc525e5-1586833240-0-250',
                   'Upgrade-Insecure-Requests': '1',
                   'If-None-Match': 'W/"c4200d67425cdd4758e69d6a5e007586"',
                   'Cache-Control': 'max-age=0',
                   'TE': 'Trailers',
                   }

    def start_requests(self):
        if not self.DEBUG:
            urls = [
                'https://www.homestay.com/homestays/search?utf8=%E2%9C%93&search_type=search_box&latitude=&longitude=&country_code=&ne_lat=&ne_lng=&sw_lat=&sw_lng=&radius=&type=&order=&location_id=66173&google_place_id=&price_filter_nights=1&location=Hanoi%2C+Vietnam&check_in=&check_out=&guests=1&min_price=&max_price=&price_filter_currency=VND&price_bracket=&meals_provided=0&self_catering=0&accept_male=0&accept_female=0&accept_couples=0&accept_families=0&accept_students=0&no_pets=0&cooking=0&golf=0&tennis=0&hiking=0&cycling=0&wheelchair_accessible=0&wifi=0&tv=0&garden=0&bikes=0&parking=0&swimming_pool=0&gym=0',
            ]

            for url in urls:
                yield scrapy.Request(url, callback=self.parse_list)
        else:
            urls = ['https://www.homestay.com/vietnam/hanoi/145868-homestay-in-nhan-chinh-hanoi']
            for url in urls:
                yield scrapy.Request(url, callback=self.parse_detail)

    def parse_list(self, response):
        links = response.xpath('//a[@class="profile-link"]/@href').getall()
        for link in links:
            yield scrapy.Request('https://homestay.com' + link, callback=self.parse_detail)

    def parse_detail(self, response):
        cookie = response.headers.getlist('Set-Cookie')[0]
        logging.info(cookie)
        homestay_id = re.search(r'/(\d+)-[^/]+', response.url)
        if homestay_id is not None:
            homestay_id = homestay_id.group(1)

        image_urls = []
        for div in response.xpath('//div[@class="gallery"]//ul/li/div')[:2]:
            image_urls.append(div.xpath('@data-image').get())
        # yield scrapy.Request(image_urls[0], callback=self.debug_image)
        homestay = Homestay.objects.filter(homestay_dot_com_id=homestay_id)
        if homestay.exists():
            if self.reup_database:
                homestay = homestay[0]
            else:
                return
        else:
            homestay = Homestay(homestay_dot_com_id=homestay_id)
        item = {'from': 'homestay.com', 'response': response, 'model': homestay, 'image_urls': image_urls, 'images': scrapy.Field()}
        return item

    def debug_image(self, response):
        self.log(response.headers)