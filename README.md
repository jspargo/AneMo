# AneMo
Home automation proof of concept. Raspberry Pi based thermostatic controller.

# Operation and Architecture
Broadly the solution is split into 4 sections:
* A controller application that runs on a publically accessible server (e.g. AWS). This contains the rules and current temperature recordings - **anemoController/**
* A recorder that measures the temperture and posts it to the controller - **thermo/**
* An actor that uses the current temperature and rules from the server to decide whether to send a signal to the boiler to turn the heating on or off - *not yet built*
* An accompanying iPhone app for updating the rules (e.g. temperature thresholds, times and overrides) - *not yet built*

Pull requests and comment gladly appreciated! Feel free to contact me via github or on [Twitter](https://twitter.com/jackspargo)