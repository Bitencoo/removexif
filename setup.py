from setuptools import setup, find_packages

setup(
    name='removexif',
    version='0.1.2',  
    description='Easily remove and add EXIF metadata to images',
    author='Tulio Bitencourt',
    author_email='tuliob.dev@gmail.com',
    license='MIT',
    url='https://github.com/Bitencoo',
    download_url='https://github.com/Bitencoo/removexif',
    packages=find_packages(),
    install_requires=[
        'Pillow',
    ],
    keywords = ['IMAGE', 'EXIF', 'METADATA', "REMOVE"],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',      
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.12'
    ],
)