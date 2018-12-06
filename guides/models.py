from enum import Enum

from django.conf import settings
from django.contrib.postgres.fields import JSONField
from django.db import models

from taggit.managers import TaggableManager


class CharacterChoices(Enum):
    Shadow = "Shadow"
    Ranger = "Ranger"
    Marauder = "Marauder"
    Duelist = "Duelist"
    Templar = "Templar"
    Witch = "Witch"
    Scion = "Scion"


Ascendancies = (
    ('Scion', (
        ('Ascendant', 'Ascendant'),
    )),
    ('Shadow', (
        ('Trickster', 'Trickster'),
        ('Saboteur', 'Saboteur'),
        ('Assassin', 'Assassin'),
    )),
    ('Duelist', (
        ('Slayer', 'Slayer'),
        ('Gladiator', 'Gladiator'),
        ('Champion', 'Champion'),
    )),
    ('Witch', (
        ('Necromancer', 'Necromancer'),
        ('Elementalist', 'Elementalist'),
        ('Occultist', 'Occultist'),
    )),
    ('Templar', (
        ('Inquisitor', 'Inquisitor'),
        ('Hierophant', 'Hierophant'),
        ('Guardian', 'Guardian'),
    )),
    ('Marauder', (
        ('Juggernaut', 'Juggernaut'),
        ('Berserker', 'Berserker'),
        ('Chieftain', 'Chieftain'),
    )),
    ('Ranger', (
        ('Deadeye', 'Deadeye'),
        ('Raider', 'Raider'),
        ('Pathfinder', 'Pathfinder'),
    )),
)


# Create your models here.
class Guide(models.Model):
    LOW_QUALITY_THRESHOLD = -10

    ascendancy = models.CharField(max_length=20, choices=Ascendancies)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    character_class = models.CharField(max_length=15, choices=[(tag, tag.value) for tag in CharacterChoices])
    content = JSONField()
    items = JSONField()
    patch_version = models.CharField(max_length=10)
    primary_skill = models.CharField(max_length=100)
    published = models.BooleanField(default=False)
    score = models.IntegerField()
    tags = TaggableManager()
    title = models.CharField(max_length=155)


    def primary_skill_icon(self):
        pass

    def upvote(self):
        pass

    def downvote(self):
        pass

    def __str__(self):
        return '{title} by {author}'.format(title=self.title, author=self.author.username)

    def is_visible(self):
        return self.score >= LOW_QUALITY_THRESHOLD
