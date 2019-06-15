import time

from base.base_driver import init_driver
from page.page import Page


class TestShopCart:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    def test_add_shop_cart(self):
        # 首页，如果没有登录就登录
        self.page.home.login_if_not(self.page)
        # 首页 - 分类
        self.page.home.click_category()
        # 分类 - 商品列表
        self.page.category.click_goods_list()
        # 商品列表 - 商品详情
        self.page.goods_list.click_goods()
        # 记录一下 当前商品的标题
        goods_title = self.page.goods_detail.get_goods_title_text()
        # 商品详情 - 加入购物车
        self.page.goods_detail.click_add_shop_cart()
        # 商品详情 - 选择规格
        self.page.goods_detail.click_spec()
        # 商品详情 - 购物车
        self.page.goods_detail.click_shop_cart()

        time.sleep(2)

        # 根据添加完成之后的页面，是否用相同商品标题进行判断
        assert self.page.goods_detail.is_goods_title_exist(goods_title)
