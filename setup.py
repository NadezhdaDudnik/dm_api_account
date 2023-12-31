from setuptools import setup, find_packages

REQUIRES = [
    'requests',
    'allure-pytest',
    'pydantic'
]
setup(
    name='dm_api_account',
    version='0.0.2',
    packages=find_packages(),
    url='https://github.com/NadezhdaDudnik/dm_api_account.git',
    license='MIT',
    author='Nadezhda Dudnik',
    author_email='-',
    install_requires=REQUIRES,
    description='dm_api_account library with apis and models'
)
