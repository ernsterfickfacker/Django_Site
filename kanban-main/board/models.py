import uuid

from django.db import models
from drf_yasg.utils import swagger_auto_schema
# @api_view(http_method_names=["GET", "POST"])
# @permission_classes([AllowAny])
@swagger_auto_schema(operation_summary="Посмотреть список задач")
class Task(models.Model):
    class boardNames(models.TextChoices):
        ToDo = 'Сделать'
        InProgress = 'В процессе'
        Review = 'На проверке'
        Done = 'Выполнено'
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE,
                              related_name='tasks')
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,
                            editable=False)
    name = models.CharField(max_length=500)
    boardName = models.CharField(max_length=12, choices=boardNames.choices,
                                 default=boardNames.ToDo)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return str(self.name)
