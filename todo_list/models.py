from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    content = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks", blank=True)

    class Meta:
        ordering = ("is_done", "-created_at")

    def get_date(self) -> str:
        created = self.created_at.strftime("%B %d, %Y, %I:%M %p")
        deadline = (
            f" | Deadline: {self.deadline:%B %d, %Y, %I:%M %p}"
            if self.deadline else ""
        )
        return f"Created: {created}{deadline}"

    def __str__(self) -> str:
        return self.content
