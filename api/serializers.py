from rest_framework import serializers
from projects.models import Project, Tag, Review
from users.models import Profile


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    owner = ProfileSerializer(many=False)  # даём доступ связанным моделям
    tags = TagSerializer(many=True)
    reviews = serializers.SerializerMethodField()  # для child objects

    class Meta:
        model = Project
        fields = "__all__"

    def get_reviews(self, obj):  # для child objects
        reviews = obj.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return serializer.data
