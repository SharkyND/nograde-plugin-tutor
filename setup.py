from setuptools import setup, find_packages  
  
setup(  
    name="tutor-nogrades",  
    version="0.1.0",  
    url="https://github.com/SharkyND/nograde-plugin-tutor",  
    author="Sharjy",  
    author_email="your.email@example.com",  
    description="A Tutor plugin to disable grading",  
    packages=find_packages(),  
    include_package_data=True,  
    install_requires=["tutor"],  
    entry_points={"tutor.plugin.v0": ["nogrades = nogrades"]},  
    classifiers=[  
        "Development Status :: 3 - Alpha",  
        "Intended Audience :: Developers",  
        "License :: OSI Approved :: GNU Affero General Public License v3",  
        "Programming Language :: Python :: 3",  
    ],  
)  
