import unittest
import time
import random
from faker import Faker
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import WebDriverException as WDE
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
import AllureReports


fake = Faker()
def delay():
    time.sleep(random.randint(1, 3))

class Tesla_ModelY_Positive(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_01(self):

        driver = self.driver
        self.driver.maximize_window()
        driver.get('https://www.tesla.com/')

    # Verify (do assert) "Tesla" in website title
        try:
            assert "Electric Cars, Solar & Clean Energy | Tesla" in driver.title
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)

    # Verify Model Y Page
        try:
            driver.execute_script("window.scrollTo(0, 700)")
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Order Now')])[1]").click()
            delay()
            driver.find_element(By.CLASS_NAME, "tds-site-logo-link")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            driver.execute_script("window.scrollTo(0, 0)")

            # Scrolling right carousel
            right_arrow = driver.find_element(By.XPATH, "//body/div[@id='root']/div[3]/main[1]/section[1]/div[1]/div[1]/button[2]/*[1]")
            for _ in range(4):
                right_arrow.click()
                delay()
            print("----Right scroll 4 times completed")

            # Scrolling left carousel
            left_arrow = driver.find_element(By.XPATH, "//body/div[@id='root']/div[3]/main[1]/section[1]/div[1]/div[1]/button[1]/*[1]")
            for _ in range(4):
                left_arrow.click()
                delay()
            print("----Left scroll 4 times completed")

            print("TC-1 passed. Page Model Y is correct")
        except NoSuchElementException:
            print("TC-1 failed. Is there something wrong")

        self.driver.quit()

    def test_02(self):

        driver = self.driver
        self.driver.maximize_window()
        driver.get('https://www.tesla.com/')


    # Verify Model Y Page/Cash
        try:
            driver.execute_script("window.scrollTo(0, 700)")
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Order Now')])[1]").click()
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Model Y')])[1]")

            driver.execute_script("document.body.style.zoom = '0.75'")
            delay()

            driver.find_element(By.XPATH, "//button[@id='cash']").click()
            driver.find_element(By.XPATH, "//span[contains(text(),'Long Range Rear-Wheel Drive')]").click()
            driver.find_element(By.XPATH, "//span[contains(text(),'Long Range All-Wheel Drive')]").click()
            driver.find_element(By.XPATH, "//span[contains(text(),'Performance All-Wheel Drive')]").click()
            driver.find_element(By.XPATH, "(//input[contains(@type,'checkbox')])[1]").click()
            driver.find_element(By.XPATH, "(//input[contains(@type,'checkbox')])[1]").click()

            # Verify that all indicators price has been calculated
            try:
                driver.find_element(By.XPATH, "//span[contains(text(),'337')]")
                driver.find_element(By.XPATH, "//span[contains(text(),'135')]")
                driver.find_element(By.XPATH, "//span[contains(text(),'6.5')]")
                print("All indicators has been calculated correct.")
            except NoSuchElementException:
                print("Estimated amounts have changed.")

            driver.find_element(By.XPATH, "//span[contains(text(),'Edit Savings')]").click()
            delay()
            driver.find_element(By.XPATH, "//h2[contains(text(),'Financing Options')]")
            driver.find_element(By.XPATH, "(//input[@type='checkbox'])[1]").click()
            driver.find_element(By.XPATH, "(//input[@type='checkbox'])[1]").click()
            driver.find_element(By.XPATH, "(//input[@type='checkbox'])[2]").click()
            driver.find_element(By.XPATH, "(//input[@type='checkbox'])[2]").click()
            driver.find_element(By.XPATH, "(//input[@type='checkbox'])[3]").click()
            driver.find_element(By.XPATH, "//span[contains(text(),'View Criteria')]").click()
            delay()
            driver.find_element(By.XPATH, "//span[contains(text(),'Eligibility Criteria')]")
            driver.find_element(By.XPATH, "//body/div[@id='root']/div[3]/div[1]/dialog[1]/section[1]/div[2]/div[1]/button[1]/*[1]").click()
            driver.find_element(By.XPATH, "//span[contains(text(),'Show Details')]").click()
            delay()
            driver.find_element(By.XPATH, "//span[contains(text(),'Est. Taxes & Fees')]")
            driver.find_element(By.XPATH, "//body/div[@id='root']/div[3]/div[1]/dialog[1]/section[1]/div[2]/div[1]/button[1]/*[1]").click()
            driver.find_element(By.XPATH, "//span[contains(text(),'Customize')]").click()
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Gas Savings')])[1]")

            driver.find_element(By.ID, "fuelEfficiency").send_keys("u'\ue009' + u'\ue003'")
            driver.find_element(By.ID, "fuelEfficiency").send_keys("23")
            driver.find_element(By.ID, "distance").send_keys("u'\ue009' + u'\ue003'")
            driver.find_element(By.ID, "distance").send_keys("15000")
            driver.find_element(By.ID, "fuelPrice").send_keys("u'\ue009' + u'\ue003'")
            driver.find_element(By.ID, "fuelPrice").send_keys("3.8")
            driver.find_element(By.ID, "electricityPrice").send_keys("u'\ue009' + u'\ue003'")
            driver.find_element(By.ID, "electricityPrice").send_keys("0.15")
            delay()

            # Verify that the amount est. gas savings has been calculated
            try:
                driver.find_element(By.XPATH, "(//span[contains(.,'$9,500')])[2]")
                print("The amount est. gas savings has been calculated.")
            except NoSuchElementException:
                print("Est. gas savings amounts have changed.")

            driver.close()

            print("TC-2 passed. Information Model Y/Cash is correct")
        except NoSuchElementException:
            print("TC-2 failed. Is there something wrong")

        self.driver.quit()

    def test_03(self):

        driver = self.driver
        self.driver.maximize_window()
        driver.get('https://www.tesla.com/')

    # Verify Model Y Page/Lease
        try:
            driver.execute_script("window.scrollTo(0, 700)")
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Order Now')])[1]").click()
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Model Y')])[1]")

            driver.execute_script("document.body.style.zoom = '0.65'")
            delay()

            driver.find_element(By.XPATH, "//button[@id='finplat.AUTO_LEASE:OPERATIONAL_LEASE:CT_PRIVATE']").click()
            driver.find_element(By.XPATH, "//span[contains(text(),'Long Range Rear-Wheel Drive')]").click()
            driver.find_element(By.XPATH, "//span[contains(text(),'Long Range All-Wheel Drive')]").click()
            driver.find_element(By.XPATH, "//span[contains(text(),'Performance All-Wheel Drive')]").click()
            driver.find_element(By.XPATH, "(//input[@type='checkbox'])[1]").click()
            driver.find_element(By.XPATH, "(//input[@type='checkbox'])[1]").click()

            # Verify that all indicators price has been calculated
            try:
                driver.find_element(By.XPATH, "//span[contains(text(),'277')]")
                driver.find_element(By.XPATH, "//span[contains(text(),'155')]")
                driver.find_element(By.XPATH, "//span[contains(text(),'3.5')]")
                print("All indicators has been calculated correct.")
            except NoSuchElementException:
                print("Estimated amounts have changed.")

            driver.find_element(By.XPATH, "//span[contains(text(),'Edit Terms & Savings')]").click()
            delay()
            driver.find_element(By.XPATH, "//h2[contains(text(),'Financing Options')]")
            driver.find_element(By.XPATH, "//input[@id='cashDownPayment']").send_keys("u'\ue009' + u'\ue003'")
            driver.find_element(By.XPATH, "//input[@id='cashDownPayment']").send_keys("5000")
            dp_down = driver.find_element(By.XPATH, "(//button[contains(@aria-haspopup,'listbox')])[1]")
            dp_down.send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, "//li[@id='termLength-listbox-24']").click()
            time.sleep(1)
            dp_down = driver.find_element(By.XPATH, "(//button[contains(@aria-haspopup,'listbox')])[2]")
            dp_down.send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, "//li[@id='distanceAllowed-listbox-15000']").click()
            time.sleep(1)

            driver.find_element(By.XPATH, "(//input[@type='checkbox'])[1]").click()
            driver.find_element(By.XPATH, "(//input[@type='checkbox'])[1]").click()
            driver.find_element(By.XPATH, "(//input[@type='checkbox'])[2]").click()
            driver.find_element(By.XPATH, "//span[contains(text(),'Show Details')]").click()
            delay()
            driver.find_element(By.XPATH, "//span[contains(text(),'Est. Taxes & Fees')]")
            driver.find_element(By.XPATH, "//body/div[@id='root']/div[3]/div[1]/dialog[1]/section[1]/div[2]/div[1]/button[1]/*[1]").click()
            driver.find_element(By.XPATH, "//span[contains(text(),'Customize')]").click()
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Gas Savings')])[1]")
            driver.find_element(By.ID, "fuelEfficiency").send_keys("u'\ue009' + u'\ue003'")
            driver.find_element(By.ID, "fuelEfficiency").send_keys("22")
            driver.find_element(By.ID, "distance").send_keys("u'\ue009' + u'\ue003'")
            driver.find_element(By.ID, "distance").send_keys("10000")
            driver.find_element(By.ID, "fuelPrice").send_keys("u'\ue009' + u'\ue003'")
            driver.find_element(By.ID, "fuelPrice").send_keys("3.8")
            driver.find_element(By.ID, "electricityPrice").send_keys("u'\ue009' + u'\ue003'")
            driver.find_element(By.ID, "electricityPrice").send_keys("0.15")
            delay()
            # Verify that the amount/mo est. gas savings has been calculated
            try:
                driver.find_element(By.XPATH, "(//span[contains(.,'$133 /mo')])[2]")
                print("The amount est./mo est. gas savings has been calculated.")
            except NoSuchElementException:
                print("Est. gas savings amounts have changed.")

            driver.close()


            print("TC-3 passed. Information Model Y/Lease is correct")
        except NoSuchElementException:
            print("TC-3 failed. Is there something wrong")

        self.driver.quit()

    def test_04(self):

        driver = self.driver
        self.driver.maximize_window()
        driver.get('https://www.tesla.com/')

    # Verify Model Y Page/Finance
        try:
            driver.execute_script("window.scrollTo(0, 700)")
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Order Now')])[1]").click()
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Model Y')])[1]")

            driver.execute_script("document.body.style.zoom = '0.65'")
            delay()

            driver.find_element(By.XPATH, "//button[@id='finplat.AUTO_LOAN:LOAN:CT_PRIVATE']").click()
            driver.find_element(By.XPATH, "//span[contains(text(),'Long Range Rear-Wheel Drive')]").click()
            driver.find_element(By.XPATH, "(//span[contains(.,'Long Range All-Wheel Drive')])[2]").click()
            driver.find_element(By.XPATH, "//span[contains(text(),'Performance All-Wheel Drive')]").click()
            driver.find_element(By.XPATH, "(//input[@type='checkbox'])[1]").click()
            driver.find_element(By.XPATH, "(//input[@type='checkbox'])[1]").click()

            # Verify that all indicators price has been calculated
            try:
                driver.find_element(By.XPATH, "//span[contains(text(),'337')]")
                driver.find_element(By.XPATH, "//span[contains(text(),'135')]")
                driver.find_element(By.XPATH, "//span[contains(text(),'6.5')]")
                print("All indicators has been calculated correct.")
            except NoSuchElementException:
                print("Estimated amounts have changed.")

            driver.find_element(By.XPATH, "//span[contains(text(),'Edit Terms & Savings')]").click()
            delay()
            driver.find_element(By.XPATH, "//h2[contains(text(),'Financing Options')]")
            driver.find_element(By.XPATH, "//input[@id='cashDownPayment']").send_keys("u'\ue009' + u'\ue003'")
            driver.find_element(By.XPATH, "//input[@id='cashDownPayment']").send_keys("5000")
            dp_down = driver.find_element(By.XPATH, "(//button[contains(@aria-haspopup,'listbox')])[1]")
            dp_down.send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, "//li[@id='termLength-listbox-60']").click()
            time.sleep(1)
            dp_down = driver.find_element(By.XPATH, "(//button[contains(@aria-haspopup,'listbox')])[2]")
            dp_down.send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, "//span[contains(text(),'Very Good (680-720)')]").click()
            time.sleep(1)
            driver.find_element(By.XPATH, "//input[@id='interestRate']")
            driver.find_element(By.XPATH, "(//input[@type='checkbox'])[1]").click()
            driver.find_element(By.XPATH, "(//input[@type='checkbox'])[1]").click()
            driver.find_element(By.XPATH, "(//input[@type='checkbox'])[2]").click()
            driver.find_element(By.XPATH, "(//input[@type='checkbox'])[2]").click()
            driver.find_element(By.XPATH, "(//input[@type='checkbox'])[3]").click()
            driver.find_element(By.XPATH, "//span[contains(text(),'View Criteria')]").click()
            delay()
            driver.find_element(By.XPATH, "//span[contains(text(),'Eligibility Criteria')]")
            driver.find_element(By.XPATH, "//body/div[@id='root']/div[3]/div[1]/dialog[1]/section[1]/div[2]/div[1]/button[1]/*[1]").click()
            driver.find_element(By.XPATH, "//span[contains(text(),'Show Details')]").click()
            delay()
            driver.find_element(By.XPATH, "//span[contains(text(),'Est. Taxes & Fees')]")
            driver.find_element(By.XPATH, "//body/div[@id='root']/div[3]/div[1]/dialog[1]/section[1]/div[2]/div[1]/button[1]/*[1]").click()
            driver.find_element(By.XPATH, "//span[contains(text(),'Customize')]").click()
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Gas Savings')])[1]")
            driver.find_element(By.ID, "fuelEfficiency").send_keys("u'\ue009' + u'\ue003'")
            driver.find_element(By.ID, "fuelEfficiency").send_keys("22")
            driver.find_element(By.ID, "distance").send_keys("u'\ue009' + u'\ue003'")
            driver.find_element(By.ID, "distance").send_keys("15000")
            driver.find_element(By.ID, "fuelPrice").send_keys("u'\ue009' + u'\ue003'")
            driver.find_element(By.ID, "fuelPrice").send_keys("3.8")
            driver.find_element(By.ID, "electricityPrice").send_keys("u'\ue009' + u'\ue003'")
            driver.find_element(By.ID, "electricityPrice").send_keys("0.15")
            # Verify that the amount/mo est. gas savings has been calculated
            try:
                driver.find_element(By.XPATH, "(//span[@class='tds-text--h1-alt'][contains(.,'$167 /mo')])[1]")
                print("The amount est./mo est. gas savings has been calculated.")
            except NoSuchElementException:
                print("Est. gas savings amounts have changed.")

            driver.close()


            print("TC-4 passed. Information ModelY/Finance is correct")
        except NoSuchElementException:
            print("TC-4 failed. Is there something wrong")

        self.driver.quit()

    def test_05(self):

        driver = self.driver
        self.driver.maximize_window()
        driver.get('https://www.tesla.com/')

    # Verify Model Y Page/Feature Details
        try:
            driver.execute_script("window.scrollTo(0, 700)")
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Order Now')])[1]").click()
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Model Y')])[1]")

            driver.execute_script("document.body.style.zoom = '0.70'")
            delay()

            driver.find_element(By.XPATH, "(//span[contains(.,'Feature Details')])[2]").click()
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Range and Performance')])[1]")
            time.sleep(1)
            driver.find_element(By.XPATH, "//body/div[@id='root']/div[3]/div[3]/dialog[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/*[1]").click()
            driver.find_element(By.XPATH, "//span[contains(text(),'Interior & Convenience')]").click()
            time.sleep(1)
            driver.find_element(By.XPATH, "//body/div[@id='root']/div[3]/div[3]/dialog[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/*[1]").click()
            driver.find_element(By.XPATH, "//span[contains(text(),'Safety')]").click()
            time.sleep(1)
            driver.find_element(By.XPATH, "//body/div[@id='root']/div[3]/div[3]/dialog[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/*[1]").click()
            driver.close()

            print("TC-5 passed. ModelY/Feature Details is correct")
        except NoSuchElementException:
            print("TC-5 failed. Is there something wrong")

        self.driver.quit()

    def test_06(self):

        driver = self.driver
        self.driver.maximize_window()
        driver.get('https://www.tesla.com/')

    # Verify Model Y Page/Select Car Color
        try:
            driver.execute_script("window.scrollTo(0, 700)")
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Order Now')])[1]").click()
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Model Y')])[1]")

            driver.execute_script("document.body.style.zoom = '0.70'")
            delay()
            driver.execute_script("window.scrollTo(0, 400)")
            delay()

            driver.find_element(By.CSS_SELECTOR, "#Model_Y_Ultra_Red").click()
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Ultra Red')])[1]")
            driver.close()

            print("TC-6 passed. The User can select the color of the car")
        except NoSuchElementException:
            print("TC-6 failed. Is there something wrong")

        self.driver.quit()


    def test_07(self):

        driver = self.driver
        self.driver.maximize_window()
        driver.get('https://www.tesla.com/')

    # Verify Model Y Page/Select Type of Wheels
        try:
            driver.execute_script("window.scrollTo(0, 700)")
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Order Now')])[1]").click()
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Model Y')])[1]")

            driver.execute_script("document.body.style.zoom = '0.70'")
            delay()
            driver.execute_script("window.scrollTo(0, 500)")
            delay()

            driver.find_element(By.ID, "Model_Y_20’’_Induction Wheels").click()
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'20’’ Induction Wheels')])[1]")
            driver.find_element(By.XPATH, "//span[contains(.,'All-Season Tires')]")
            driver.find_element(By.XPATH, "//p[contains(text(),'Range (est.) : 305mi')]")
            driver.close()

            print("TC-7 passed. The User can select Type of Wheels")
        except NoSuchElementException:
            print("TC-7 failed. Is there something wrong")

        self.driver.quit()

    def test_08(self):

        driver = self.driver
        self.driver.maximize_window()
        driver.get('https://www.tesla.com/')

        # Verify Model Y Page/Select Tow Package
        try:
            driver.execute_script("window.scrollTo(0, 700)")
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Order Now')])[1]").click()
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Model Y')])[1]")

            driver.execute_script("document.body.style.zoom = '0.70'")
            delay()
            driver.execute_script("window.scrollTo(0, 500)")
            delay()
            driver.find_element(By.XPATH, "//span[contains(text(),'Tow Package')]")
            driver.find_element(By.XPATH, "(//span[@class='tds-form-input-visual-checkbox'])[1]").click()
            driver.find_element(By.XPATH, "(//div[contains(.,'Tow Hitch')])[10]")
            # Verify that the amount Tow Hitch has been calculated
            try:
                driver.find_element(By.XPATH, "(//span[contains(.,'$1,000')])[2]")
                print("The amount Tow Hitch has been calculated.")
            except NoSuchElementException:
                print("Tow Hitch amounts have changed.")

            driver.close()

            print("TC-8 passed. The User can select Tow Package")
        except NoSuchElementException:
            print("TC-8 failed. Is there something wrong")

        self.driver.quit()


    def test_09(self):

        driver = self.driver
        self.driver.maximize_window()
        driver.get('https://www.tesla.com/')


    # Verify Model Y Page/Select Interior Color
        try:
            driver.execute_script("window.scrollTo(0, 700)")
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Order Now')])[1]").click()
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Model Y')])[1]")

            driver.execute_script("document.body.style.zoom = '0.70'")
            delay()
            driver.execute_script("window.scrollTo(0, 700)")
            delay()
            driver.find_element(By.ID, "Model_Y_Black_and White Interior").click()
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Black and White Interior')])[1]")
            driver.find_element(By.XPATH, "//span[contains(text(),'Five Seat Interior')]")
            driver.find_element(By.XPATH, "(//span[contains(.,'Feature Details')])[4]").click()
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Glass Roof')])[2]")
            driver.close()




            print("TC-9 passed. The User can select Interior Color")
        except NoSuchElementException:
            print("TC-9 failed. Is there something wrong")

        self.driver.quit()

    def test_10(self):

        driver = self.driver
        self.driver.maximize_window()
        driver.get('https://www.tesla.com/')

    # Verify Model Y Page/Select Full Self-Driving
        try:
            driver.execute_script("window.scrollTo(0, 700)")
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Order Now')])[1]").click()
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Model Y')])[1]")

            driver.execute_script("document.body.style.zoom = '0.70'")
            delay()
            driver.execute_script("window.scrollTo(0, 1000)")
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Full Self-Driving (Supervised)')])[2]")
            driver.find_element(By.XPATH, "//span[contains(text(),'0% APR* Available with Purchase')]")
            driver.find_element(By.XPATH, "(//span[contains(.,'Full Self-Driving')])[3]")
            driver.find_element(By.XPATH, "(//span[@class='tds-form-input-visual-checkbox'])[2]").click()
            driver.find_element(By.XPATH, "//span[contains(text(),'Watch a Video')]").click()
            delay()
            driver.find_element(By.XPATH, "//span[contains(text(),'Watch Full Self-Driving')]")
            driver.find_element(By.XPATH, "//span[contains(text(),'Begin Drive')]").click()
            driver.find_element(By.XPATH, "//span[contains(text(),'Roundabouts')]").click()
            driver.find_element(By.XPATH, "//span[contains(text(),'Tight Gaps')]").click()
            driver.close()

            print("TC-10 passed. The User can select Full Self-Driving")
        except NoSuchElementException:
            print("TC-10 failed. Is there something wrong")

        self.driver.quit()

    def test_11(self):

        driver = self.driver
        self.driver.maximize_window()
        driver.get('https://www.tesla.com/')

    # Verify Model Y Page/Select Charging
        try:
            driver.execute_script("window.scrollTo(0, 700)")
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Order Now')])[1]").click()
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Model Y')])[1]")

            driver.execute_script("document.body.style.zoom = '0.70'")
            delay()
            driver.execute_script("window.scrollTo(0, 1300)")
            delay()
            driver.find_element(By.XPATH, "//h2[contains(text(),'Charging')]")
            driver.find_element(By.XPATH, "//span[contains(text(),'Home Charger')]")
            driver.find_element(By.XPATH, "//span[contains(text(),'Mobile Charger')]")
            driver.find_element(By.XPATH, "(//span[@class='tds-form-input-visual-checkbox'])[3]").click()
            driver.find_element(By.XPATH, "(//span[@class='tds-form-input-visual-checkbox'])[4]").click()
            driver.find_element(By.XPATH, "(//button[contains(.,'Learn More')])[1]").click()
            delay()
            driver.find_element(By.XPATH, "//h3[contains(text(),'Home Charger')]")
            driver.find_element(By.XPATH, "(//button[contains(.,'Remove')])[1]").click()
            driver.find_element(By.XPATH, "//button[contains(.,'Add')]").click()
            driver.close()

            print("TC-11 passed. The User can select Charging")
        except NoSuchElementException:
            print("TC-11 failed. Is there something wrong")

        self.driver.quit()

    def test_12(self):

        driver = self.driver
        self.driver.maximize_window()
        driver.get('https://www.tesla.com/')

    # Verify Model Y Page/Select Accessories
        try:
            driver.execute_script("window.scrollTo(0, 700)")
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Order Now')])[1]").click()
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Model Y')])[1]")

            driver.execute_script("document.body.style.zoom = '0.70'")
            delay()
            driver.execute_script("window.scrollTo(0, 1600)")
            delay()
            driver.find_element(By.XPATH, "//h2[contains(text(),'Accessories')]")
            driver.find_element(By.XPATH, "//span[contains(text(),'Center Console Trays')]")
            driver.find_element(By.XPATH, "//span[contains(text(),'Sunshade')]")
            driver.find_element(By.XPATH, "//span[contains(text(),'All-Weather Interior Liners')]")
            driver.find_element(By.XPATH, "//span[contains(text(),'Parcel Shelf')]")
            driver.find_element(By.XPATH, "(//span[@class='tds-form-input-visual-checkbox'])[5]").click()
            driver.find_element(By.XPATH, "(//span[@class='tds-form-input-visual-checkbox'])[6]").click()
            driver.find_element(By.XPATH, "(//span[@class='tds-form-input-visual-checkbox'])[7]").click()
            driver.find_element(By.XPATH, "(//span[@class='tds-form-input-visual-checkbox'])[8]").click()
            driver.find_element(By.XPATH, "(//button[contains(.,'Learn More')])[2]").click()
            delay()
            driver.find_element(By.XPATH, "//h3[contains(text(),'Center Console Trays')]")
            driver.find_element(By.XPATH, "(//button[contains(.,'Remove')])[1]").click()
            driver.find_element(By.XPATH, "//button[contains(.,'Add')]").click()
            driver.close()

            print("TC-12 passed. The User can select Accessories")
        except NoSuchElementException:
            print("TC-12 failed. Is there something wrong")

        self.driver.quit()

    def test_13(self):

        driver = self.driver
        self.driver.maximize_window()
        driver.get('https://www.tesla.com/')

    # Verify Model Y Page/Est. Purchase Price
        try:
            driver.execute_script("window.scrollTo(0, 700)")
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Order Now')])[1]").click()
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Model Y')])[1]")

            driver.execute_script("document.body.style.zoom = '0.70'")
            delay()
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            delay()
            driver.find_element(By.XPATH, "//h3[contains(text(),'Your Model Y')]")
            driver.find_element(By.XPATH, "//span[contains(text(),'Due Today')]")
            try:
                driver.find_element(By.XPATH, "(//span[contains(.,'$250')])[3]")
                print("Amount Due Today has been calculated.")
            except NoSuchElementException:
                print("Amount Due Today have changed.")
            driver.find_element(By.XPATH, "(//span[contains(.,'Est. Purchase Price')])[2]")
            try:
                driver.find_element(By.XPATH, "(//span[contains(.,'$46,630')])[2]")
                print("Est. Purchase Price has been calculated.")
            except NoSuchElementException:
                print("Est. Purchase Price have changed.")
            try:
                driver.find_element(By.XPATH, "//p[contains(text(),'Est. Delivery: Oct – Nov 2024')]")
                print("Est. Delivery date has been calculated.")
            except NoSuchElementException:
                print("Est. Delivery date have changed.")

            driver.find_element(By.XPATH, "//button[contains(text(),'Order with Card')]").click()
            delay()

            print("TC-13 passed. Est. Purchase Price has been calculated")
        except NoSuchElementException:
            print("TC-13 failed. Is there something wrong")

        self.driver.quit()


    def test_14(self):

        driver = self.driver
        self.driver.maximize_window()
        driver.get('https://www.tesla.com/')

    # Verify Model Y Page/Est. Purchase Price
        try:
            driver.execute_script("window.scrollTo(0, 700)")
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Order Now')])[1]").click()
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Model Y')])[1]")

            driver.execute_script("document.body.style.zoom = '0.65'")
            delay()
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            delay()
            driver.find_element(By.XPATH, "//h3[contains(text(),'Your Model Y')]")

            driver.find_element(By.XPATH, "//button[contains(text(),'Order with Card')]").click()
            delay()
            driver.execute_script("window.scrollTo(0, 2100)")
            time.sleep(2)

            driver.find_element(By.XPATH, "//legend[contains(text(),'Enter Account Details')]")
            # filling in the form
            first_name = driver.find_element(By.XPATH, "//input[@id='FIRST_NAME']")
            first_name.send_keys("Jessica")
            last_name = driver.find_element(By.XPATH, "//input[@id='LAST_NAME']")
            last_name.send_keys("Smith")
            email_address = driver.find_element(By.XPATH, "//input[@id='EMAIL']")
            email_address.send_keys("jenipo9498@polatrix.com")
            confirm_email_address = driver.find_element(By.XPATH, "//input[@id='EMAIL_CONFIRM']")
            confirm_email_address.send_keys("jenipo9498@polatrix.com")
            phone_number = driver.find_element(By.XPATH, "//input[@id='PHONE_NUMBER']")
            phone_number.send_keys("(513)555-0123")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            delay()
            driver.find_element(By.XPATH, "//button[contains(text(),'Place Order')]")

            print("TC-14 passed. User information has been entered")
        except NoSuchElementException:
            print("TC-14 failed. Is there something wrong")

        self.driver.quit()


class Tesla_ModelY_Negative(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_01(self):

        driver = self.driver
        driver.maximize_window()
        driver.get('https://www.tesla.com/')

        # Verify that the user can't Customize Gas Savings with invalid entered values (invalid Gas Car Efficiency (mpg))
        try:
            driver.execute_script("window.scrollTo(0, 700)")
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Order Now')])[1]").click()
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Model Y')])[1]")

            driver.execute_script("document.body.style.zoom = '0.70'")
            delay()
            driver.find_element(By.XPATH, "//button[@id='cash']").click()
            delay()
            driver.find_element(By.XPATH, "//span[contains(text(),'Edit Savings')]").click()
            delay()
            driver.find_element(By.XPATH, "//h2[contains(text(),'Financing Options')]")
            driver.find_element(By.XPATH, "//span[contains(text(),'Customize')]").click()
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Gas Savings')])[1]")

            driver.find_element(By.ID, "fuelEfficiency").send_keys("u'\ue009' + u'\ue003'")
            driver.find_element(By.ID, "fuelEfficiency").send_keys("NR")
            delay()
            driver.find_element(By.XPATH, "(//div[contains(.,'a valid gas car efficiency (mpg) is required')])[13]")

            print("TC-1-1 passed. The User can't enter invalid values 'Gas Car Efficiency (mpg)'")
        except NoSuchElementException:
            print("TC-1-1 failed. Is there something wrong")

        self.driver.quit()


    def test_02(self):

        driver = self.driver
        self.driver.maximize_window()
        driver.get('https://www.tesla.com/')

        # Verify that the user can't Customize Gas Savings with invalid entered values (invalid Annual Mileage)
        try:
            driver.execute_script("window.scrollTo(0, 700)")
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Order Now')])[1]").click()
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Model Y')])[1]")

            driver.execute_script("document.body.style.zoom = '0.70'")
            delay()
            driver.find_element(By.XPATH, "//button[@id='cash']").click()
            delay()
            driver.find_element(By.XPATH, "//span[contains(text(),'Edit Savings')]").click()
            delay()
            driver.find_element(By.XPATH, "//h2[contains(text(),'Financing Options')]")
            driver.find_element(By.XPATH, "//span[contains(text(),'Customize')]").click()
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Gas Savings')])[1]")

            driver.find_element(By.ID, "distance").send_keys("u'\ue009' + u'\ue003'")
            driver.find_element(By.ID, "distance").send_keys("")
            delay()
            driver.find_element(By.XPATH, "(//div[contains(.,'a valid annual mileage is required')])[13]")

            print("TC-2-2 passed. The User can't enter invalid values 'Annual Mileage'")
        except NoSuchElementException:
            print("TC-2-2 failed. Is there something wrong")

        self.driver.quit()

    def test_03(self):

        driver = self.driver
        self.driver.maximize_window()
        driver.get('https://www.tesla.com/')

        # Verify that the user can't Customize Gas Savings with invalid entered values (invalid Gas Cost (per gallon))
        try:
            driver.execute_script("window.scrollTo(0, 700)")
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Order Now')])[1]").click()
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Model Y')])[1]")

            driver.execute_script("document.body.style.zoom = '0.70'")
            delay()
            driver.find_element(By.XPATH, "//button[@id='cash']").click()
            delay()
            driver.find_element(By.XPATH, "//span[contains(text(),'Edit Savings')]").click()
            delay()
            driver.find_element(By.XPATH, "//h2[contains(text(),'Financing Options')]")
            driver.find_element(By.XPATH, "//span[contains(text(),'Customize')]").click()
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Gas Savings')])[1]")

            driver.find_element(By.ID, "fuelPrice").send_keys("u'\ue009' + u'\ue003'")
            driver.find_element(By.ID, "fuelPrice").send_keys("0")
            delay()
            driver.find_element(By.XPATH, "(//div[contains(.,'a valid gas cost (per gallon) is required')])[13]")

            print("TC-3-3 passed. The User can't enter invalid values 'Gas Cost (per gallon)'")
        except NoSuchElementException:
            print("TC-3-3 failed. Is there something wrong")

        self.driver.quit()

    def test_04(self):

        driver = self.driver
        self.driver.maximize_window()
        driver.get('https://www.tesla.com/')

        # Verify that the user can't Customize Gas Savings with invalid entered values (invalid Electricity Cost (per kWh))
        try:
            driver.execute_script("window.scrollTo(0, 700)")
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Order Now')])[1]").click()
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Model Y')])[1]")

            driver.execute_script("document.body.style.zoom = '0.70'")
            delay()
            driver.find_element(By.XPATH, "//button[@id='cash']").click()
            delay()
            driver.find_element(By.XPATH, "//span[contains(text(),'Edit Savings')]").click()
            delay()
            driver.find_element(By.XPATH, "//h2[contains(text(),'Financing Options')]")
            driver.find_element(By.XPATH, "//span[contains(text(),'Customize')]").click()
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Gas Savings')])[1]")

            driver.find_element(By.ID, "electricityPrice").send_keys("u'\ue009' + u'\ue003'")
            driver.find_element(By.ID, "electricityPrice").send_keys("-")
            delay()
            driver.find_element(By.XPATH, "(//div[contains(.,'a valid electricity cost (per kwh) is required')])[13]")

            print("TC-4-4 passed. The User can't enter invalid values 'Electricity Cost (per kWh)'")
        except NoSuchElementException:
            print("TC-4-4 failed. Is there something wrong")

        self.driver.quit()

    def test_05(self):

        driver = self.driver
        self.driver.maximize_window()
        driver.get('https://www.tesla.com/')

    # Verify that the user can't edit Financing Options with invalid entered values (invalid Down Payment)
        try:
            driver.execute_script("window.scrollTo(0, 700)")
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Order Now')])[1]").click()
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Model Y')])[1]")

            driver.execute_script("document.body.style.zoom = '0.65'")
            delay()

            driver.find_element(By.XPATH, "//button[@id='finplat.AUTO_LEASE:OPERATIONAL_LEASE:CT_PRIVATE']").click()
            delay()
            driver.find_element(By.XPATH, "//span[contains(text(),'Edit Terms & Savings')]").click()
            delay()
            driver.find_element(By.XPATH, "//h2[contains(text(),'Financing Options')]")
            driver.find_element(By.XPATH, "//input[@id='cashDownPayment']").send_keys("u'\ue009' + u'\ue003'")
            driver.find_element(By.XPATH, "//input[@id='cashDownPayment']").send_keys("20000")
            delay()
            driver.find_element(By.XPATH, "(//div[contains(.,'Downpayment cannot exceed $8,733')])[14]")

            print("TC-5-5 passed. The User can't enter invalid Down Payment")
        except NoSuchElementException:
            print("TC-5-5 failed. Is there something wrong")

        self.driver.quit()


    def test_06(self):

        driver = self.driver
        self.driver.maximize_window()
        driver.get('https://www.tesla.com/')

    # Verify that the user can't enter invalid values (invalid First Name)
        try:
            driver.execute_script("window.scrollTo(0, 700)")
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Order Now')])[1]").click()
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Model Y')])[1]")

            driver.execute_script("document.body.style.zoom = '0.65'")
            delay()
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            delay()
            driver.find_element(By.XPATH, "//h3[contains(text(),'Your Model Y')]")

            driver.find_element(By.XPATH, "//button[contains(text(),'Order with Card')]").click()
            delay()
            driver.execute_script("window.scrollTo(0, 2100)")
            time.sleep(2)

            driver.find_element(By.XPATH, "//legend[contains(text(),'Enter Account Details')]")

            # filling in the form

            first_name = driver.find_element(By.XPATH, "//input[@id='FIRST_NAME']")
            first_name.send_keys("1#%")
            driver.find_element(By.XPATH, "//label[contains(text(),'First Name')]").click()
            driver.find_element(By.XPATH, "//div[contains(text(),'Invalid name')]")
            delay()

            print("TC-6-6 passed. The User can't enter invalid First name")
        except NoSuchElementException:
            print("TC-6-6 failed. Is there something wrong")

        self.driver.quit()

    def test_07(self):

        driver = self.driver
        self.driver.maximize_window()
        driver.get('https://www.tesla.com/')

    # Verify that the user can't enter invalid values (invalid Last Name)
        try:
            driver.execute_script("window.scrollTo(0, 700)")
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Order Now')])[1]").click()
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Model Y')])[1]")

            driver.execute_script("document.body.style.zoom = '0.65'")
            delay()
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            delay()
            driver.find_element(By.XPATH, "//h3[contains(text(),'Your Model Y')]")

            driver.find_element(By.XPATH, "//button[contains(text(),'Order with Card')]").click()
            delay()
            driver.execute_script("window.scrollTo(0, 2100)")
            time.sleep(2)

            driver.find_element(By.XPATH, "//legend[contains(text(),'Enter Account Details')]")

            # filling in the form

            last_name = driver.find_element(By.XPATH, "//input[@id='LAST_NAME']")
            last_name.send_keys("")
            driver.find_element(By.XPATH, "//label[contains(text(),'Last Name')]").click()
            driver.find_element(By.XPATH, "//div[contains(text(),'Required')]")
            delay()

            print("TC-7-7 passed. The User can't enter invalid Last name")
        except NoSuchElementException:
            print("TC-7-7 failed. Is there something wrong")

        self.driver.quit()


    def test_08(self):

        driver = self.driver
        self.driver.maximize_window()
        driver.get('https://www.tesla.com/')

    # Verify that the user can't enter invalid values (invalid Email)
        try:
            driver.execute_script("window.scrollTo(0, 700)")
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Order Now')])[1]").click()
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Model Y')])[1]")

            driver.execute_script("document.body.style.zoom = '0.65'")
            delay()
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            delay()
            driver.find_element(By.XPATH, "//h3[contains(text(),'Your Model Y')]")

            driver.find_element(By.XPATH, "//button[contains(text(),'Order with Card')]").click()
            delay()
            driver.execute_script("window.scrollTo(0, 2100)")
            time.sleep(2)

            driver.find_element(By.XPATH, "//legend[contains(text(),'Enter Account Details')]")

            # filling in the form

            email_address = driver.find_element(By.XPATH, "//input[@id='EMAIL']")
            email_address.send_keys("jenipo9498@polatrix.")
            driver.find_element(By.XPATH, "(//label[contains(.,'Email Address')])[1]").click()
            driver.find_element(By.XPATH, "//div[contains(text(),'Email address is not valid')]")
            delay()

            print("TC-8-8 passed. The User can't enter invalid email")
        except NoSuchElementException:
            print("TC-8-8 failed. Is there something wrong")

        self.driver.quit()


    def test_09(self):

        driver = self.driver
        self.driver.maximize_window()
        driver.get('https://www.tesla.com/')

    # Verify that the user can't enter invalid values (confirm another Email)
        try:
            driver.execute_script("window.scrollTo(0, 700)")
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Order Now')])[1]").click()
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Model Y')])[1]")

            driver.execute_script("document.body.style.zoom = '0.65'")
            delay()
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            delay()
            driver.find_element(By.XPATH, "//h3[contains(text(),'Your Model Y')]")

            driver.find_element(By.XPATH, "//button[contains(text(),'Order with Card')]").click()
            delay()
            driver.execute_script("window.scrollTo(0, 2100)")
            time.sleep(2)

            driver.find_element(By.XPATH, "//legend[contains(text(),'Enter Account Details')]")

            # filling in the form

            email_address = driver.find_element(By.XPATH, "//input[@id='EMAIL']")
            email_address.send_keys("jenipo9498@polatrix.com")
            confirm_email_address = driver.find_element(By.XPATH, "//input[@id='EMAIL_CONFIRM']")
            confirm_email_address.send_keys("jenipo949@polatrix.com")
            driver.find_element(By.XPATH, "//label[contains(text(),'Confirm Email Address')]").click()
            driver.find_element(By.XPATH, "//div[contains(text(),'Email addresses do not match')]")
            delay()

            print("TC-9-9 passed. The User can't confirm another email")
        except NoSuchElementException:
            print("TC-9-9 failed. Is there something wrong")

        self.driver.quit()


    def test_10(self):

        driver = self.driver
        self.driver.maximize_window()
        driver.get('https://www.tesla.com/')

    # Verify that the user can't enter invalid values (enter invalid phone number)
        try:
            driver.execute_script("window.scrollTo(0, 700)")
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Order Now')])[1]").click()
            delay()
            driver.find_element(By.XPATH, "(//span[contains(.,'Model Y')])[1]")

            driver.execute_script("document.body.style.zoom = '0.65'")
            delay()
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            delay()
            driver.find_element(By.XPATH, "//h3[contains(text(),'Your Model Y')]")

            driver.find_element(By.XPATH, "//button[contains(text(),'Order with Card')]").click()
            delay()
            driver.execute_script("window.scrollTo(0, 2100)")
            time.sleep(2)

            driver.find_element(By.XPATH, "//legend[contains(text(),'Enter Account Details')]")

            # filling in the form

            phone_number = driver.find_element(By.XPATH, "//input[@id='PHONE_NUMBER']")
            phone_number.send_keys("(513)555")
            driver.find_element(By.XPATH, "//label[contains(text(),'Mobile Phone Number')]").click()
            driver.find_element(By.XPATH, "//div[contains(text(),'Phone number is not valid')]")
            delay()

            print("TC-10-10 passed. The User can't enter invalid phone number")
        except NoSuchElementException:
            print("TC-10-10 failed. Is there something wrong")

        self.driver.quit()
def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
        unittest.main(AllureReports)
