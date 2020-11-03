from django.contrib import admin
from unycAPI.models import Biere, Stock, Ranking

# Register your models here.
class BieresAdmin(admin.ModelAdmin):
    pass
class StockAdmin(admin.ModelAdmin):
    pass
class RankingAdmin(admin.ModelAdmin):
    pass
admin.site.register(Biere, BieresAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(Ranking, RankingAdmin)