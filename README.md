# An open-source app for ethnographic research

This repository includes code to set up a server for app-based ethnographic research.

Recently, a range of [social researchers](https://anthrosource.onlinelibrary.wiley.com/doi/pdf/10.1111/aman.12999) have confirmed that ethnographic fieldwork can be enhanced using smartphones as tools to empower research subjects, enable fieldwork under challenging conditions, and allow for a more immersive account of personal experience.

The ultimate goal of this project is to develop an application platform that is not easily deprecated, extensible, and free-to-use.

This project is an attempt to develop a reproducible open-source client/server model that can scale to different research scenarios. 
- We are using Progressive Web Apps (PWA) to avoid the problems posed by idiosyncratic app-store review policies, platform interoperability, and the constant deprecation of various smartphone OSes. Coding will be in [React Native](https://reactnative.dev/).
- The server-side implementation uses [Django](https://www.djangoproject.com/) a popular and easy to use Python Web framework.
- The back-end Database is sql

Initial use and testing of this app will be on a project researching "Experiences of Landscape Workers" by [Jeremy Kidwell](https//jeremykidwell.info) at the University of Birmingham. Development work is being provided by the UOB. Please [get in touch](mailto:j.kidwell@bham.ac.uk) if you'd like to be involved or help with beta testing.
