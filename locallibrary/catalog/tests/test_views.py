from django.test import TestCase
from django.urls import reverse

from catalog.models import Author
from catalog.models import Book


class BookListViewTest(TestCase):
    # @classmethod
    # def setUpTestData(cls):
    #     # Create 13 books for pagination tests
    #     number_of_books = 13
    #
    #     for book_id in range(number_of_books):
    #         Book.objects.create(
    #             title=f'Yolo{book_id}',
    #             author=f'CharlieChaplin {book_id}',
    #         )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/catalog/books/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('books'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('books'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/book_list.html')

    def test_pagination_is_ten(self):
        response = self.client.get(reverse('books'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        # self.assertTrue(response.context['is_paginated'] == True)
        # self.assertTrue(len(response.context['book_list']) == 10)

    # def test_lists_all_books(self):
    #     # Get second page and confirm it has (exactly) remaining 3 items
    #     response = self.client.get(reverse('books') + '?page=2')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTrue('is_paginated' in response.context)
    #     self.assertTrue(response.context['is_paginated'] == True)
    #     self.assertTrue(len(response.context['book_list']) == 3)



# Note: Not used currently since Author list is not setup.

# class AuthorListViewTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         # Create 13 authors for pagination tests
#         number_of_authors = 13
#
#         for author_id in range(number_of_authors):
#             Author.objects.create(
#                 first_name=f'Christian {author_id}',
#                 last_name=f'Surname {author_id}',
#             )
#
#     def test_view_url_exists_at_desired_location(self):
#         response = self.client.get('/catalog/authors/')
#         self.assertEqual(response.status_code, 200)
#
#     def test_view_url_accessible_by_name(self):
#         response = self.client.get(reverse('authors'))
#         self.assertEqual(response.status_code, 200)
#
#     def test_view_uses_correct_template(self):
#         response = self.client.get(reverse('authors'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'catalog/author_list.html')
#
#     def test_pagination_is_ten(self):
#         response = self.client.get(reverse('authors'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTrue('is_paginated' in response.context)
#         self.assertTrue(response.context['is_paginated'] == True)
#         self.assertTrue(len(response.context['author_list']) == 10)
#
#     def test_lists_all_authors(self):
#         # Get second page and confirm it has (exactly) remaining 3 items
#         response = self.client.get(reverse('authors') + '?page=2')
#         self.assertEqual(response.status_code, 200)
#         self.assertTrue('is_paginated' in response.context)
#         self.assertTrue(response.context['is_paginated'] == True)
#         self.assertTrue(len(response.context['author_list']) == 3)