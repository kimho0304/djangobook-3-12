from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question, Category


def index(request, category_name='전체게시판'):
    """
    pybo 목록 출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지

    # 조회
    category_list = Category.objects.all()
    category = get_object_or_404(Category, name=category_name)

    if category_name == "전체게시판":
        question_list = Question.objects.all()
    else:
        question_list = Question.objects.filter(category=category)

    question_list.order_by('-create_date')

    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'category_list': category_list, 'category': category}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id, category_name='전체게시판'):
    """
    pybo 내용 출력
    """
    category_list = Category.objects.all()
    category = get_object_or_404(Category, name=category_name)

    question = get_object_or_404(Question, pk=question_id)
    question.visited_number += 1
    question.save()
    context = {'question': question, 'category_list': category_list, 'category': category}
    return render(request, 'pybo/question_detail.html', context)
