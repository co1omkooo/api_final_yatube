from django.contrib.auth import get_user_model
from django.db import models

from .constants import SLICE_SIZE, TEXT_LENGTH

User = get_user_model()


class Group(models.Model):
    """Группы."""

    title = models.CharField(max_length=TEXT_LENGTH,
                             verbose_name='Название')
    slug = models.SlugField(unique=True,
                            verbose_name='Слаг')
    description = models.TextField(
        verbose_name='Описание',
    )

    class Meta:
        verbose_name = 'Группы'

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='posts/',
        null=True,
        blank=True
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        verbose_name='Группа',
        blank=True,
        null=True
    )

    class Meta:
        ordering = ('-pub_date', )
        default_related_name = 'posts'
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.text[:SLICE_SIZE]


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    class Meta:
        default_related_name = 'comments'
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('created',)

    def __str__(self):
        return self.text[:SLICE_SIZE]


class Follow(models.Model):
    """Подписки."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='На кого подписаны'
    )

    class Meta:
        verbose_name = 'Подписки'
        constraints = [
            models.CheckConstraint(
                check=~models.Q(user=models.F('following')),
                name='no_self_follow'
            ),
            models.UniqueConstraint(
                fields=('user', 'following'),
                name='unique_user_following'),
        ]
