from distutils.core import setup

REQUIRES = [
    'requests',
    'allure'
]
setup(
    name='dm_api_account',
    version='0.0.1',
    packages=['dm_api_account'],
    url='https://github.com/NadezhdaDudnik/dm_api_account.git',
    license='MIT',
    author='Nadezhda Dudnik',
    author_email='-',
    install_requires=REQUIRES,
    description='dm_api_account with allure and logger'
)
