from django.db.models import (
    Count,
    Prefetch,
    QuerySet
)

from blog import models


class PostQuerySet(QuerySet):

    def popular(self):
        posts_by_likes_count = (self.annotate(likes_count=Count('likes'))
                                .order_by('-likes_count'))

        return posts_by_likes_count

    def fetch_with_comments_count(self):
        posts_ids = [post.id for post in self]
        posts_with_comments_count_field = (self.model.objects
                                           .filter(id__in=posts_ids)
                                           .annotate(comments_count=Count('comments')))

        ids_and_comments_count = (posts_with_comments_count_field
                                  .values_list('id', 'comments_count'))

        count_for_id = dict(ids_and_comments_count)
        for post in self:
            post.comments_count = count_for_id[post.id]

        return list(self)

    def prefetch_tags_by_posts(self):
        tags_with_posts_count = models.Tag.objects.annotate(posts_count=Count('posts'))

        prefetch = Prefetch('tags', queryset=tags_with_posts_count)
        posts_with_tags = self.prefetch_related(prefetch)

        return posts_with_tags

    def year(self, year):
        posts_at_year = (self.filter(published_at__year=year)
                         .order_by('published_at'))

        return posts_at_year


class TagQuerySet(QuerySet):

    def popular(self):
        tags_by_posts_count = (self.annotate(posts_count=Count('posts'))
                               .order_by('-posts_count'))

        return tags_by_posts_count
