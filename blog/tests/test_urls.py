'''
UnitTest in Blog app
'''
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import (PostList, PopularList, AuthorPosts, PostDetail,
                        PostLike, PostCreate, PostUpdate, PostDelete)


class TestUrls(SimpleTestCase):
    '''
    Test all URLS
    '''

    def test_home_url_is_resolved(self):
        '''
        Test home url
        '''
        url = reverse('home')
        self.assertEqual(resolve(url).func.view_class, PostList)

    def test_popular_url_is_resolved(self):
        '''
        Test popular country url
        '''
        url = reverse('country_list')
        self.assertEqual(resolve(url).func.view_class, PopularList)

    def test_author_url_is_resolved(self):
        '''
        Test posts by author url
        '''
        url = reverse('author_list')
        self.assertEqual(resolve(url).func.view_class, AuthorPosts)

    def test_post_detail_url_is_resolved(self):
        '''
        Test detail post url
        '''
        url = reverse('post_detail', args=['UUID'])
        self.assertEqual(resolve(url).func.view_class, PostDetail)

    def test_likes_url_is_resolved(self):
        '''
        Test like/unlike url
        '''
        url = reverse('post_like', args=['uuid'])
        self.assertEqual(resolve(url).func.view_class, PostLike)

    def test_post_create_url_is_resolved(self):
        '''
        Test create new post url
        '''
        url = reverse('post_create')
        self.assertEqual(resolve(url).func.view_class, PostCreate)

    def test_post_update_url_is_resolved(self):
        '''
        Test edit/update post url
        '''
        url = reverse('post_update', args=['1'])
        self.assertEqual(resolve(url).func.view_class, PostUpdate)

    def test_post_delete_url_is_resolved(self):
        '''
        Test delete post url
        '''
        url = reverse('post_delete', args=['1'])
        self.assertEqual(resolve(url).func.view_class, PostDelete)

    def test_about_url_is_resolved(self):
        '''
        Test about page url
        '''
        url = reverse('about')
        self.assertEqual(resolve(url).route, 'about/')

    def test_contact_url_is_resolved(self):
        '''
        Test contact page url
        '''
        url = reverse('contact_us')
        self.assertEqual(resolve(url).route, 'contact_us/')
