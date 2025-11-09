from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Comment
from .serializers import CommentSerializer, CommentCreateSerializer


@swagger_auto_schema(
    method='get',
    operation_summary="댓글 목록 조회",
    operation_description="""
    등록된 모든 댓글을 조회합니다.
    
    **응답 데이터:**
    - **success** (bool): 성공 여부
    - **message** (string): 응답 메시지
    - **data** (object)
        - **count** (int): 전체 댓글 수
        - **comments** (array): 댓글 목록
            - **id** (int): 댓글 ID
            - **content** (string): 댓글 내용
            - **created_at** (string): 작성일시 (YYYY-MM-DD HH:MM:SS)
    """,
    responses={
        200: openapi.Response(
            description="댓글 목록 조회 성공",
            examples={
                "application/json": {
                    "success": True,
                    "message": "댓글 목록 조회 성공",
                    "data": {
                        "count": 1,
                        "comments": [
                            {
                                "id": 1,
                                "content": "첫 번째 댓글입니다.",
                                "created_at": "2025-11-08 10:00:00"
                            }
                        ]
                    }
                }
            }
        ),
        500: openapi.Response(description="서버 내부 오류"),
    }
)
@api_view(['GET'])
def comment_list(request):
    """댓글 목록 조회"""
    try:
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        
        return Response({
            'success': True,
            'message': '댓글 목록 조회 성공',
            'data': {
                'count': comments.count(),
                'comments': serializer.data
            }
        }, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response({
            'success': False,
            'message': '서버 오류가 발생했습니다.',
            'error': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@swagger_auto_schema(
    method='post',
    operation_summary="댓글 작성",
    operation_description="""
    새로운 댓글을 작성합니다.
    
    **요청 바디:**
    - **content** (string, 필수): 댓글 내용 (1~500자)
    
    **유효성 검사:**
    - 댓글 내용: 1자 이상 500자 이하
    
    **응답 데이터:**
    - **success** (bool): 성공 여부
    - **message** (string): 응답 메시지
    - **data** (object)
        - **id** (int): 생성된 댓글 ID
        - **content** (string): 댓글 내용
        - **created_at** (string): 작성일시 (YYYY-MM-DD HH:MM:SS)
    """,
    request_body=CommentCreateSerializer,
    responses={
        201: openapi.Response(
            description="댓글 작성 성공",
            examples={
                "application/json": {
                    "success": True,
                    "message": "댓글 작성 성공",
                    "data": {
                        "id": 3,
                        "content": "새로운 댓글입니다.",
                        "created_at": "2025-11-08 11:00:00"
                    }
                }
            }
        ),
        400: openapi.Response(
            description="잘못된 요청",
            examples={
                "application/json": {
                    "success": False,
                    "message": "잘못된 요청",
                    "errors": {
                        "content": ["댓글 내용은 필수입니다."]
                    }
                }
            }
        ),
        500: openapi.Response(description="서버 내부 오류"),
    }
)
@api_view(['POST'])
def comment_create(request):
    """댓글 작성"""
    serializer = CommentCreateSerializer(data=request.data)
    
    if serializer.is_valid():
        try:
            comment = serializer.save()
            response_serializer = CommentSerializer(comment)
            
            return Response({
                'success': True,
                'message': '댓글 작성 성공',
                'data': response_serializer.data
            }, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({
                'success': False,
                'message': '댓글 저장 중 오류가 발생했습니다.',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    return Response({
        'success': False,
        'message': '잘못된 요청',
        'errors': serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)