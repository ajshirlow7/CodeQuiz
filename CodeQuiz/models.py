
from django.db import models

class LeaderboardEntry(models.Model):
	username = models.CharField(max_length=150)
	html_score = models.IntegerField(default=0)
	css_score = models.IntegerField(default=0)
	javascript_score = models.IntegerField(default=0)
	python_score = models.IntegerField(default=0)

	def total_score(self):
		return self.html_score + self.css_score + self.javascript_score + self.python_score

	def __str__(self):
		return f"{self.username} ({self.total_score()})"
