from constants import *
from secrets_and_config import * #coud replace with .env
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from colorama import just_fix_windows_console, Back

def register_classes():
    just_fix_windows_console()

    driver = webdriver.Chrome()
    # driver.implicitly_wait(10)
    wait = WebDriverWait(driver, timeout=15)

    def find_element(css_selector:str):
        return driver.find_element(by=By.CSS_SELECTOR, value=css_selector)
    def find_elements(css_selector:str):
        return driver.find_elements(by=By.CSS_SELECTOR, value=css_selector)
    # def wait_until_displayed(element):
    #     wait.until(lambda d : element.is_displayed())


    def sign_in_cuny_first():
        username = find_element("#CUNYfirstUsernameH")
        password = find_element("#CUNYfirstPassword")
        submit = find_element("#submit")

        username.clear()
        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        submit.click()


    # main script starts
    driver.get(SB_URL)

    # sign in
    sign_in_button = find_element(".sign_in_button")
    sign_in_button.click()
    sign_in_cuny_first()



    time.sleep(5)
    #load favorite schedule
    favorites_tab = find_element(".link_favorites")
    wait.until(lambda d : favorites_tab.is_displayed())
    favorites_tab.click()

    desired_favorite = find_element(f'[title^="{DESIRED_FAVORITE_TITLE}"]')
    desired_favorite.click()
    time.sleep(2)
    find_element(".load_button").click()


    #get schedule
    time.sleep(2)
    get_button = find_element(".button_get_schedule")
    get_button.click()


    #TODO: add to waitlist support
    # find_elements("...")

    # sign up
    final_button = find_element(".button_do_actions")
    wait.until(lambda d : final_button.is_displayed())
    final_button.click()


    # Check if success
    wait.until(lambda d : find_element(".actionResult").is_displayed())
    # len(find_elements(".actionResult")) > 0
    print("\n")
    for failure in find_elements(".actionFailMessage"):
        print(Back.RED + f"Failed to add class: " + Back.RESET + f"\"{failure.text}\"")

    #TODO
    # for success in find_elements(".actionSuccessMessage"): #no idea if this works
    #     print(Back.GREEN + f"ADDED CLASS: " + Back.RESET + f"\"{success.text}\"")
    print("\n(this program probably can not yet detect succeeded classes only lack of any failures.)\n")


    if len(find_elements(".actionFailMessage")) == 0:
        print(Back.GREEN + "NO FAILURES WOOP WOOP!" + Back.RESET)
        succeeded = True
    else:
        succeeded = False



    time.sleep(1)
    driver.quit()

    if succeeded:
        print("Done, SUCCEEDED")
    else:
        print("Done, not successful")
    return succeeded

