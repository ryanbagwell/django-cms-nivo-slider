from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.conf import settings
from filer.models.imagemodels import Image as FilerImage
from .models import *

class SliderPlugin(CMSPluginBase):
    name = "Nivo Slider"
    render_template = "slider.html"
    change_form_template = "slider_change_form.html"
    model = SliderOptions
    module = "Carousel"
    admin_preview = True
    
    def render(self, context, instance, placeholder):
        self.cms_plugin_instance = instance
        context.update({
            'options': SliderOptions.objects.all()[0],
            'images':  self.get_selected_images(),
            })
        return context

    def render_change_form(self, request, context,
        add=False, change=False, form_url='', obj=None):
        
        context.update({
            'plugin': obj,
            # 'preview': False,
            #           'is_popup': False,
            #'plugin': self.cms_plugin_instance,
            #'CMS_MEDIA_URL': settings.CMS_MEDIA_URL,
            'available_images': self.get_available_images(obj),
            'selected_images': self.get_selected_images(obj),
        })
        
        return super(CMSPluginBase, self).render_change_form(request, context,
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