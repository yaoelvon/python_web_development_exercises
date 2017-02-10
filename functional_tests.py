from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# yaoel听说一个很棒的在线待办事项应用
		# 他去看了这个应用的首页
		self.browser.get('http://localhost:8000')

		# 他注意到网页的标题和头部头包含“To-Do"这个词
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		# 应用邀请他输入一个待办事项
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
			)

		# 他在一个文本框中输入了"Buy peacock feathers"（购买孔雀羽毛）
		# yaoel的爱好是使用假蝇做鱼饵钓鱼
		inputbox.send_keys('Buy peacock feathers')

		# 他按下回车键后，页面更新了
		# 待办事项表格中显示了"1: Buy peack feathers"
		inputbox.send_keys(Keys.ENTER)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn('1: Buy peacock feathers', [row.text for row in rows])

		# 页面上又显示了一个文本框，可以输入其他待办事项
		# 他输入了"Use peacock feathers to make a fly"（使用孔雀羽毛做假蝇）
		# yaoel做事很有条例
		self.fail('Finish the test!')


if __name__ == '__main__':
	unittest.main(warnings='ignore')
