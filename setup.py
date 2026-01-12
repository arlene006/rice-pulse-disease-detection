from setuptools import setup, find_packages

# Read requirements
with open("requirements.txt", "r") as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name='crop_disease_detector',
    
    author='Arlene',
    
    author_email='arleneregi006@gmail.com',
    
    version='1.0.0',
    
    description='AI-Powered Agricultural Diagnostic Tool for detecting diseases in rice and pulse crops using deep learning',
    
    long_description_content_type="text/markdown",
    
    url='https://github.com/arlene006/rice-pulse-disease-detection',
    
    install_requires=requirements,
    
    keywords='streamlit, machine learning, agriculture, disease detection, deep learning, CNN, PyTorch',
    
    packages=find_packages(include=['crop_disease_detector', 'crop_disease_detector.*']),
    
    include_package_data=True,
    
    python_requires='>=3.11',
    
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.11',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Image Recognition',
    ],
    
    # Entry points for running the application
    entry_points={
        'console_scripts': [
            'crop-disease-detector=crop_disease_detector.app:main',
        ],
    },
)