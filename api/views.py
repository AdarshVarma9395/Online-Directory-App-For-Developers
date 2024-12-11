from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import ProjectSerializers
from projects.models import Project, Review, Tag


@api_view(["GET"])
def getRoutes(request):
    routes = [
        {'GET':'/api/projects'},
        {'GET':'/api/projects/id'},
        {'POST':'/api/projects/id/vote'},

        {'POST':'/api/users/token'},
        {'POST':'/api/users/tokenrefresh'},
    ]
    return Response(routes)


@api_view(['GET'])
def getProjects(request):
    #Retrieve a list of all Project objects.
    projects = Project.objects.all()  # Query all projects
    serializer = ProjectSerializers(projects, many=True)  # Serialize the queryset
    return Response(serializer.data) 


@api_view(['GET'])
def getProject(request, pk):
    # Retrieve a specific Project object by its ID (primary key).
    try:
        project = Project.objects.get(pk=pk)  # Retrieve the object
    except Project.DoesNotExist:
        return Response({'error': 'Project not found'})
    
    serializer = ProjectSerializers(project)  # Serialize the object
    return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def projectVote(request, pk):
    project = Project.objects.get(id=pk)
    user = request.user.profile
    data = request.data

    review, created = Review.objects.get_or_create(
        owner = user,
        project = project,
    )

    review.value = data['value']
    review.save()

    project.getVoteCount
    
    serializer = ProjectSerializers(project, many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
def removeTag(request):
    tagId = request.data['tag']
    projectId = request.data['project']

    project = Project.objects.get(id=projectId)
    tag = Tag.objects.get(id=tagId)

    project.tags.remove(tag)

    return Response('Tag was deleted!')
