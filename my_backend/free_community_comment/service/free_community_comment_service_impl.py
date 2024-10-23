from free_community_comment.repository.free_community_comment_repository_impl import FreeCommunityCommentRepositoryImpl
from free_community_comment.service.free_community_comment_service import FreeCommunityCommentService


class FreeCommunityCommentServiceImpl(FreeCommunityCommentService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__freeCommunityCommentRepository = FreeCommunityCommentRepositoryImpl.getInstance()
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def listComments(self, freeCommmunityId):
        return self.__freeCommunityCommentRepository.list(freeCommmunityId)

    def listReplies(self, parentId):
        return self.__freeCommunityCommentRepository.list_replies(parentId)

    def createComment(self, content, freeCommmunityId, accountId, parentId):
        return self.__freeCommunityCommentRepository.create(content, freeCommmunityId, accountId, parentId)

    def readComment(self, commentId):
        return self.__freeCommunityCommentRepository.findByCommentId(commentId)

    def removeComment(self, commentId):
        return self.__freeCommunityCommentRepository.deleteByCommentId(commentId)

    def updateComment(self, commentId, commentData):
        comment = self.__freeCommunityCommentRepository.findByCommentId(commentId)
        return self.__freeCommunityCommentRepository.update(comment, commentData)