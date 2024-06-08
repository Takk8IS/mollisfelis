# setup.py

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='MollisFelis',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'tensorflow',
        'scikit-learn'
    ],
    description='Biblioteca Python para animações suaves e fluidas, otimizada para uso moderno com suporte a inteligência artificial.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='David C Cavalcantwe',
    author_email='say@takk.ag',
    url='https://github.com/takk8is/mollisfelis',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Multimedia :: Graphics :: Animation',
        'Intended Audience :: Developers',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'mollisfelis=mollisfelis.cli:main',
        ],
    },
    keywords='animation, graphics, AI, machine learning',
    project_urls={
        'Documentation': 'https://takk.ag/mollisfelis.readthedocs.io/',
        'Source': 'https://github.com/takk8is/mollisfelis',
        'Tracker': 'https://github.com/takk8is/mollisfelis/issues',
    },
)
