from django.contrib import admin
from .models import Day, Tour, TermsAndConditions,CancellationPolicy, Included, Excluded
from django.forms import inlineformset_factory

DayFormSet = inlineformset_factory(Tour, Day, fields=('number_order', 'title', 'description', 'picture'), extra=1)
class DayInline(admin.TabularInline):
    model = Day
    extra = 1

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    inlines = [DayInline]

admin.site.register(TermsAndConditions)
admin.site.register(CancellationPolicy)
admin.site.register(Included)
admin.site.register(Excluded)