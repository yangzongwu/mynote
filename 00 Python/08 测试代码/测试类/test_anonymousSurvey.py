from unittest import TestCase
from survey import AnonymousSurvey

class TestAnonymousSurvey(TestCase):
    """测试单个答案会被妥善地存储"""
    def test_store_single_response(self):
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)

    def test_store_three_responses(self):
        """测试三个答案会被妥善地存储"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, my_survey.responses)

'''
在前面的test_survey.py中，我们在每个测试方法中都创建了一个AnonymousSurvey 实例，并在每个方法中都创建了答案。
unittest.TestCase 类包含方法setUp() ，让我 们只需创建这些对象一次，并在每个测试方法中使用它们

测试自己编写的类时，方法setUp() 让测试方法编写起来更容易：
可在setUp() 方法中创建一系列实例并设置它们的属性，再在测试方法中直接使用这些实例。
相比于在每个 测试方法中都创建实例并设置其属性，这要容易得多。

'''
class TestAnonymousSurvey2(TestCase):
    """针对AnonymousSurvey类的测试"""
    def setUp(self):
        """ 创建一个调查对象和一组答案，供使用的测试方法使用 """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """测试单个答案会被妥善地存储"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """测试三个答案会被妥善地存储"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)