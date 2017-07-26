# Zelus

Zelus is a distributed framework for testing NoSQL databases under various loads. It's main focus is to coordinate several VMs to act as artificial consumers and perform operations/actions on the desired NoSQL database.

# Architecture

Zelus is comprised of three main types of machines:

1. You
2. Emperors
3. Stormtroopers

In short: You ask the Emperors to tell the Stormtroopers to perform actions on the DBs.

Why this multilayered approach?
This way you reduce the overhead your machine will get when using bigger numbers of VMs.

# Overview 

Assuming you have the VMs ready, you can describe your desired architecture in the config.py file, and then run zelush.sh. There is a custom made shell-like environment to communicate with the VMs. 

A first step would be to deploy the underlying tech to the VMs mentioned in the config.py. Zelus uses Puppet, which is an open-source configuration tool, to set up and configure the VMs to behave as desired.

Once these are complete, you are free to deploy the desired NoSQL db on the VMs you specified in the config.py OR you can use machines which already have the NoSQL dbs deployed. Either option is fine, as long as the VMs are mentioned in the config.py file.

//TODO

# Prerequisites

Run install.sh
