from __future__ import print_function

try:
    from setuptools import setup
except ImportError:
    import sys
    print("Please install the `setuptools` package in order to install this library", file=sys.stderr)
    raise

setup(
    name='mqttrpc',
    version='1.0',
    author='Max',
    author_email='litnimaxster@gmail.com',
    packages=('mqttrpc',),
    license='BSD',
    keywords='mqtt rpc',
    url='http://github.com/litnimax/python-mqttrpc',
    description='''A RPC interface over MQTT''',
    install_requires=['tinyrpc', 'hbmqtt', 'aiohttp', 'asyncio'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    scripts=['mqttrpc/http_bridge.py'],
)
