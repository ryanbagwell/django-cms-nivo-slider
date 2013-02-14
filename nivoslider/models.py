from django.db import models
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField
from filer.fields.folder import FilerFolderField
from cms.models.pluginmodel import CMSPlugin

class Slider(models.Model):
    image = FilerImageField(null=True, blank=True)
    url = models.URLField(
        verify_exists=False, max_length=200, null=True, blank=True)
    
class SliderOptions(CMSPlugin):
    
    EFFECTS = (
        ('random','random'),        
        ('sliceDown','sliceDown'),
        ('sliceDownLeft','sliceDownLeft'),
        ('sliceUp','sliceUp'),
        ('sliceUpLeft','sliceUpLeft'),
        ('sliceUpDown','sliceUpDown'),
        ('sliceUpDownLeft','sliceUpDownLeft'),
        ('fold','fold'),
        ('fade','fade'),
        ('random','random'),
        ('slideInRight','slideInRight'),
        ('slideInLeft','slideInLeft'),
        ('boxRandom','boxRandom'),
        ('boxRain','boxRain'),
        ('boxRainReverse','boxRainReverse'),
        ('boxRainGrow','boxRainGrow'),
        ('boxRainGrowReverse','boxRainGrowReverse'),
    )

    base_folder = FilerFolderField(blank=True, null=True,
        help_text="The folder that contains the available images")
    images = models.CharField(
        max_length=255, blank=True, null=True)
    effect = models.CharField(
        default="random", max_length=255, blank=True, null=True, choices=EFFECTS)
    animation_speed = models.CharField(
        default="500",max_length=255,blank=True,null=True,
        help_text="The animation speed in miliseconds")
    pause_time = models.CharField(
        max_length=255, blank=True, null=True, 
        help_text="The delay between animations")
    show_nav = models.BooleanField(
        default=True, help_text="Show the navigation icons")
    use_nav_thumbs = models.BooleanField(
        default=True, help_text="Use thumbnails as the navigation icons")
    random_start = models.BooleanField(
        default=False, help_text="Start on a random image")
    pause_on_hover = models.BooleanField(
        default=True, help_text="Pause on Hover")
    direction_nav = models.BooleanField(
        default=True, help_text="Show the direction nav (next & prev)")
