from dataclasses import fields
from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform,Review



class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        exclude = ['watchlist']



class WatchListSerializer(serializers.ModelSerializer):
    # length_name = serializers.SerializerMethodField()
    reviews = ReviewSerializer(many=True , read_only=True)
    platform = serializers.CharField(source = "platform.name")


    # reviews = serializers.StringRelatedField(many=True, read_only = True)


    class Meta:
        model= WatchList
        fields = "__all__"
        # exclude = ["active"]

    # def get_length_name(self,object):
    #     return len(object.name)

    # def validate(self, data):
    #     if data["name"] == data["description"]:
    #         raise serializers.ValidationError("Title and description should be different")
       
    #     return data

    # def validate_name(self,value):
    #     if len(value) <= 2:
    #         raise serializers.ValidationError("Name is too short")
    #     else:
    #         return value


# def name_length(value):
#     if len(value) <= 2:
#         raise serializers.ValidationError("Name is too short")
#     else:
#         return value
    

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get("name" , instance.name)
#         instance.description = validated_data.get("description" , instance.description)
#         instance.active = validated_data.get("active" , instance.active)
#         instance.save()
#         return instance

    
#     def validate(self, data):
#         if data["name"] == data["description"]:
#             raise serializers.ValidationError("Title and description should be different")
       
#         return data

    # def validate_name(self,value):
    #     if len(value) <= 2:
    #         raise serializers.ValidationError("Name is too short")
    #     else:
    #         return value




class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = serializers.StringRelatedField(many=True, read_only = True)
    class Meta:
        model = StreamPlatform
        fields = "__all__"



