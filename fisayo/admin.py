from django.contrib import admin

# Register your models here.
from .models import Home, About, Profile, Category, Skills, Portfolio, Contact, Details

# Home
admin.site.register(Home)


# About
class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 1

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
     inlines = [
        ProfileInline,
    ]

# Skills
class SkillsInline(admin.TabularInline):
    model = Skills
    extra = 2

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
     inlines = [
        SkillsInline,
    ]


#Details
class DetailsInline(admin.TabularInline):
    model = Details

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    inlines = [
        DetailsInline,
    ]

# Portfolio
admin.site.register(Portfolio)