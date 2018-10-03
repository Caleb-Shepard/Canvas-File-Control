# **************************************************************************** #
#                                                                              #
#                                                             |\               #
#    file_downloader.py                                 ------| \----          #
#                                                       |    \`  \  |  p       #
#    By: cshepard6055 <cshepard6055@floridapoly.edu>    |  \`-\   \ |  o       #
#                                                       |---\  \   `|  l       #
#    Created: 2018/10/02 20:17:10 by cshepard6055       | ` .\  \   |  y       #
#    Updated: 2018/10/02 20:20:38 by cshepard6055       -------------          #
#                                                                              #
# **************************************************************************** #

from selenium import webdriver
from time import sleep
import selenium
import getpass

# DEFINE GLOBALS
CHROMEDRIVER_PATH   = "/usr/local/bin/chromedriver"
WEBDRIVER_SLEEP     = 5
DEBUG_MODE          = True
CANVAS_URL          = "https://floridapolytechnic.instructure.com/"

def chromedriver_get(url, chrome_instance):
    chrome_instance.get(url)
    sleep(WEBDRIVER_SLEEP)


# print debug messages when debug mode is active; otherwise just ignore
def print_debug_messages(debug_message):
    if DEBUG_MODE is True:
        print(debug_message)


def canvas_login(chrome_instance):
    print_debug_messages("exec canvas_login()")

    chromedriver_get(CANVAS_URL, chrome_instance)

    # Enter username, password, and submit
    username_box = chrome_instance.find_element_by_id("userNameInput")
    username_box.send_keys(input("username: "))
    password_box = chrome_instance.find_element_by_id ("passwordInput")
    password_box.send_keys(getpass.getpass("Password: "))
    chrome_instance.find_element_by_id("submitButton").click()


def get_file_download_urls(course_url, chrome_instance):
    print_debug_messages("exec get_file_download_urls()")
    files_url_suffix = r"/files"
    course_files_url = course_url + files_url_suffix

    file_download_links = []

    chromedriver_get(course_files_url, chrome_instance)

    # scan for hyperlinks containing files
    course_files = chrome_instance.find_elements_by_class_name("ef-name-col__link")
    for course_file in course_files:
        file_download_link = course_file.get_attribute("href")
        file_download_links.append(file_download_link)

    return file_download_links


#TODO
def download_files(file_urls, chrome_instance):
    pass


def main():
    print_debug_messages("exec main()")
    print_debug_messages("Dirty hack that accesses course files for comp arch")
    course_url = "https://floridapolytechnic.instructure.com/courses/2556"

    chrome_instance = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)
    canvas_login(chrome_instance)
    file_urls = get_file_download_urls(course_url, chrome_instance)

    # Simple functionality demonstration
    for file_url in file_urls:
        chromedriver_get(file_url, chrome_instance)

    download_files(file_urls, chrome_instance)
    chrome_instance.quit()


main()
