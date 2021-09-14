from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


class GarpixPaginator(Paginator):

    def __init__(self, object_list, per_page, orphans=0,
                 allow_empty_first_page=True, neighbors=4):
        super().__init__(object_list, per_page, orphans, allow_empty_first_page)
        self.current_page = 1
        self.neighbors = int(neighbors)

    def get_page(self, number):
        try:
            number = self.validate_number(number)
        except PageNotAnInteger:
            number = 1
        except EmptyPage:
            number = self.num_pages
        self.current_page = number
        return self.page(number)

    @property
    def page_range_beauty(self):
        left_page = self.current_page - self.neighbors
        if left_page < 1:
            left_page = 1
        right_page = self.current_page + self.neighbors
        if right_page > self.num_pages:
            right_page = self.num_pages
        page_range_list = list(map(lambda x: (x, x), range(left_page, right_page + 1)))
        if left_page > 2:
            page_range_list.insert(0, (left_page - 1, '...'))
        if left_page != 1:
            page_range_list.insert(0, (1, 1))
        if right_page < self.num_pages - 1:
            page_range_list.append((right_page + 1, '...'))
        if right_page != self.num_pages:
            page_range_list.append((self.num_pages, self.num_pages))
        return page_range_list
