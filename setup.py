from setuptools import setup, find_packages

setup(
    name='site_eye',  
    version='0.1',  
    packages=find_packages(), 
    entry_points={
        'console_scripts': [
            'site_eye=main:main',  
        ],
    },
    install_requires=[
        'opencv-python',  
        'pyfiglet',       
        'colorama',       
        'yagmail',        
        'selenium',       
        'Pillow',         
    ],
    author='اسمك',
    author_email='بريدك الإلكتروني',
    description='Site Eye is a tool for monitoring changes in website content. It captures screenshots of web pages, compares them to detect changes, and sends email notifications when changes are found. This tool provides continuous and effective monitoring of websites with ease and without constant manual intervention.',
    url='https://github.com/everythingBlackkk/SiteEye',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  
)
