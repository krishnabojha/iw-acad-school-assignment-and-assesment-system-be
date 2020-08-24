from rest_framework.viewsets import ModelViewSet
from .serializers import (SubjectSerializer,
                          AssignmentSerializer,
                          QuestionSerializer,
                          AnswerSerializer)
from .models import Subject, Assignment, Question, Answer


class SubjectModelCreateView(ModelViewSet):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()


class AssignmentViewSet(ModelViewSet):
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()

class QuestionViewSet(ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class AnswerViewSet(ModelViewSet):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
