import scrapy
import re

class lichessSpider(scrapy.Spider):
    name = "lichessSpider"

    def start_requests(self):
        url = 'https://lichess.org/coach/all/all/login?page=1'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        coach_handles = response.xpath("//a[@class='overlay']/@href").getall()
        for coach_handle in coach_handles:
            yield response.follow(url="https://lichess.org"+coach_handle, callback=self.parse_coach)
        current_page = int(response.url.split('=')[-1])
        if len(coach_handles) == 0:
            return
        #if current_page > 2:
        #    return 
        next_page = response.url.split('page')[0] + 'page=' + str(current_page + 1)
        yield scrapy.Request(url=next_page, callback=self.parse)

    def parse_coach(self,response):
         yield {'name': response.xpath("//div[@class='overview']/h1[@class='coach-name']/text()").get(),
                'headline': response.xpath("//div[@class='overview']/p[@class='headline large']/text()").get(),
                'languages': response.xpath("//tr[@class='languages']/td/text()").getall(),
                'location': response.xpath("//span[@class='location']/text()").get(),
                'rate': response.xpath("//tr[@class='rate']/td/text()").get(),
                'rating_fide': response.xpath("//tr[@class='rating']/td/text()").get(),
                'rating_bullet': response.xpath("//span[contains(@title, 'Bullet rating')]/text()").get(),
                'rating_blitz': response.xpath("//span[contains(@title, 'Blitz rating')]/text()").get(),
                'rating_rapid': response.xpath("//span[contains(@title, 'Rapid rating')]/text()").get(),
                'about': response.xpath("//h2[contains(text(),'About')]/following-sibling::div/text()").get(),
                'playing_experience': response.xpath("//h2[contains(text(),'Playing')]/following-sibling::div/text()").get(),
                'teaching_experience': response.xpath("//h2[contains(text(),'Teaching')]/following-sibling::div/text()").get(),
                'other_experience': response.xpath("//h2[contains(text(),'Other')]/following-sibling::div/text()").get(),
                'best_skills': response.xpath("//h2[contains(text(),'Best')]/following-sibling::div/text()").get(),
                'teaching_methodology': response.xpath("//h2[contains(text(),'methodology')]/following-sibling::div/text()").get()        
            }
         

class lichessSpider_basic(scrapy.Spider):
    name = "lichessSpider_basic"

    def start_requests(self):
        url = 'https://lichess.org/coach/all/all/login?page=1'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        coaches = response.xpath("//article[@class='coach-widget paginated']")
        for coach in coaches:
            yield {'name': coach.xpath(".//div/h2[@class='coach-name']/text()").get(),
                    'headline': coach.xpath(".//div/p[@class='headline small']/text()").get(),
                    'languages': coach.xpath(".//tr[@class='languages']/td/text()").getall(),
                    'location': coach.xpath(".//span[@class='location']/text()").get(),
                    'rating_fide': coach.xpath(".//tr[@class='rating']/td/text()").get(),
                    'rating_bullet': coach.xpath(".//span[contains(@title, 'Bullet rating')]/text()").get(),
                    'rating_blitz': coach.xpath(".//span[contains(@title, 'Blitz rating')]/text()").get(),
                    'rating_rapid': coach.xpath(".//span[contains(@title, 'Rapid rating')]/text()").get(),
                    'rate': coach.xpath(".//tr[@class='rate']/td/text()").get(),
            }
        current_page = int(response.url.split('=')[-1])
        if len(coaches) == 0:
            return
        #if current_page > 2:
        #    return 
        next_page = response.url.split('page')[0] + 'page=' + str(current_page + 1)
        yield scrapy.Request(url=next_page, callback=self.parse)