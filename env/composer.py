#!/usr/bin/env python

"""Composer let's you remove unnecessary services from a Docker Compose file. It is built for larger stacks with many services,
and the fact the not every service is needed always.

Usage:
  composer.py compose [--with=SERVICES...] [--without=SERVICES...]
  composer.py (-h | --help)
  composer.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.

"""


import ruamel.yaml as yaml
import inquirer
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__, version='Composer 0.1')
    print arguments


with open("docker-compose.core.yml") as stream:
    try:
        parsedYaml = yaml.load(stream, yaml.RoundTripLoader)
    except yaml.YAMLError as exc:
        print(exc)

services = parsedYaml['services']


if arguments['--with'] and arguments['--without']:
    print "Only one of --with or --without can be present at once"
    exit(1)

if arguments['--with']:
    if len(arguments['--with']) == 0:
        print "Provide at least one service"
        exit(1)
    else:
        withServices = arguments['--with'][0].split(',')
        notNeededServices = list(set(services.keys()) - set(withServices))
        for serviceNotNeeded in notNeededServices:
            del services[serviceNotNeeded]
elif arguments['--without']:
    if len(arguments['--without']) == 0:
        print "Provide at least one service"
        exit(1)
    else:
        for serviceNotNeeded in arguments['--without'][0].split(','):
            del services[serviceNotNeeded]
else:
    questions = [
        inquirer.Checkbox('services',
                          message="What services do you need?",
                          choices=services.keys(),
                          default=services.keys()
                          ),
    ]
    answers = inquirer.prompt(questions)
    notNeededServices = list(set(services.keys()) - set(answers['services']))

    for serviceNotNeeded in notNeededServices:
        del services[serviceNotNeeded]


print(yaml.dump(parsedYaml, Dumper=yaml.RoundTripDumper))