from django.test import TestCase


class MenuPageTests(TestCase):
    def test_menu_shows_52_products_with_an_image_for_each_category(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        products = response.context["products"]
        self.assertEqual(len(products), 52)
        self.assertEqual(response.content.decode().count('class="food"'), 52)
        self.assertTrue(all(product["image"].startswith("https://images.unsplash.com/photo-") for product in products))
        self.assertTrue(all(product["image"] and product["name"] for product in products))
        self.assertEqual(
            {product["category"] for product in products},
            {"taom", "milliy", "desert", "ichimlik"},
        )