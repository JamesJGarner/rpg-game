[1mdiff --git a/game/apps/userprofiles/urls.py b/game/apps/userprofiles/urls.py[m
[1mindex 1453d52..9689c24 100644[m
[1m--- a/game/apps/userprofiles/urls.py[m
[1m+++ b/game/apps/userprofiles/urls.py[m
[36m@@ -3,6 +3,6 @@[m [mfrom .views import UserProfilePage, chart[m
 [m
 urlpatterns = [[m
     url(r'^user/(?P<pk>\d+)/$', UserProfilePage.as_view(), name="profile_page"),[m
[31m-    url(r'^character/$', chart, name="profile_page"),[m
[32m+[m[32m    url(r'^image/(?P<pk>\d+)/$', CharacterImage.as_view(), name="CharacterImage"),[m
     [m
 ][m
[1mdiff --git a/game/apps/userprofiles/views.py b/game/apps/userprofiles/views.py[m
[1mindex 42d11ae..98a66f9 100644[m
[1m--- a/game/apps/userprofiles/views.py[m
[1m+++ b/game/apps/userprofiles/views.py[m
[36m@@ -1,4 +1,4 @@[m
[31m-from django.views.generic import UpdateView[m
[32m+[m[32mfrom django.views.generic import UpdateView, DetailView[m
 from django.views.generic.edit import ModelFormMixin[m
 from .forms import UserProfileForm[m
 from .models import UserProfile[m
[36m@@ -53,23 +53,30 @@[m [mclass UserProfilePage(UpdateView):[m
         return context[m
 [m
 [m
[31m-def chart(request):[m
[31m-    media = "game/media/items/"[m
[32m+[m[32mclass CharacterImage(DetailView):[m
 [m
[31m-    background = Image.open("game/static/img/character-type/wizard.png")[m
[31m-    background = ImageOps.expand(background,border=80)[m
[32m+[m[32m    def get(self, request, *args, **kwargs):[m
[32m+[m[32m        self.object = self.get_object()[m
[32m+[m[32m        context = self.get_context_data(object=self.object)[m
[32m+[m[32m        return self.render_to_response(context)[m
 [m
 [m
[31m-    hat = Image.open(media + "hat-1.png")[m
[31m-    background.paste(hat, (200, 27), hat)[m
[32m+[m[32m        media = "game/media/items/"[m
 [m
[31m-    sword = Image.open(media + "sword-mounted_l9Rz3r8.png")[m
[31m-    background.paste(sword, (55, 27), sword)[m
[32m+[m[32m        background = Image.open("game/static/img/character-type/wizard.png")[m
[32m+[m[32m        background = ImageOps.expand(background,border=80)[m
 [m
 [m
[31m-    response = HttpResponse(content_type="image/png")[m
[31m-    background.save(response, "PNG")[m
[32m+[m[32m        hat = Image.open(media + "hat-1.png")[m
[32m+[m[32m        background.paste(hat, (200, 27), hat)[m
 [m
[32m+[m[32m        sword = Image.open(media + "sword-mounted_l9Rz3r8.png")[m
[32m+[m[32m        background.paste(sword, (55, 27), sword)[m
 [m
[31m-    return response[m
[32m+[m
[32m+[m[32m        response = HttpResponse(content_type="image/png")[m
[32m+[m[32m        background.save(response, "PNG")[m
[32m+[m
[32m+[m
[32m+[m[32m        return response[m
 [m
