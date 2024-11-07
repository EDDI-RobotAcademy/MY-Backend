from abc import ABC, abstractmethod

class UserAnalysisService(ABC):
    @abstractmethod
    def createUserAnalysis(self, title, description):
        pass

    @abstractmethod
    def createUserAnalysisQuestion(self, user_analysis_id, question_text, user_analysis_type):
        pass

    @abstractmethod
    def createUserAnalysisCustomSelection(self, question_id, custom_text):
        pass

    @abstractmethod
    def saveAnswer(self, account_id, user_analysis_id, answers, guest_identifier=None):
        pass

    @abstractmethod
    def listAllRequest(self):
        pass

    @abstractmethod
    def listOwnRequest(self, account_id):
        pass

    @abstractmethod
    def readRequest(self, request_id):
        pass

    @abstractmethod
    def listAnswer(self, user_analysis_id):
        pass

    @abstractmethod
    def listQuestions(self, user_analysis_id):
        pass

    @abstractmethod
    def listSelections(self, question_id):
        pass

    @abstractmethod
    def listUserAnalysis(self):
        pass

    @abstractmethod
    def getAnswer(self, request_id):
        pass