from django.db import models


class PostQuerySet(models.QuerySet):

    def year(self, year):
        posts_at_year = (self.filter(published_at__year=year)
                         .order_by('published_at'))

        return posts_at_year
