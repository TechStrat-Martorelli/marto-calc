import setuptools

setuptools.setup(
    name="streamlit-authenticator",
    version="0.2.3",
    author="Marcelo Mesquita",
    author_email="marcelo.mesquita@techstrategy.com.br",
    description="description",
    url="https://github.com/mkhorasani/Streamlit-Authenticator",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[ "Programming Language :: Python :: 3" ],
    keywords=['Python', 'Streamlit', 'Authentication', 'Components'],
    python_requires=">=3.6",
    install_requires=[
        "PyJWT >=2.3.0",
        "bcrypt >= 3.1.7",
        "PyYAML >= 5.3.1",
        "streamlit >= 1.18.0",
        "extra-streamlit-components >= 0.1.60"
    ],
)