# Experiences of Landscape Workers: An open-source progressive web app for ethnographic research


## About the Project

This project is a [Progressive Web App](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps) created by [Jeremy Kidwell](https://www.birmingham.ac.uk/staff/profiles/tr/kidwell-jeremy.aspx) and the [Research Software Group](https://intranet.birmingham.ac.uk/it/teams/infrastructure/research/bear/rsg/research-software-group.aspx) at the [University of Birmingham](https://intranet.birmingham.ac.uk/index.aspx).

Recently, a range of [social researchers](https://anthrosource.onlinelibrary.wiley.com/doi/pdf/10.1111/aman.12999) have confirmed that ethnographic fieldwork can be enhanced using smartphones as tools to empower research subjects, enable fieldwork under challenging conditions, and allow for a more immersive account of personal experience.

The ultimate goal of this project is to develop an application platform that is not easily deprecated, extensible, and free-to-use.

This project is an attempt to develop a reproducible open-source client/server model that can scale to different research scenarios. We are using Progressive Web Apps (PWA) to avoid the problems posed by idiosyncratic app-store review policies, platform interoperability, and the constant deprecation of various smartphone OSes.

Initial use and testing of this app will be on a project researching "Experiences of Landscape Workers" by [Jeremy Kidwell](https//jeremykidwell.info) at the University of Birmingham. Development work is being provided by the UOB. Please [get in touch](mailto:j.kidwell@bham.ac.uk) if you'd like to be involved or help with beta testing.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

To run this project, you're required to have the following software installed on your machine:

* Python 3 (for specific Python 3 version please see the [Django documentation](https://www.djangoproject.com/)
* pip
* virtualenv

### Installing

* The project dependencies are specified in requirements.txt
* cd into project directory 
* create a virtualenv
* run `pip install -r requirements.txt`


## Built With

* [Django](https://www.djangoproject.com/) - The Python web framework used
* [Django REST Framework](https://www.django-rest-framework.org/) - The web API framework used
* [PostgreSQL](https://www.postgresql.org/) - The relational database system


## License

See the [LICENSE.md](LICENSE.md) file for details
