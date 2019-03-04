from django.views.generic import ListView


class MLIndexLV(ListView):
    template_name = 'ml/ml_list.html'

    def get_queryset(self):
        pass
