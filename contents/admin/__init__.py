from django.contrib import admin
from contents.models import *
from .post import PostAdmin
from .interaction import InteractionAdmin
from .comment import CommentAdmin
from .keyword import KeywordAdmin



admin.site.register(Post,PostAdmin)
admin.site.register(Interaction,InteractionAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Keyword,KeywordAdmin)