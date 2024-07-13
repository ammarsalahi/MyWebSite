from django.contrib import admin
from contents.models import *
from .post import PostAdmin
from .keyword import KeywordAdmin
from .category import CategoryAdmin
from .project import ProjectAdmin
from .techology import TechnologyAdmin
from .image import ImageAdmin

# admin.site.register(Post,PostAdmin)
# admin.site.register(Comment,CommentAdmin)
# admin.site.register(Keyword,KeywordAdmin)