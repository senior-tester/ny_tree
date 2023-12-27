from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import MoveTargetOutOfBoundsException
from time import sleep
import random


driver = webdriver.Chrome()
driver.maximize_window()


driver.get('https://www.karusel-tv.ru/games/tree')
sleep(3)
driver.execute_script("window.scrollTo(0, 300)")
sleep(1)

iframe = driver.find_element('xpath', '//iframe')
driver.switch_to.frame(iframe)
canvas = driver.find_element('xpath', '//canvas')

canvas_size = canvas.size
center_x = canvas_size['width'] / 2
center_y = canvas_size['height'] / 2

menu_left_border_x = center_x / 2
menu_width = center_x - menu_left_border_x
menu_center_x = menu_left_border_x + (menu_width / 2)
left_column_x = (menu_width / 3) + menu_left_border_x
right_column_x = ((menu_width / 3) * 2) + menu_left_border_x

menu_icons_1_row_y = (center_y / 3) * -1
menu_icons_2_row_y = -15
menu_icons_3_row_y = center_y / 4
menu_icons_4_row_y = menu_icons_3_row_y * 2
menu_icons_5_row_y = menu_icons_3_row_y * 3
stars = (left_column_x, menu_icons_1_row_y)
rings = (right_column_x, menu_icons_1_row_y)
cookies = (left_column_x, menu_icons_2_row_y)
youla = (right_column_x, menu_icons_2_row_y)
candies = (left_column_x, menu_icons_3_row_y)
zoo = (right_column_x, menu_icons_3_row_y)
candles = (left_column_x, menu_icons_4_row_y)
ball1 = (right_column_x, menu_icons_4_row_y)
ball2 = (left_column_x, menu_icons_5_row_y)
ball3 = (right_column_x, menu_icons_5_row_y)
back_button = (menu_center_x, menu_icons_1_row_y - 40)
t1 = stars
t2 = rings
t3 = cookies
t4 = youla
t5 = candies
t6 = zoo
t7 = candles
t8 = ball1
t9 = ball2
t10 = ball3

toys = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10]
icons = [stars, rings, cookies, youla, candies, zoo, candles, ball1, ball2, ball3]


def click(coords):
    actions = ActionChains(driver)
    actions.move_to_element_with_offset(canvas, *coords)
    actions.click()
    actions.perform()


def move(coords_source, coords_target):
    actions = ActionChains(driver)
    actions.move_to_element_with_offset(canvas, *coords_source)
    actions.click_and_hold()
    actions.move_by_offset(*coords_target)
    actions.release()
    actions.perform()


count = 0

while count < 20:
    click(random.choice(icons))
    sleep(2)
    x = (menu_center_x + random.randrange(-25, 15)) * -1
    y = random.randint((center_y - 30) * -1, center_x - 50)
    try:
        move(random.choice(toys), (x, y))
    except MoveTargetOutOfBoundsException:
        print(f'x:{x}\ny:{y}')
    sleep(2)
    click(back_button)
    sleep(2)
    count += 1

# click(candies)
# sleep(2)
# move(t3, ((menu_center_x + 15) * -1, -25))
# sleep(2)
# click(back_button)
# sleep(2)
