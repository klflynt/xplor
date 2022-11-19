from rest_framework import serializers

from .models import Fizzbuzz

class FizzbuzzSerializer(serializers.ModelSerializer):
    # fizzbuzz_id = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Fizzbuzz
        fields = [
            'id',
            'created_at',
            # 'useragent',
            'message',
            # 'fizzbuzz_id',
        ]
    # def get_my_fizzID(self, obj):
    #     return obj.get_fizzbuzz_id()