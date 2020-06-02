#-*- coding: UTF-8 -*-

import datetime
import unittest
from utils.browser_engine import driver
from utils.base_page import  BasePage
from pageobjects.common.topMenu import TopMenuPage
from pageobjects.homepage.homePage import  HomePage
from pageobjects.customer.customerRecord import CustomerRecordPage

nowTime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

class Address_Website(unittest.TestCase):

    # 初始化，打开浏览器，并进行登录(实例化)
    @classmethod
    def setUpClass(cls):
        cls.driver = driver
        TopMenuPage(cls.driver).get_url()
        HomePage(cls.driver).quick_entrance("Customers","C000089009",2)

    def test_01_Address_new(self):
        u"""new address"""
        CustomerRecordPage(self.driver).switch_tab("Entity")
        CustomerRecordPage(self.driver).entity_operator("Addresses", "New", "")
        self.assertTrue(CustomerRecordPage(self.driver).operator_address("Home", "Address", "changsha", "AK"))

    def test_02_Address_detail(self):
        u"""show address detail"""
        CustomerRecordPage(self.driver).entity_operator("Addresses", "Details", "1")
        self.assertTrue(CustomerRecordPage(self.driver).detail_history("Details"))

    def test_03_Address_edit(self):
        u"""edit address"""
        CustomerRecordPage(self.driver).entity_operator("Addresses", "Edit", "1")
        self.assertTrue(CustomerRecordPage(self.driver).operator_address("Office", "Address1", "changsha", "AK"))

    def test_04_Address_history(self):
        u"""show address history"""
        CustomerRecordPage(self.driver).entity_operator("Addresses", "History", "1")
        self.assertTrue(CustomerRecordPage(self.driver).detail_history("History"))

    def test_05_Address_delete(self):
        u"""delete address"""
        CustomerRecordPage(self.driver).entity_operator("Addresses", "Delete", "1")
        self.assertTrue(CustomerRecordPage(self.driver).delete())

    def test_06_Websites_new(self):
        u"""new Websites"""
        CustomerRecordPage(self.driver).entity_operator("Website", "New", "")
        self.assertTrue(CustomerRecordPage(self.driver).input_DBA_Website("url", "http://www.uiautomation.com"))

    def test_07_Websites_detail(self):
        u"""show Websites details"""
        CustomerRecordPage(self.driver).entity_operator("Website", "Details", "1")
        self.assertTrue(CustomerRecordPage(self.driver).detail_history("Details"))

    def test_08_Websites_edit(self):
        u"""edit Websites"""
        CustomerRecordPage(self.driver).entity_operator("Website", "Edit", "1")
        self.assertTrue(CustomerRecordPage(self.driver).input_DBA_Website("url", "http://www.uiautomationEdit.com"))

    def test_09_Websites_history(self):
        u"""show Websites history"""
        CustomerRecordPage(self.driver).entity_operator("Website", "History", "1")
        self.assertTrue(CustomerRecordPage(self.driver).detail_history("History"))

    def test_10_Websites_delete(self):
        u"""delete Websites"""
        CustomerRecordPage(self.driver).entity_operator("Website", "Delete", "1")
        self.assertTrue(CustomerRecordPage(self.driver).delete())






