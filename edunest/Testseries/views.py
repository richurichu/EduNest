from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.utils import timezone
from authentification.models import CustomUser


class TestseriesDetailAPI(APIView):
    print('reached testseries_______________________________________________')
    def get(self,request,testseries_id,format=None):
       
            
        # test_series = TestSeries.objects.prefetch_related('question_set__option_set').get(id=testseries_id)
        test_series = TestSeries.objects.get(id=testseries_id)
        print(test_series)
        
        questions = test_series.question_set.all()
        
        questions_dict = {}
        for question in questions:
            
            options = [{'id': option.id, 'text': option.text} for option in question.option_set.all()]
            questions_dict[question.id] = {
                'id': question.id,
                'text': question.text,
                'options': options
    }
        return Response(questions_dict)
    

        
class CalculateMarksAPIView(APIView):
    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        testseries_id = request.data.get('testseries_id')
        response_data = request.data.get('selectedOptions')
        total_marks = 0
        correct_count = 0
        unattempted_count = 0
        incorrect_count = 0

        user = CustomUser.objects.get(pk= user_id)
        testseries = TestSeries.objects.get(pk = testseries_id)

        testseries_attempt = TestAttempt.objects.create(
            user = user,
            testseries = testseries,
            created_on = timezone.now()
        )
        all_questions = Question.objects.filter(test_series=testseries)
        
        for question_id, selected_option_id in response_data.items():
            question = Question.objects.get(pk=question_id)
            selected_option = Option.objects.get(pk=selected_option_id)
            correct_option = Option.objects.get(question=question_id, is_correct = True)

            testAttempt_record  = QuizResponse.objects.create(
                testattempt = testseries_attempt,
                question = question,
                selected_option = selected_option,
                correct_option = correct_option
            )

            if selected_option.is_correct:

                total_marks += 1
                correct_count += 1
            else:
                total_marks -= 0.3
                incorrect_count += 1
            
        unattempted_questions = all_questions.exclude(id__in=response_data.keys())
        for unattempted_question in unattempted_questions:
            
            QuizResponse.objects.create(
                testattempt=testseries_attempt,
                question=unattempted_question,
                selected_option=None,
                correct_option=Option.objects.get(question=unattempted_question, is_correct=True)
            )
            unattempted_count += 1

        rounded_total_marks = round(total_marks, 3)
        return Response({'total_marks': rounded_total_marks , 'correct_count':correct_count , 'unattempted_count':unattempted_count ,'incorrect_count':incorrect_count ,'testseries_id':testseries_id})
        