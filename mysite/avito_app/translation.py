from modeltranslation.translator import TranslationOptions,register
from .models import Category, SubCategory, Product

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name', )

@register(SubCategory)
class SubcategoryTranslationOptions(TranslationOptions):
    fields = ('subcategory_name', )

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('product_name', 'description')