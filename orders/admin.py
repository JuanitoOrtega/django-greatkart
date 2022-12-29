from django.contrib import admin
from .models import Payment, Order, OrderProduct


class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user', 'payment_id', 'payment_method', 'amount_paid', 'created_at', 'status']
    list_filter = ['user', 'payment_method', 'status']
    search_fields = ['user', 'payment_id', 'payment_method']
    list_per_page = 20


class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('payment', 'user', 'product', 'quantity', 'product_price', 'ordered')
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'full_name', 'phone', 'email', 'city', 'order_total', 'tax', 'status', 'created_at', 'is_ordered']
    list_filter = ['status', 'is_ordered']
    search_fields = ['order_number', 'first_name', 'last_name', 'phone', 'email']
    list_per_page = 20
    inlines = [OrderProductInline]


class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'payment', 'order', 'user', 'quantity', 'product_price', 'created_at', 'ordered']
    list_display_links = ['product']
    list_filter = ['user', 'product', 'ordered']
    search_fields = ['user', 'product']
    list_per_page = 20


admin.site.register(Payment, PaymentAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct, OrderProductAdmin)