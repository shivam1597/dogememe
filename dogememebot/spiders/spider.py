import scrapy
from scrapy.http import Request
from ..items import DogememebotItem

class UserNameSpider(scrapy.Spider):
    name = "spider"


    def start_requests(self):
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--disable-dev-shm-usage")
        # chrome_options.add_argument("--no-sandbox")
        # driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
        # driver = webdriver.Chrome(r'C:\\chromedriver.exe', chrome_options=chrome_options)
        # maximize the window size
        # driver.implicitly_wait(1)
        # driver.get('https://www.instagram.com/login')        
        # driver.find_element_by_css_selector('input[name="username"]').send_keys('wintersolstudios@gmail.com')
        # time.sleep(2)
        # driver.find_element_by_css_selector('input[name="password"]').send_keys('Shivam@15')
        # time.sleep(5)
        # login_button = driver.find_element_by_xpath("//button[@type='submit']")
        # login_button.click()
        # time.sleep(8)
        # cookie_list = driver.get_cookies()
        # cookie_string = ''
        # for value in cookie_list:
        #     cookie_string = cookie_string + value['name'] + '=' + value['value'] + ';'
        # cookie_to_use = cookie_string[:-1]
        headers = {
            "sec-ch-ua-platform": "Windows",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "user-agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
            "cookie": """rur="EAG\05453735628921\0541690786105:01f768b4405eaf1b8fc84e3db032c39bb24616b4cfcd513819a327d2b489db28305be8de";shbid="8181\05453735628921\0541690786102:01f7924647932e0667f5a47bfd2a835c27282c41dce9589c18db15496747b49f7887dc2a";shbts="1659250102\05453735628921\0541690786102:01f720a4b3fe66c951d1a719d5701052a66d52bf4861812227faa0c28e9a80f57985669b";sessionid=53735628921%3AuJ8yBFDyUqMilm%3A8%3AAYd7BUwAOAxbCanvb045HVQck9TDW2zLDra4SdEfhg;csrftoken=WtAMEO1TXJEjoxwwsY1ZvrjSEE3Oto8M;ig_nrcb=1;ds_user_id=53735628921;ig_did=BF45CC2B-500F-43AE-96E0-BB931815BC05;mid=YuYlqgALAAGBbYIikEiicHHLFk7x;""",
            "x-ig-app-id": "936619743392459",
        }
        user_ids = self.settings.get('USER_IDS')
        for id in user_ids:
            end_cursor = "}"
            #1485933718
            #https://www.instagram.com/graphql/query/?query_hash=8c2a529969ee035a5063f2fc8602a0fd&variables={"id":"1485933718","first":"12"}
            url = 'https://www.instagram.com/graphql/query/?query_hash=8c2a529969ee035a5063f2fc8602a0fd&variables={"id":' + '"' + id + '"' + ',' + '"first":"12"'.format(id) + end_cursor
            yield Request(
                url=url,
                headers=headers,
                callback=self.parse,
                meta={
                "cookie_string": """rur="EAG\05453735628921\0541690786105:01f768b4405eaf1b8fc84e3db032c39bb24616b4cfcd513819a327d2b489db28305be8de";shbid="8181\05453735628921\0541690786102:01f7924647932e0667f5a47bfd2a835c27282c41dce9589c18db15496747b49f7887dc2a";shbts="1659250102\05453735628921\0541690786102:01f720a4b3fe66c951d1a719d5701052a66d52bf4861812227faa0c28e9a80f57985669b";sessionid=53735628921%3AuJ8yBFDyUqMilm%3A8%3AAYd7BUwAOAxbCanvb045HVQck9TDW2zLDra4SdEfhg;csrftoken=WtAMEO1TXJEjoxwwsY1ZvrjSEE3Oto8M;ig_nrcb=1;ds_user_id=53735628921;ig_did=BF45CC2B-500F-43AE-96E0-BB931815BC05;mid=YuYlqgALAAGBbYIikEiicHHLFk7x;""",
                "user_id": id
                }
            )

    def parse(self, response):
        item = DogememebotItem()
        response_object = response.json()
        id = response.meta.get('user_id')
        cookie_string = response.meta.get('cookie_string')
        self.logger.info(cookie_string)
        headers = {
            "sec-ch-ua-platform": "Windows",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "user-agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
            "cookie": """rur="EAG\05453735628921\0541690786105:01f768b4405eaf1b8fc84e3db032c39bb24616b4cfcd513819a327d2b489db28305be8de";shbid="8181\05453735628921\0541690786102:01f7924647932e0667f5a47bfd2a835c27282c41dce9589c18db15496747b49f7887dc2a";shbts="1659250102\05453735628921\0541690786102:01f720a4b3fe66c951d1a719d5701052a66d52bf4861812227faa0c28e9a80f57985669b";sessionid=53735628921%3AuJ8yBFDyUqMilm%3A8%3AAYd7BUwAOAxbCanvb045HVQck9TDW2zLDra4SdEfhg;csrftoken=WtAMEO1TXJEjoxwwsY1ZvrjSEE3Oto8M;ig_nrcb=1;ds_user_id=53735628921;ig_did=BF45CC2B-500F-43AE-96E0-BB931815BC05;mid=YuYlqgALAAGBbYIikEiicHHLFk7x;""",
            "x-ig-app-id": "936619743392459",
        }
        end_cursor = "}"
        if response_object:
            main_json = response_object['data']['user']
            if main_json:
                all_posts = main_json['edge_owner_to_timeline_media']['edges']
                for edge in all_posts:
                    is_video = edge['node']['is_video']
                    if not is_video:
                        item['image_url'] = edge['node']['display_url']
                        item['shortcode'] = edge['node']['shortcode']
                        caption_edge = edge['node']['edge_media_to_caption']['edges']
                        if caption_edge:
                            caption = caption_edge[0]['node']['text'].replace('\n', '')
                            caption_partition = caption.partition('#')
                            hashtags = '#{}'.format(caption_partition[2])
                            item['hashtags'] = hashtags
                        item['username'] = edge['node']['owner']['username']
                        item['id'] = edge['node']['owner']['id']
                        item['time_posted'] = edge['node']['taken_at_timestamp']
                        # additional_posts = edge['node'].get('edge_sidecar_to_children')
                        # if additional_posts:
                        #     if additional_posts['edges']:
                        #         for post, idx in enumerate(additional_posts['edges'], start=0):
                        #             is_video = post['node']['is_video']
                        #             if not is_video:
                        #                 item['side_image{}'.format(idx)] = post['node']['display_url']
                        yield item
            if response_object['data']['user']['edge_owner_to_timeline_media']['page_info']['has_next_page']:
                end_cursor = ',"after":"'+ response_object['data']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']+'"}'
                url = 'https://www.instagram.com/graphql/query/?query_hash=8c2a529969ee035a5063f2fc8602a0fd&variables={"id":' + '"' + response.meta.get('user_id') + '"' + ',' + '"first":"12"' + end_cursor
                yield Request(
                    url,
                    headers=headers,
                    callback=self.parse,
                    meta={
                    "cookie_string":cookie_string,
                    "user_id": id
                    }
                )