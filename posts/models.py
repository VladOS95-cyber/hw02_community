from django.db import models


from django.contrib.auth import get_user_model


User = get_user_model()


class Post(models.Model):
    """Модель публикации, содержащая
    текст к публикации, дату, имя автора и
    ссылку на модель Group
    """

    text = models.TextField()
    pub_date = models.DateField("date published", auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, 
        related_name="posts"
    )
    group = models.ForeignKey(
        "Group", on_delete=models.CASCADE, blank=True, null=True
    )


class Group(models.Model):
    """Модель сообщества куда буду попадать публикации
    в зависимости от тематики. Блогер будет иметь возможность
    самостоятельно выбрать группу, но создать группу
    смогут только админы. Модель имеет свойства:
    title(имя), адрес(slug) и описание(description)
    """

    title = models.CharField()
    slug = models.SlugField()
    description = models.TextField()

    def __str__(self):
        """Метод для печати поля title"""

        return self.title



