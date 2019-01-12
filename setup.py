from setuptools import setup

version = '1.0.0'

requirements = [
    'requests==2.20.0',
    'flask==1.0.2',
    'beautifulsoup4==4.6.3'
]

dev_requirements = [
    'pytest'
]

setup(name='score_alerts',
      version=version,
      description="Lists scores auto-magically",
      author='Marko Pavlovic',
      author_email='markopavlovic922@gmail.com',
      url='Link coming soon...',
      install_requires=requirements,
      extras_require={'dev': dev_requirements},
      packages=['score_alerts', 'score_alerts.scrapers', 'score_alerts.server.api'],
      )