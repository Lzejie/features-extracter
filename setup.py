# -*- coding: utf-8 -*-
# @Time    : 18/7/27 下午5:01
# @Author  : Edward
# @Site    :
# @File    : setup.py
# @Software: PyCharm Community Edition

from setuptools import setup, find_packages

setup(
    name="features-extracter",
    packages=find_packages(),
    version='0.1.0',
    description="text feature extracter",
    author="L_zejie",
    author_email='lzj_xuexi@163.com',
    url="https://github.com/Lzejie/features-extracter",
    license="MIT Licence",
    # download_url='https://github.com/username/reponame/archive/0.1.tar.gz',
    keywords=['feature', 'extracter', 'nlp'],
    classifiers=[],
    # entry_points={
    #     'console_scripts': [
    #         'command1 = advisorhelper.cmdline:execute'
    #         'command2 = adviserserver.create_algorithm:run',
    #         'command3 = adviserserver.run_algorithm:run'
    #     ]
    # },
    install_requires=[
        'sklearn',
        'gensim',
        'numpy',
        'jieba',
    ]
)