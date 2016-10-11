#!/usr/bin/env python

"""Composer let's you remove unnecessary services from a Docker Compose file. It is built for larger stacks with many services,
and the fact the not every service is needed always.

Usage:
  composer.py compose --env=ENV [--with=SERVICES...] [--without=SERVICES...]
  composer.py (-h | --help)
  composer.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.

"""


import ruamel.yaml as yaml
import inquirer
from docopt import docopt
import urllib, json

if __name__ == '__main__':
    arguments = docopt(__doc__, version='Composer 0.1')
    #print arguments

#################################


with open("/composer/project/docker-compose.yml") as stream:
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
    print "\n"
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

################################

# inspired by http://stackoverflow.com/questions/38252507/how-can-i-get-comments-from-a-yaml-file-using-ruamel-yaml-in-python
for service, props in services.items():
    if 'image' in services[service].ca.items:
        comment = services[service].ca.items['image'][2].value
        repo_url = comment[1:]

        response = urllib.urlopen(repo_url)
        data = json.loads(response.read())

        branches = []
        for branch in data:
            branches.append(branch['name'])

        questions = [
            inquirer.List('branch',
                              message="Which " + service + " branch do you prefer?",
                              choices=branches
                              ),
        ]
        branch = inquirer.prompt(questions)['branch']
        if branch != 'master':
            props['image'] = props['image'] + ':' + branch

modifiedYaml = yaml.dump(parsedYaml, Dumper=yaml.RoundTripDumper)
fileName = "/composer/project/docker-compose." + arguments['--env']  + ".yml"

target = open(fileName, 'w')
target.write(modifiedYaml)
target.close()

print "Compose file written to " + fileName
