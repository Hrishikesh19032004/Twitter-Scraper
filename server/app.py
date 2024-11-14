import time
import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import traceback


app = Flask(__name__)
CORS(app)

# Initialize WebDriver
def init_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    return driver

# Scrape User Profile Data
def scrape_twitter_data(driver, url):
    driver.get(url)
    wait = WebDriverWait(driver, 10)
    
    try:
        # Scrape username
        username = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'h1[role="heading"] span'))).text
        
        # Scrape profile name 
        profile_name = "Name not available"
        try:
            profile_name = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'div[data-testid="UserName"] span'))).text
        except:
            pass
        
        # Scrape bio
        bio = "No bio available"
        try:
            bio = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'div[data-testid="UserDescription"]'))).text
        except:
            pass
        
        # Scrape following count
        following = "Following count not found"
        try:
            following = wait.until(EC.presence_of_element_located(
                (By.XPATH, '//a[contains(@href,"/following")]/span[1]/span'))).text
        except:
            pass
        
        # Scrape followers count
        followers = "Followers count not found"
        try:
            followers = wait.until(EC.presence_of_element_located(
                (By.XPATH, '//a[contains(@href,"/followers")]/span[1]'))).text
        except:
            pass

        # Scrape profile image URL
        profile_image_url = "Profile image not found"
        try:
            profile_image_url = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'div.css-175oi2r img'))).get_attribute('src')
        except:
            pass

        # Optional fields 
        location = "Location not found"
        website = "Website not found"

        try:
            location = driver.find_element(By.CSS_SELECTOR, 'span[data-testid="UserLocation"]').text
        except:
            pass
        
        try:
            website = driver.find_element(By.CSS_SELECTOR, 'a[data-testid="UserUrl"]').get_attribute('href')
        except:
            pass

        user_data = {
            "url": url,
            "username": username,
            "profile_name": profile_name,
            "bio": bio,
            "following": following,
            "followers": followers,
            "location": location,
            "website": website,
            "profile_image_url": profile_image_url
        }

        # Save user data to CSV
        df = pd.DataFrame([user_data])
        df.to_csv('user_data.csv', mode='a', header=False, index=False)

        return user_data

    except Exception as e:
        return {"error": str(e), "traceback": traceback.format_exc()}

# Scrape Posts
def scrape_posts(driver, url):
    driver.get(url)
    wait = WebDriverWait(driver, 10)
    posts_data = []

    try:
        posts = wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, 'article')))[:20]  
        
        for post in posts:
            content = post.text
            posts_data.append({"content": content})
        
        # Save posts to CSV
        pd.DataFrame(posts_data).to_csv('post_data.csv', mode='a', header=False, index=False)

    except Exception as e:
        return {"error": str(e), "traceback": traceback.format_exc()}

    return posts_data

# Flask route to handle scraping
@app.route('/scrape', methods=['POST'])
def scrape_twitter():
    try:
        data = request.json
        twitter_urls = data.get('urls') 

        if not twitter_urls or not isinstance(twitter_urls, list):
            return jsonify({"error": "URLs are required and should be a list"}), 400

        driver = init_driver()
        all_user_data = []
        all_posts_data = []

        
        for url in twitter_urls:
            try:
                user_data = scrape_twitter_data(driver, url)
                if "error" in user_data:
                    print(f"Error scraping data for {url}: {user_data['error']}")
                    continue  
                
                posts_data = scrape_posts(driver, url)
                all_user_data.append(user_data)
                all_posts_data.append(posts_data)
            except Exception as e:
                print(f"Error processing {url}: {str(e)}")
                continue 

        driver.quit()

        return jsonify({
            "user_data": all_user_data,
            "posts_data": all_posts_data
        }), 200

    except Exception as e:
        error_msg = traceback.format_exc()
        print(f"Error occurred: {error_msg}")
        return jsonify({"error": "An error occurred", "details": error_msg}), 500

if __name__ == '__main__':
    app.run(debug=True, port=7000)
