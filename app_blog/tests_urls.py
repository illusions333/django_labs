from django.test import TestCase
from django.urls import reverse, resolve

from .views import HomePageView, ArticleList, ArticleCategoryList, ArticleDetail


class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEqual(view.func.view_class, HomePageView)

    def test_category_view_status_code(self):
        url = reverse('articles-category-list', args = ('name',))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_sport_url_resolves_sport_view(self):
        view = resolve('/articles/category/sport/')
        self.assertEqual(view.func.view_class, ArticleCategoryList)
    def test_osvita_url_resolves_osvita_view(self):
        view = resolve('/articles/category/osvita/')
        self.assertEqual(view.func.view_class, ArticleCategoryList)
    def test_politika_url_resolves_politika_view(self):
        view = resolve('/articles/category/politika/')
        self.assertEqual(view.func.view_class, ArticleCategoryList)
    def test_tehnologiyi_url_resolves_tehnologiyi_view(self):
        view = resolve('/articles/category/tehnologiyi/')
        self.assertEqual(view.func.view_class, ArticleCategoryList)

    def test_articles_view_status_code(self):
        url = reverse('articles-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_articles_url_resolves_articles_view(self):
        view = resolve('/articles/')
        self.assertEqual(view.func.view_class, ArticleList)

    def test_news1_url_resolves_news_view(self):
        view = resolve('/articles/2025/11/03/lunin-prokomentuvav-vyluchennia-v-el-classico/')
        self.assertEqual(view.func.view_class, ArticleDetail)
    def test_news2_url_resolves_news_view(self):
        view = resolve('/articles/2025/11/03/trump-zayavyv-chy-rozglyadaye-postavky-tomahawk/')
        self.assertEqual(view.func.view_class, ArticleDetail)
    def test_news3_url_resolves_news_view(self):
        view = resolve('/articles/2025/11/03/nimechchyna-peredala-ukraini-dodatkovi-patriot/')
        self.assertEqual(view.func.view_class, ArticleDetail)
    def test_news4_url_resolves_news_view(self):
        view = resolve('/articles/2025/11/03/vcheni-pidtverdyly-80-richnu-gipotezu/')
        self.assertEqual(view.func.view_class, ArticleDetail)
    def test_news5_url_resolves_news_view(self):
        view = resolve('/articles/2025/11/03/vcheni-znaishly-novu-formu-zhyttia/')
        self.assertEqual(view.func.view_class, ArticleDetail)
    def test_news6_url_resolves_news_view(self):
        view = resolve('/articles/2025/11/03/chomu-tehnika-mozhe-zgority-pid-chas-vidkluchen/')
        self.assertEqual(view.func.view_class, ArticleDetail)