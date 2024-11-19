import time
import pytest
from selenium.webdriver.common.by import By


link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_add_to_basket_is_present(browser):
    browser.get(link)
    time.sleep(30)
    assert browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket"), "button btn-add-to-basket should be present"


if __name__ == "__main__":
    pytest.main()