from rest_framework import serializers
from .models import ClassRoom, StudyMaterial, AssignmentPDF, Assignment, Question, Choice


class ClassRoomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ['id', 'classname', 'email', 'created_at']
        # read_only = ['id']


class StudyMaterialModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyMaterial
        fields = ['id', 'file_title', 'video_title', 'files', 'videos', 'created_at', 'updated_at', 'classid']


class AssignmentPDFModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentPDF
        fields = ['id', 'file_title', 'files', 'created_at', 'updated_at', 'classid']


class StringModelSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value


class QuestionModelSerializer(serializers.ModelSerializer):
    choices = StringModelSerializer(many=True)

    class Meta:
        model = Question
        fields = ('id', 'choices', 'question', 'order')


class AssignmentModelSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()

    class Meta:
        model = Assignment
        fields = '__all__'

    # def get_questions(self, obj):
    #     questions = QuestionModelSerializer(obj.questions.all(), many=True).data
    #     return questions
    #
    # def create(self, request):
    #     data = request.data
    #
    #     assignment = Assignment()
    #     assignment.title = data['file_title']
    #     assignment.save()
    #
    #     order = 1
    #     for q in data['questions']:
    #         newQ = Question()
    #         newQ.question = q['file_title']
    #         newQ.order = order
    #         newQ.save()
    #
    #         for c in q['choices']:
    #             newC = Choice()
    #             newC.title = c
    #             newC.save()
    #             newQ.choices.add(newC)
    #
    #         newQ.answer = Choice.objects.get(title=q['answer'])
    #         newQ.assignment = assignment
    #         newQ.save()
    #         order += 1
    #     return assignment

