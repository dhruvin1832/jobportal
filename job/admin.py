from django.contrib import admin
from .models import MyUser,Company,PostJob,ApplyJob,Question,Result,Contact
# Register your models here.
admin.site.register(MyUser)
admin.site.register(Company)
admin.site.register(PostJob)
admin.site.register(ApplyJob)
admin.site.register(Question)
admin.site.register(Result)
admin.site.register(Contact)