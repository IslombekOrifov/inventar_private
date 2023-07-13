from accounts.models import CustomUser
from index.models import Category, Model


def context_datas(request):
    if not request.user.is_anonymous:
        if request.user.is_superuser:
            category_count = Category.objects.filter(group=request.user.groups.first()).count()
            model_count = Model.objects.filter(group=request.user.groups.first()).count()
            res_count = CustomUser.objects.filter(groups=request.user.groups.first()).count()
            return {
                'category_count': category_count,
                'model_count': model_count,
                'res_count': res_count
            }
        else:
            return {
                'category_count': 0,
                'model_count': 0,
                'res_count': 0
            }
    else:
        return {
            'category_count': 0,
            'model_count': 0,
            'res_count': 0
        }