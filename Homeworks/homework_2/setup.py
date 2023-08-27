from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='0.0.1',
    description='The script that cleans a specified folder',
    author='Gregory Ostapenko',
    author_email='goalliance@gmail.com',
    url='https://github.com/InSmartGroup/GoIT_Python_Course/tree/master/Homeworks/homework_2',
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    packages=find_namespace_packages(),
    include_package_data=True,
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']}
)
