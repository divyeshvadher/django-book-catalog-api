from rest_framework import serializers
from .models import Book
import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_isbn(self, value):
        if len(value) != 13:
            raise serializers.ValidationError("ISBN must be exactly 13 characters.")
        return value

    def validate_page_count(self, value):
        if value < 1:
            raise serializers.ValidationError("Page count must be at least 1.")
        return value

    def validate_published_date(self, value):
        if value > datetime.date.today():
            raise serializers.ValidationError("Published date cannot be in the future.")
        return value
