from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from faker import Faker
from blog.models import Post, Comment


class Command(BaseCommand):
    help = 'Generate random blog posts and comments'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Indicates the number of posts and comments to be created')

    def handle(self, *args, **kwargs):
        fake = Faker()
        count = kwargs['count']

        User = get_user_model()
        superuser = User.objects.get(username='admin')

        for _ in range(count):
            title = fake.sentence()
            content = fake.text()
            post = Post(title=title, content=content,
                        owner=superuser)
            post.save()

            username = fake.user_name()
            text = fake.paragraph()
            comment = Comment(
                post=post,
                owner=superuser,
                text=text
            )
            comment.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully generated {count} posts and comments for each post'))
