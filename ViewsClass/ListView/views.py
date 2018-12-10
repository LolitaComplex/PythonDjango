from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from .models import Article
from django.db import transaction
# Create your views here.

@transaction.atomic
def createData(request):
    articles = []
    for x in range(200):
        articles.append(Article(title = "标题 %d" % (x + 1), content = "这是正文内容！！ %d" % (x + 1)))

    Article.objects.bulk_create(articles)

    return HttpResponse("添加成功")


class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"
    context_object_name = "articles"

    paginate_by = 15
    page_kwarg = "page"
    ordering = "create_time"

    showPageNum = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["other"] = "这是扩展的额外内容"

        paginator = context.get("paginator")
        print("总共 %d 条数据" % (paginator.count))
        print("总共 %d 页" % (paginator.num_pages))
        print("页面区间 %s " % (paginator.page_range))

        page = context.get("page_obj")
        print("是否还有下一页 %s " % (page.has_next()))
        print("是否还有上一页 %s " % (page.has_previous()))
        # print("下一页页码: %d" % (page.next_page_number()))
        # print("上一页页码: %d" % (page.previous_page_number())) 
        print("当前页: %d" % (page.number))
        print("第一条数据索引值：%d " % (page.start_index()))
        print("最后一条数据索引值: %d " % (page.end_index()))

        if (paginator.num_pages - page.number >= self.showPageNum):
            self.__initCurrentNum(context, page.number)
        else :
            self.__initCurrentNum(context, paginator.num_pages - self.showPageNum)
        return context

    def __initCurrentNum(self, context, currentNum):
        context["showCurrentNum"] = range(currentNum, currentNum + self.showPageNum + 1)

    def get_queryset(self):
        # Article.object.filter()
        return super().get_queryset()

