# Понабится для др.проектов чтобы реализовать сессионую корзину!
# from decimal import Decimal  # правильное название модуля
# from django.shortcuts import get_object_or_404  # get_list_or_404 не нужен
# from main.models import Product


# class Cart:
#     def __init__(self, request):  # было __inir__ — опечатка
#         self.session = request.session
#         cart = self.session.get('cart')
#         if not cart:
#             cart = self.session['cart'] = {}  # было self,self.session['cart'] == {}
#         self.cart = cart

#     def add(self, product, size, quantity=1, override_quantity=False):
#         product_id = str(product.id)
#         size_name = str(size)
#         cart_key = f"{product_id}_{size_name}"

#         if cart_key not in self.cart:
#             self.cart[cart_key] = {
#                 'quantity': 0,
#                 'price': str(product.price),  # было prise + не было запятой
#                 'product_id': product_id,
#                 'size': size_name,
#             }
#         if override_quantity:
#             self.cart[cart_key]['quantity'] = override_quantity
#         else:
#             self.cart[cart_key]['quantity'] += quantity

#         self.save()  # было self.safe()

#     def save(self):
#         self.session.modified = True

#     def remove(self, product, size):
#         product_id = str(product.id)
#         size_name = str(size)
#         cart_key = f"{product_id}_{size_name}"

#         if cart_key in self.cart:  # было вне метода — неправильный отступ!
#             del self.cart[cart_key]
#             self.save()

#     def update_quantity(self, product, size, quantity):  # было update_qunatity
#         if quantity > 0:  # было <= 0 — логика была перевёрнута!
#             self.add(product, size, quantity, override_quantity=True)
#         else:
#             self.remove(product, size)

#     def __iter__(self):
#         product_ids = [item['product_id'] for item in self.cart.values()]  # было [item['product_id']] — лишние скобки
#         products = Product.objects.filter(id__in=product_ids)
#         cart = self.cart.copy()

#         for product in products:
#             for cart_key, cart_item in cart.items():  # было cart_items — не существует
#                 if cart_item['product_id'] == str(product.id):
#                     cart_item['product'] = product
#                     cart_item['price'] = Decimal(cart_item['price'])
#                     cart_item['total_price'] = cart_item['price'] * cart_item['quantity']
#                     yield cart_item

#     def __len__(self):
#         return sum(item['quantity'] for item in self.cart.values())

#     def get_total_price(self):
#         return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

#     def clear(self):
#         del self.session['cart']
#         self.save()
    

#     def get_cart_items(self):
#         items = []
#         for item in self:
#             items.append({
#             'product': item['product'],
#             'quantity': item['quantity'],
#             'size': item['size'],
#             'price': Decimal(item['price']),
#             'total_price': item['total_price'],
#             'cart_key': f"{item['product_id']}_{item['size']}"
#         })
#         return items