from setuptools import setup, find_packages

setup(
    name='botclassifier',
    version='0.1.0',
    description='A machine learning package to classify VK users as bots or real users',
    author='Simran',
    author_email='drsimran69@gmail.com',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
        'xgboost',
        'matplotlib',
        'seaborn',
        'flask',        # If you're using a web app
        # 'fastapi',    # Alternative to Flask
        # 'uvicorn',    # If using FastAPI
        'joblib'
    ],
    entry_points={
        'console_scripts': [
            'train-bot-model=botclassifier.train:main',
            'run-bot-app=botclassifier.app:main'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
