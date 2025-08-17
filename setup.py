from setuptools import setup, find_packages

setup(
    name='insurance_package',
    version='0.1.0',
    author='Shaneen Dickinson',
    author_email='Shaneen.dickinson@gmail.com',
    description='A package for managing insurance policies',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Neen2025/Insurance_Project.git',
    packages=find_packages(),
    install_requires=open('requirements.txt').read().splitlines(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)