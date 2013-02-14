from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.conf import settings
from filer.models.imagemodels import Image as FilerImage
from .models import *

class SliderPlugin(CMSPluginBase):
    name = "Sliding Images"
    render_template = "slider.html"
    change_form_template = "slider_change_form.html"
    model = SliderOptions
    module = "Carousel"
    filer_folder_name = getattr(settings,'SLIDER_FOLDER_NAME','Home Page Images')
    admin_preview = False
    
    def render(self, context, instance, placeholder):
        self.cms_plugin_instance = instance
        context['options'] = SliderOptions.objects.all()[0]
        context['images'] = self.get_selected_images()
        return context
        

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
          
        context.update({
            'preview': False,
            'is_popup': False,
            'plugin': self.cms_plugin_instance,
            'CMS_MEDIA_URL': settings.CMS_MEDIA_URL,
            'available_images':FilerImage.objects.filter(folder__name=self.filer_folder_name),
            'selected_images':self.get_selected_images()
        })
    
        
        return super(CMSPluginBase, self).render_change_form(request, context, add, change, form_url, obj)
        
    def get_selected_images(self,):
        
        selected_images = []
        
        try:
            options =  SliderOptions.objects.filter(cmsplugin_ptr=self.cms_plugin_instance.id)[0]
            for id in options.images.split(','):
                selected_images.append(FilerImage.objects.filter(id=id)[0])
        except:
            selected_images = []
    
        return selected_images

plugin_pool.register_plugin(SliderPlugin)    
     