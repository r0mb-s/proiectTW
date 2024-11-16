from django.db import models


class QuizClass(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class Student(models.Model):
    class_name = models.ForeignKey(
        QuizClass, related_name="students", on_delete=models.CASCADE
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Quiz(models.Model):
    class_name = models.ForeignKey(
        QuizClass, related_name="quizes", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    number_of_questions = models.IntegerField()
    questions = models.JSONField()
    answers = models.JSONField()


class QuizTry(models.Model):
    quiz_name = models.ForeignKey(Quiz, related_name="quiz", on_delete=models.CASCADE)
    student_name = models.ForeignKey(
        Student, related_name="student", on_delete=models.CASCADE
    )
    timestamp = models.DateTimeField()
    answers = models.JSONField()

class Question(models.Model):
    question_text = models.TextField()
    answer_1 = models.CharField(max_length=255)
    answer_2 = models.CharField(max_length=255)
    answer_3 = models.CharField(max_length=255)
    answer_4 = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)

    def __str__(self):
        return self.question_text