from products.views import (
    ProductList,
)


class Index(ProductList):
    template_name = 'index.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['paginator'] = self.IterablePaginator(
            context['paginator']
        ).__next__
        return context

    @staticmethod
    def IterablePaginator(paginator):
        for page_num in paginator.page_range:
            yield paginator.get_page(page_num).object_list
