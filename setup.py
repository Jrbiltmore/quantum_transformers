from setuptools import setup, find_packages

setup(
    name='QuantumTransformers',
    version='0.1.0',
    description='A package for quantum, classical, and hybrid algorithms.',
    author='Jacob Thomas Messer Redmond, ChatGPT-4o',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pennylane',
        'qiskit',
        'cirq',
        'numpy',
        'scipy',
        'pytest',
        'matplotlib',
        'pyyaml'
    ],
    entry_points={
        'console_scripts': [
            'quantumtransformers=src.main:main',
        ],
    },
)
# END