import info 
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from random import randint


class Bot : 
    def __init__(self) : 
        self.webdriver = webdriver.Firefox()
        self.username = info.username
        self.password = info.password
        self.login(self.username, self.password) 
        
       
    def login(self, username, password) : 
        "Login to instagram account"


        # Open instagram.com
        self.webdriver.get("https://www.instagram.com/")

        sleep(2)

        # Find username box and enter username 
        self.username_box = self.webdriver.find_element(By.NAME, "username")
        self.username_box.send_keys(username)

        sleep(2)

        # find the password box and enter the password
        self.password_box = self.webdriver.find_element(By.NAME, "password")
        self.password_box.send_keys(password) 

        sleep(2)

        # Click the log in button 
        self.webdriver.find_element(By.XPATH,
        "/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button").click()
        

        sleep(3)
        print(f"Login to page {username}")

    def Like_Posts_of_a_page(self , page_ID : str) : 
        "Like the post in page"

        # Open the page
        self.webdriver.get(f"https://www.instagram.com/{page_ID}/")
        sleep(2)

        #Scroll 
        for i in range(8) : 
            self.webdriver.execute_script("window.scrollTo(0,document.body.scrollHeight)") 
            sleep(2)


        sleep(3)

        # Get href attribute of all element in the page
        href = self.webdriver.find_elements(By.TAG_NAME , 'a')
        
        # Cut the post url and save un post_URL 
        post_URL = [element.get_attribute("href") for element in href if "https://www.instagram.com/p" in element.get_attribute("href")]

        # Open posts one by one 
        for URL in post_URL : 
            self.webdriver.get(URL)
            sleep(3.5)

            # Click the like button 
            self.webdriver.find_element(By.XPATH,
             "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button/div[2]").click()

            sleep(randint(2 , 30))
            
    def Close_Browser(self) : 
        "CLose the Browser"
        self.webdriver.close()
        print("Browser is close!")

    
    def Follow_The_pages(self, *args) :
        "Follow your pages ID automatically!"
    
        if len(args) == 1 : 
            self.webdriver.get(f"https://www.instagram.com/{args}/")
            sleep(3)

            # CLick The Follow button 
            self.webdriver.find_element(By.XPATH, 
            "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/button").click()
            print(f"You are Following '{args}'")

        elif len(args) != 1 : 
            for page in args : 
                self.webdriver.get(f"https://www.instagram.com/{page}/")
                sleep(3)

                # CLick The Follow button 
                self.webdriver.find_element(By.XPATH, 
                "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/button").click()
                print(f"You are Following '{page}'")

                sleep(2)

    def Log_Out_Account(self) : 
        "Log out of account" 

        # Go to profile
        self.webdriver.get("https://www.instagram.com/%s/" %self.username)

        sleep(2)

        # CLick the account logo 
        self.webdriver.find_element(By.XPATH, 
        "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[1]/span/img").click()

        sleep(2)

        # CLick to "Log Out" button 
        self.webdriver.find_element(By.XPATH, 
        '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div/div[2]/div[5]/div/div/div/div/div/div').click()

        print("Log Out Successfully!")

    def Unfollow_Pages(self, *args) : 
        "Unfollow your pages ID automatically!"

        if len(args) == 1 : 
            # Go to page 
            self.webdriver.get(f'https://www.instagram.com/{args}/')
            sleep(2)
            
            # Click the unfollow button 
            self.webdriver.find_element(By.XPATH,
             '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/button').click()

            print(f"You don't follow the '{args}' page anymore")

        elif len(args) != 1 : 
            for page in args : 
                # Go to page 
                self.webdriver.get(f'https://www.instagram.com/{page}/')

                sleep(2)

                # Click the unfollow button 
                self.webdriver.find_element(By.XPATH,
                '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/button').click()

                sleep(0.5)

                # Click the unfollow button in pop up 
                self.webdriver.find_element(By.XPATH, 
                "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[1]").click()

                sleep(3)

                print(f"You don't follow the '{page}' page anymore")


    def Like_Posts_in_hashtag(self , hashtag) : 
        "Liking the posts of a hashtag"
        # Sleep after login
        sleep(3)

        # Go to hashtag page
        self.webdriver.get(f"https://www.instagram.com/explore/tags/{hashtag}/")

        sleep(3)

        # Scroll 
        for i in range(10) : 
            self.webdriver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            sleep(2)

        hrefs = self.webdriver.find_elements(By.TAG_NAME , 'a')
        post_hrefs = [element.get_attribute('href') for element in hrefs if ".com/p" in element.get_attribute('href')]
        
        # Checking the non-duplication of posts in a hashtag

        uniq_post_hrefs = []
        for post_href in post_hrefs : 
            if post_href not in uniq_post_hrefs : 
                uniq_post_hrefs.append(post_href)

        # Open Post one by one 
        for post in uniq_post_hrefs : 
            self.webdriver.get(post)
            sleep(3)

            # Click "heart" button 
            self.webdriver.find_element(By.XPATH,
             '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button').click()

            # Sleep between 2 and 30 seconds
            sleep(randint(2, 30))


def main() : 
    my_bot = Bot()
    my_bot.Like_Posts_in_hashtag("python")

if __name__ == '__main__' : 
    main()