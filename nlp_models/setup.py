from setuptools import setup, find_packages

setup(
    name='NLP_examples',
    version='0.0.1',
    pacakges=find_packages(include=['nlp_models', 'nlp_model.*']),
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
        'matplotlib',
        'plotly',
        'seaborn',
        'torch',
        'torchvision',
        'transformers',
        'jupyterlab',
        'pytest',
        'ipywidgets',
        
    ]
)