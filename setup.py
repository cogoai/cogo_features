import setuptools 

install_requires = [
    "tensorflow==1.12.2",
    "rasa_nlu==0.14.3",
    "tensorflow-hub==0.2.0",
]

setuptools.setup(
    name='cogo_features',
    install_requires=install_requires,
    packages=setuptools.find_packages(),
    version='0.0.1',
    description='A library of featurizing natural english',
    author='COGOAI',
    author_email='johnny@agentcogo.com',
    url='https://github.com/cogoai/cogo_features',
    download_url='https://github.com/cogoai/cogo_features/0.1',
    keywords=['cogoai', 'features'],
)
