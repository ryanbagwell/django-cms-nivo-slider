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
        
        self
        
        
        context.update({
            # 'preview': False,
            #           'is_popup': False,
            #'plugin': self.cms_plugin_instance,
            #'CMS_MEDIA_URL': settings.CMS_MEDIA_URL,
            'available_images': self.get_available_images(obj),
            'selected_images': self.get_selected_images(obj),
        })
        
        return super(CMSPluginBase, self).render_change_form(request, context,
            add=False, change=False, form_url='', obj=None)
    
        # return super(CMSPluginBase, self).render_change_form(
        #     request, context, add, change, form_url, obj)
        
    def get_selected_images(self, obj):
        
        selected_images = []
        
        #assert False, obj.__dict__
        
        
        try:
            options =  obj.objects.filter(
                cmsplugin_ptr=self.cms_plugin_instance.id)[0]
            for id in options.images.split(','):
                selected_images.append(
                    FilerImage.objects.filter(id=id)[0])
        except:
            selected_images = []
    
        return selected_images
        
    def get_available_images(self, obj):
        
        try:
            return obj.base_folder.files
        except:
            return []

plugin_pool.register_plugin(SliderPlugin)     