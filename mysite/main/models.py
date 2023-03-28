from django.db import models

# Create your models here.


class HomeLogo(models.Model):

    logo = models.ImageField('Home logo', upload_to='images')


class HomeInfo(models.Model):

    name1 = models.CharField('Home info name1', max_length=50)
    name2 = models.CharField('Home info name2', max_length=50)
    button_name = models.CharField('Home button', max_length=50)

    def __str__(self):
        return self.name1


class HomeSlider(models.Model):

    name = models.CharField('Slider name', max_length=50)
    img = models.ImageField('Slider image', upload_to='images')
    verify_button = models.BooleanField('Slider verify button Show/Hide')
    verify_logo = models.ImageField('Slider verify logo', upload_to='images')
    link_1 = models.URLField('Slider link1', blank=True)
    link_2 = models.URLField('Slider link2', blank=True)
    link_3 = models.URLField('Slider link3', blank=True)
    link1_name = models.CharField('Slider link1 name', max_length=100, blank=True)
    link2_name = models.CharField('Slider link2 name', max_length=100, blank=True)
    link3_name = models.CharField('Slider link3 name', max_length=100, blank=True)
    proff1 = models.CharField('Proff1 name', max_length=50, blank=True)
    proff2 = models.CharField('Proff2 name', max_length=50, blank=True)

    def __str__(self):
        return self.name
    

class HomeFooterBg(models.Model):

    img = models.ImageField('HomeFooterBg', upload_to='images')


class LastEpisode(models.Model):

    after = models.ForeignKey(HomeSlider, on_delete=models.CASCADE, related_name='last_episode')
    name = models.CharField('Last_episode name', max_length=60)

    