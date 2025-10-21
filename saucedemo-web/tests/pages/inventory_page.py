class InventoryPage:
    TITLE = ".title"
    ADD_TO_CART_BTNS = "[data-test^='add-to-cart']"
    CART_BADGE = ".shopping_cart_badge"
    CART_LINK = ".shopping_cart_link"
    CHECKOUT_BTN = "[data-test='checkout']"

    def __init__(self, page):
        self.page = page

    def is_open(self):
        title = self.page.text_content(self.TITLE)
        return (title or "").strip() == "Products"

    def add_first_n_items(self, n=1):
        buttons = self.page.locator(self.ADD_TO_CART_BTNS)
        cnt = buttons.count()
        for i in range(min(cnt, n)):
            buttons.nth(i).click()

    def cart_count(self):
        badge = self.page.locator(self.CART_BADGE)
        return int(badge.text_content()) if badge.count() else 0

    def open_cart(self):
        self.page.click(self.CART_LINK)

    def can_checkout(self):
        return self.page.locator(self.CHECKOUT_BTN).is_visible()
