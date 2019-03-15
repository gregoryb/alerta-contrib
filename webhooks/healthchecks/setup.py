from setuptools import setup, find_packages

version = '1.0.0'

setup(
    name="alerta-healthchecks",
    version=version,
    description='Alerta Webhook for Healthchecks.io',
    url='https://github.com/alerta/alerta-contrib',
    license='MIT',
    author='Grégory BITTAN',
    author_email='gregory.bittan@gmail.com',
    packages=find_packages(),
    py_modules=['alerta_healthchecks'],
    install_requires=[],
    include_package_data=True,
    zip_safe=True,
    entry_points={
        'alerta.webhooks': [
            'healthchecks = alerta_healthchecks:HealthchecksWebhook'
        ]
    }
)