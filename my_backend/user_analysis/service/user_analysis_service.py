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