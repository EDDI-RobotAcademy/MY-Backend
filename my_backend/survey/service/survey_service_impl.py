from account.repository.account_repository_impl import AccountRepositoryImpl
from survey.repository.survey_answer_repository_impl import SurveyAnswerRepositoryImpl
from survey.repository.survey_question_repository_impl import SurveyQuestionRepositoryImpl
from survey.repository.survey_repository_impl import SurveyRepositoryImpl
from survey.repository.custom_selection_repository_impl import SurveySelectionRepositoryImpl
from survey.service.survey_service import SurveyService


class SurveyServiceImpl(SurveyService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__surveyRepository = SurveyRepositoryImpl.getInstance()
        cls.__instance.__accountRepository = AccountRepositoryImpl.getInstance()
        cls.__instance.__surveyQuestionRepository = SurveyQuestionRepositoryImpl.getInstance()
        cls.__instance.__surveySelectionRepository = SurveySelectionRepositoryImpl.getInstance()
        cls.__instance.__surveyAnswerRepository = SurveyAnswerRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def createSurvey(self, title, description):
        try:
            return self.__surveyRepository.create(title, description)

        except Exception as e:
            print('Error creating order:', e)
            raise e

    def createSurveyQuestion(self, survey_id, question_text, survey_type):
        survey = self.__surveyRepository.findById(survey_id)
        if survey is None:
            raise ValueError("Survey not found")

        return self.__surveyQuestionRepository.create(survey, question_text, survey_type)

    def createSurveySelection(self, question_id, selection_text):
        try:
            question = self.__surveyQuestionRepository.findById(question_id)
            if question is None:
                raise ValueError("Survey Question not found")

            return self.__surveySelectionRepository.createCustomSelection(question, selection_text)

        except ValueError as e:
            print(f"Error: {str(e)}")
            raise e

        except Exception as e:
            print(f"Unexpected error while creating selection: {str(e)}")
            raise e

    def saveAnswer(self, answers, account_id):
        try:
            for answer in answers:

                question_id = answer.get('question_id')
                question = self.__surveyQuestionRepository.findById(question_id)
                survey_id = question.survey_id
                answer_data = answer.get('answer_data')


                self.__surveyAnswerRepository.saveAnswer(survey_id, question_id, answer_data, account_id)

        except Exception as e:
            print('답변 저장중 오류 발생: ', {e})



