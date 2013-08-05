from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.conf import settings
from filer.models.imagemodels import Image as FilerImage
from .models import *

class SliderPlugin(CMSPluginBase):
    name = "Nivo Slider"
    render_template = "nivoslider/nivoslider.html"
    change_form_template = "nivoslider/slider_change_form.html"
    model = SliderOptions
    module = "Carousel"
    admin_preview = True

    def render(self, context, instance, placeholder):
        context.update({
            'images':  self.get_selected_images(instance),
            'show_nav': instance.show_nav,
            'pause_on_hover': instance.pause_on_hover,
            'use_nav_thumbs': instance.use_nav_thumbs,
            'animation_speed': instance.animation_speed,
            'show_direction_nav': instance.direction_nav,
            'random_start': instance.random_start,
            'effect': instance.effect,
            'pause_time': instance.pause_time,
        })

        return context

    def render_change_form(self, request, context,
        add=False, change=False, form_url='', obj=None):

        context.update({
            'available_images': self.get_available_images(obj),
            'selected_images': self.get_selected_images(obj),
        })

        return super(SliderPlugin, self).render_change_form(request, context,
            add, change, form_url, obj)

    def get_selected_images(self, obj):

        try:
            return FilerImage.objects.filter(
                id__in=obj.images.split(','))
        except:
            return []

    def get_available_images(self, obj):

        try:
            return obj.base_folder.files
        except:
            return []

plugin_pool.register_plugin(SliderPlugin)