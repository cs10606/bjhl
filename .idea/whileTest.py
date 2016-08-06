# -*- coding: utf-8 -*-
from selenium import  webdriver

"""
天眼登录
"""
driver =webdriver.Chrome()
driver.get('http://eye.baijiahulian.com')
driver.find_element_by_id('username').send_keys('huanglong')
driver.find_element_by_id('password').send_keys('Cs200603231!')
driver.find_element_by_tag_name('button').click()

"""
进入天校管理界面
"""
driver.implicitly_wait(5)
driver.find_element_by_class_name('ng-scope').click()
driver.find_element_by_class_name('ng-binding').click()
driver.find_element_by_name('status').find_element_by_tag_name('input').click
driver.quit()

