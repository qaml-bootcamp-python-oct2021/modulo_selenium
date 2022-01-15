from proyecto_final.pages.base_page import BasePage
from selenium.webdriver.common.by import By
import proyecto_final.util.constants as constants


class ProductPage(BasePage):
    _h1_product = (By.XPATH, '//*[@id="content"]//h1')
    _input_quantity = (By.ID, 'input-quantity')
    _span_car_total = (By.ID, 'cart-total')
    _button_add_car = (By.ID, 'button-cart')

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def verify_input_quantity(self):
        assert self.is_displayed(
            self._input_quantity), 'No se encuentra la caja de texto quantity'

    def verify_span_car_total(self):
        assert self.is_displayed(
            self._span_car_total), 'No se encuentra la etiqueta car total'

    def verify_btn_add_car(self):
        assert self.is_displayed(
            self._button_add_car), 'No se encuentra el botón Add to car'

    def verify_header(self):
        assert self.is_displayed(
            self._h1_product), 'No se encuentra la etiqueta h1'

    def verify_header_text_content(self, text_expected):
        text_h1 = self.get_element(self._h1_product).text
        try:
            assert text_expected == text_h1
        except AssertionError:
            self.take_screenshot(constants.EVIDENCE_ERROR,
                                 f'featured_detail_{text_expected}')
            raise AssertionError(
                f'Titulo esperado{text_expected}, titulo obtenido :{text_h1}')

    def write_quantity(self, quantity):
        self.verify_input_quantity()
        self.get_element(self._input_quantity).send_keys(quantity)

    def add_to_car(self):
        self.verify_btn_add_car()
        self.click_element(self._button_add_car)

    def verify_quantity(self, quantity_expected):
        self.verify_element_visible(self._span_car_total)
        car_total = self.get_element(self._span_car_total)
        print(car_total.text)
        car_quantity_text = car_total.text.split("-")[0]
        print(car_quantity_text)
        try:
            assert quantity_expected.strip() == car_quantity_text.strip()
        except AssertionError:
            self.take_screenshot(constants.EVIDENCE_ERROR,'verify_quantity')
            raise AssertionError(f'Quantity actual:{ car_quantity_text}, Quantity agregado: {quantity_expected}.')
