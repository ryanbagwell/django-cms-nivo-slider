from distutils.core import setup

setup(
    name='Django CMS NivoSlider',
    version='0.1.0',
    author='Ryan Bagwell',
    author_email='ryan@ryanbagwell.com',
    packages=['nivoslider',],
    url='https://github.com/ryanbagwell/django-cms-nivo-slider',
    license='LICENSE.txt',
    description='A Django CMS carousel version of Nivo Slider',
    long_description=open('README.txt').read(),
    install_requires=[
        "Django >= 1.4",
        "django-filer >= 0.9.3",
    ],
)