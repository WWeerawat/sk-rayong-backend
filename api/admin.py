from multiprocessing import Lock
from django.contrib import admin

from .models import LockImage, Lock, Nearyby, Phase, PhaseImage

# Register your models here.
admin.site.register(Phase)
admin.site.register(PhaseImage)
admin.site.register(Lock)
admin.site.register(LockImage)
admin.site.register(Nearyby)
