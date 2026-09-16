import random

from django.core.management.base import BaseCommand
from django.utils import timezone

from avito_app.models import (
    UserProfile,
    Category,
    SubCategory,
    Product,
    ProductImages,
    Reviews,
)


class Command(BaseCommand):
    help = "Заполняет базу тестовыми данными (с переводами en/ru)"

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING("Начинаем заполнение базы данными..."))

        # ---------- USERS ----------
        users_data = [
            {
                "username": "asel_2026",
                "email": "asel@example.com",
                "age": 25,
                "phone_number": "+996700111222",
                "status": "gold",
            },
            {
                "username": "bakyt_dev",
                "email": "bakyt@example.com",
                "age": 30,
                "phone_number": "+996700333444",
                "status": "silver",
            },
            {
                "username": "cholpon77",
                "email": "cholpon@example.com",
                "age": 22,
                "phone_number": "+996700555666",
                "status": "bronze",
            },
            {
                "username": "damir_user",
                "email": "damir@example.com",
                "age": 40,
                "phone_number": "+996700777888",
                "status": "simple",
            },
        ]

        users = []
        for data in users_data:
            user, created = UserProfile.objects.get_or_create(
                username=data["username"],
                defaults={
                    "email": data["email"],
                    "age": data["age"],
                    "phone_number": data["phone_number"],
                    "status": data["status"],
                    "avatar": "profile_image/default_avatar.jpg",
                },
            )
            if created:
                user.set_password("test12345")
                user.save()
            users.append(user)
            self.stdout.write(f"  Пользователь: {user.username}")

        # ---------- CATEGORIES (с переводами) ----------
        categories_data = [
            {
                "en": "Electronics",
                "ru": "Электроника",
                "image": "category_image/electronics.jpg",
            },
            {
                "en": "Clothing",
                "ru": "Одежда",
                "image": "category_image/clothing.jpg",
            },
            {
                "en": "Home & Garden",
                "ru": "Дом и сад",
                "image": "category_image/home_garden.jpg",
            },
        ]

        categories = []
        for cat in categories_data:
            category, _ = Category.objects.get_or_create(
                category_name_en=cat["en"],
                defaults={
                    "category_name_ru": cat["ru"],
                    "category_image": cat["image"],
                },
            )
            categories.append(category)
            self.stdout.write(f"  Категория: {category.category_name_en} / {category.category_name_ru}")

        # ---------- SUBCATEGORIES (с переводами) ----------
        subcategories_data = [
            {"category": categories[0], "en": "Smartphones", "ru": "Смартфоны", "image": "subcategory_image/smartphones.jpg"},
            {"category": categories[0], "en": "Laptops", "ru": "Ноутбуки", "image": "subcategory_image/laptops.jpg"},
            {"category": categories[1], "en": "Men's Clothing", "ru": "Мужская одежда", "image": "subcategory_image/men_clothing.jpg"},
            {"category": categories[1], "en": "Women's Clothing", "ru": "Женская одежда", "image": "subcategory_image/women_clothing.jpg"},
            {"category": categories[2], "en": "Furniture", "ru": "Мебель", "image": "subcategory_image/furniture.jpg"},
        ]

        subcategories = []
        for sub in subcategories_data:
            subcategory, _ = SubCategory.objects.get_or_create(
                subcategory_name_en=sub["en"],
                category=sub["category"],
                defaults={
                    "subcategory_name_ru": sub["ru"],
                    "subcategory_image": sub["image"],
                },
            )
            subcategories.append(subcategory)
            self.stdout.write(f"  Подкатегория: {subcategory.subcategory_name_en} / {subcategory.subcategory_name_ru}")

        # ---------- PRODUCTS (с переводами) ----------
        products_data = [
            {
                "subcategory": subcategories[0],
                "name_en": "iPhone 15 Pro",
                "name_ru": "Айфон 15 Про",
                "desc_en": "Latest Apple smartphone with A17 chip",
                "desc_ru": "Новейший смартфон Apple с чипом A17",
                "price": 999.99,
                "article_number": 1000001,
            },
            {
                "subcategory": subcategories[0],
                "name_en": "Samsung Galaxy S24",
                "name_ru": "Самсунг Гэлакси С24",
                "desc_en": "Flagship Android smartphone",
                "desc_ru": "Флагманский смартфон на Android",
                "price": 899.99,
                "article_number": 1000002,
            },
            {
                "subcategory": subcategories[1],
                "name_en": "MacBook Air M3",
                "name_ru": "Макбук Эйр М3",
                "desc_en": "Lightweight and powerful laptop",
                "desc_ru": "Лёгкий и мощный ноутбук",
                "price": 1299.99,
                "article_number": 1000003,
            },
            {
                "subcategory": subcategories[2],
                "name_en": "Men's Denim Jacket",
                "name_ru": "Мужская джинсовая куртка",
                "desc_en": "Classic denim jacket for everyday wear",
                "desc_ru": "Классическая джинсовая куртка на каждый день",
                "price": 59.99,
                "article_number": 1000004,
            },
            {
                "subcategory": subcategories[3],
                "name_en": "Women's Summer Dress",
                "name_ru": "Женское летнее платье",
                "desc_en": "Light and comfortable summer dress",
                "desc_ru": "Лёгкое и удобное летнее платье",
                "price": 39.99,
                "article_number": 1000005,
            },
            {
                "subcategory": subcategories[4],
                "name_en": "Wooden Coffee Table",
                "name_ru": "Деревянный журнальный столик",
                "desc_en": "Solid wood coffee table for living room",
                "desc_ru": "Журнальный столик из массива дерева для гостиной",
                "price": 149.99,
                "article_number": 1000006,
            },
        ]

        products = []
        for prod in products_data:
            product, _ = Product.objects.get_or_create(
                article_number=prod["article_number"],
                defaults={
                    "subcategory": prod["subcategory"],
                    "product_name_en": prod["name_en"],
                    "product_name_ru": prod["name_ru"],
                    "description_en": prod["desc_en"],
                    "description_ru": prod["desc_ru"],
                    "price": prod["price"],
                    "product_type": True,
                },
            )
            products.append(product)
            self.stdout.write(f"  Товар: {product.product_name_en} / {product.product_name_ru}")

        # ---------- PRODUCT IMAGES ----------
        for i, product in enumerate(products):
            for j in range(2):  # по 2 картинки на товар
                ProductImages.objects.get_or_create(
                    product=product,
                    product_image=f"product_images/product_{i+1}_{j+1}.jpg",
                )
        self.stdout.write("  Изображения товаров созданы")

        # ---------- REVIEWS ----------
        comments_data = [
            {"en": "Great product, highly recommend!", "ru": "Отличный товар, всем советую!"},
            {"en": "Good quality but delivery was slow.", "ru": "Хорошее качество, но доставка была долгой."},
            {"en": "Not what I expected.", "ru": "Не то, что ожидал."},
            {"en": "Excellent value for money.", "ru": "Отличное соотношение цены и качества."},
        ]

        for product in products:
            for user in random.sample(users, k=2):
                comment = random.choice(comments_data)
                Reviews.objects.get_or_create(
                    user=user,
                    product=product,
                    defaults={
                        "stars": str(random.randint(3, 5)),
                        "comments": f"{comment['en']} / {comment['ru']}",
                        "review_image": "review_images/default_review.jpg",
                    },
                )
        self.stdout.write("  Отзывы созданы")

        self.stdout.write(self.style.SUCCESS("Готово! База данных успешно заполнена тестовыми данными."))

