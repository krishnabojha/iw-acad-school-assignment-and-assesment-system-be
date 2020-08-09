from rest_framework import serializers
from .models import Info

class AddTwoNumbersSerializer(serializers.Serializer):
    number1 = serializers.IntegerField()
    number2 = serializers.IntegerField()

class InfoSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 200)
    address = serializers.CharField(max_length = 200)

    def create(self, validated_data):
        print('current time in serializer : ', self.context)
        return Info.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.address = validated_data['address']
        instance.save()
        return instance

class InfoModelSerializer(serializers.ModelSerializer):
    message = serializers.SerializerMethodField()
    class Meta:
        model = Info
        fields = ['name', 'address', 'message', 'id']
        ## this will help you not to post id 
        read_only = ['id']

    def get_message(self, obj):
        name = obj.name
        return f'Hello i am {name}'
    @staticmethod
    def validate_name(name):
        if len(name) <3:
            raise serializers.ValidationError('The name should have more than 3 character.')
        return name

    def validate(self, data):
        print(data)
        name = data['name']
        address = data['address']
        if name == address:
            raise serializers.ValidationError('The name and address can not be same.')
        return data