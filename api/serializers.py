from rest_framework.serializers import ModelSerializer, SerializerMethodField
from projects.models import Project, Tag, Review
from users.models import Profile


class ProfileSerializers(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'        # in json it was not showing profile and tag objects it was just showing id's so to get details we did this

class TagSerializers(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class ReviewSerializers(ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ProjectSerializers(ModelSerializer):
    owner = ProfileSerializers()
    tags = TagSerializers(many=True)
    reviews = SerializerMethodField()

    class Meta:
        model = Project
        fields = '__all__'

    def get_reviews(self, obj):
        reviews = obj.review_set.all()
        serializer = ReviewSerializers(reviews, many=True)
        return serializer.data