#-*- coding: UTF-8 -*-

import datetime
import unittest
from utils.browser_engine import driver
from utils.base_page import  BasePage
from config.customer.customer_record_entity import CustomerRecordEntity
from pageobjects.common.topMenu import TopMenuPage
from pageobjects.homepage.homePage import  HomePage
from pageobjects.customer.customerRecord import CustomerRecordPage

nowTime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

class DBA_Identifier(unittest.TestCase):

    # 初始化，打开浏览器，并进行登录(实例化)
    @classmethod
    def setUpClass(cls):
        cls.driver = driver
        TopMenuPage(cls.driver).get_url()
        HomePage(cls.driver).quick_entrance("Customers","C000089009",2)

    def test_01_DBA_new(self):
        u"""new a DBA"""
        CustomerRecordPage(self.driver).switch_tab("Entity")
        CustomerRecordPage(self.driver).entity_operator("Doing Business As (DBA)", "New", "")
        self.assertTrue(CustomerRecordPage(self.driver).input_DBA_Website("alias", "UIAutomation" + nowTime))

    def test_02_DBA_detail(self):
        u"""query DBA detail"""
        CustomerRecordPage(self.driver).entity_operator("Doing Business As (DBA)", "Details", "1")
        self.assertTrue(CustomerRecordPage(self.driver).detail_history("Details"))

    def test_03_DBA_edit(self):
        u"""edit DBA"""
        CustomerRecordPage(self.driver).entity_operator("Doing Business As (DBA)", "Edit", "1")
        self.assertTrue(CustomerRecordPage(self.driver).input_DBA_Website("alias", "UIAutomationEdit" + nowTime))

    def test_04_DBA_history(self):
        u"""show DBA history"""
        CustomerRecordPage(self.driver).entity_operator("Doing Business As (DBA)", "History", "1")
        self.assertTrue(CustomerRecordPage(self.driver).detail_history("History"))

    def test_05_DBA_delete(self):
        u"""delete DBA"""
        CustomerRecordPage(self.driver).entity_operator("Doing Business As (DBA)", "Delete", "1")
        self.assertTrue(CustomerRecordPage(self.driver).delete())

    def test_06_Identifier_new(self):
        u"""new identifier"""
        CustomerRecordPage(self.driver).entity_operator("Business Identifier", "New", "")
        self.assertTrue(CustomerRecordPage(self.driver).operator_identifier("SSN", "123456789"))

    def test_07_Identifier_detail(self):
        u"""show identifier detail"""
        CustomerRecordPage(self.driver).entity_operator("Business Identifier", "Details", "1")
        self.assertTrue(CustomerRecordPage(self.driver).detail_history("Details"))

    def test_08_Identifier_edit(self):
        u"""edit identifier"""
        CustomerRecordPage(self.driver).entity_operator("Business Identifier", "Edit", "1")
        self.assertTrue(CustomerRecordPage(self.driver).operator_identifier("State Tax ID", "11111111111"))

    def test_09_Identifier_history(self):
        u"""show identifier history"""
        CustomerRecordPage(self.driver).entity_operator("Business Identifier", "History", "1")
        self.assertTrue(CustomerRecordPage(self.driver).detail_history("History"))

    def test_10_Identifier_delete(self):
        u"""delete identifier"""
        CustomerRecordPage(self.driver).entity_operator("Business Identifier", "Delete", "1")
        self.assertTrue(CustomerRecordPage(self.driver).delete())








