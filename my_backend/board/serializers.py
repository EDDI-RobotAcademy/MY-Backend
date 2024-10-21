from rest_framework import serializers

from board.entity.boardcategory import BoardCategory
from board.entity.models import Board



class BoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Board
        fields = ['boardId', 'title', 'account', 'content', 'regDate', 'updDate', 'category_id', 'categoryBoardId']
        read_only_fields = ['boardId', 'regDate', 'updDate', 'categoryBoardId']

    def validate_category_id(self, value):
        try:
            BoardCategory.objects.get(pk=value)
        except BoardCategory.DoesNotExist:
            raise serializers.ValidationError(f"Category with id {value} does not exist.")
        return value

    def create(self, validated_data):
        category_id = validated_data.pop('category_id')
        category = BoardCategory.objects.get(pk=category_id)
        board = Board.objects.create(category=category, **validated_data)
        return board


class BoardCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardCategory
        fields = ['categoryId', 'name']
