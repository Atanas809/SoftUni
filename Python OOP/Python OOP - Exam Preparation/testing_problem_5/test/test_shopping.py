from unittest import TestCase, main

from structure_and_functionality_5.shopping_cart import ShoppingCart


class ShoppingTests(TestCase):
    def test_init_is_initialized_correctly(self):
        cart = ShoppingCart("HM", 1000.5)

        self.assertEqual('HM', cart.shop_name)
        self.assertEqual(1000.5, cart.budget)
        self.assertEqual({}, cart.products)

    def test_shop_name_with_lowercase_first_char_raises(self):
        cart = ShoppingCart("HM", 1000.5)

        with self.assertRaises(ValueError) as ex:
            cart.shop_name = "aaap"

        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ex.exception))

    def test_shop_name_with_non_alpha_chars_first_char_raises(self):
        cart = ShoppingCart("HM", 1000.5)

        with self.assertRaises(ValueError) as ex:
            cart.shop_name = "A1pld2"

        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ex.exception))

    def test_add_to_cart_with_value_equal_to_min_price_raises(self):
        cart = ShoppingCart("HM", 1000.5)

        with self.assertRaises(ValueError) as ex:
            cart.add_to_cart('Apple', 100)

        self.assertEqual("Product Apple cost too much!", str(ex.exception))

    def test_add_to_cart_with_value_more_than_min_price_raises(self):
        cart = ShoppingCart("HM", 1000.5)

        with self.assertRaises(ValueError) as ex:
            cart.add_to_cart('Apple', 200)

        self.assertEqual("Product Apple cost too much!", str(ex.exception))

    def test_add_to_cart_adding_correctly_to_products_dict(self):
        cart = ShoppingCart("HM", 1000.5)

        self.assertEqual({}, cart.products)

        result = cart.add_to_cart('Apple', 10)
        expected_result = "Apple product was successfully added to the cart!"

        self.assertEqual(expected_result, result)
        self.assertEqual({'Apple': 10}, cart.products)

    def test_remove_from_cart_with_non_existing_product_raises(self):
        cart = ShoppingCart("HM", 1000.5)

        self.assertEqual({}, cart.products)

        cart.add_to_cart('Apple', 10)
        self.assertEqual({'Apple': 10}, cart.products)

        with self.assertRaises(ValueError) as ex:
            cart.remove_from_cart("Orange")

        self.assertEqual("No product with name Orange in the cart!", str(ex.exception))
        self.assertEqual({'Apple': 10}, cart.products)

    def test_remove_from_cart_with_existing_product_returns_correctly(self):
        cart = ShoppingCart("HM", 1000.5)

        self.assertEqual({}, cart.products)

        cart.add_to_cart('Apple', 10)
        self.assertEqual({'Apple': 10}, cart.products)

        result = cart.remove_from_cart("Apple")
        expected_result = "Product Apple was successfully removed from the cart!"

        self.assertEqual(expected_result, result)
        self.assertEqual({}, cart.products)

    def test_add_method_returns_new_instance_correctly(self):
        cart1 = ShoppingCart("HM", 1000.5)
        cart2 = ShoppingCart("Bershka", 2000.5)

        cart1.add_to_cart('Apple', 10)
        cart2.add_to_cart('Orange', 10)

        new_shop = cart1 + cart2

        self.assertEqual("HMBershka", new_shop.shop_name)
        self.assertEqual(3001.0, new_shop.budget)
        self.assertEqual({'Apple': 10, 'Orange': 10}, new_shop.products)

    def test_buy_products_with_lower_budget_than_total_sum_raises(self):
        cart = ShoppingCart("HM", 30)

        self.assertEqual({}, cart.products)

        cart.add_to_cart('Apple', 50)
        cart.add_to_cart('Orange', 10)

        self.assertEqual({'Apple': 50, 'Orange': 10}, cart.products)

        with self.assertRaises(ValueError) as ex:
            cart.buy_products()

        self.assertEqual("Not enough money to buy the products! Over budget with 30.00lv!", str(ex.exception))

    def test_buy_products_with_possible_budget_to_spend(self):
        cart = ShoppingCart("HM", 1000.0)

        self.assertEqual({}, cart.products)

        cart.add_to_cart('Apple', 50)
        cart.add_to_cart('Orange', 10)

        self.assertEqual({'Apple': 50, 'Orange': 10}, cart.products)

        result = cart.buy_products()
        expected_result = 'Products were successfully bought! Total cost: 60.00lv.'

        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()
