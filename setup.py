from setuptools import setup, find_packages

setup(
    name='unicellgpt',
    version='0.3',
    description='A package for unicell firm to use GPT models',
    author='Shiyao Wang',
    author_email='galadata@sina.com',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'torch',
        'transformers',
        'openai'
    ]
)
