# Zelus

Zelus is a distributed framework for testing NoSQL databases under various loads. It's main focus is to coordinate several VMs to act as artificial consumers and perform operations/actions on the desired NoSQL database.

# Architecture

Zelus is comprised of three main types of machines:

1. You
2. Emperors
3. Stormtroopers
4. Rebels

In short: You ask the Emperors to tell the Stormtroopers to perform actions on the Rebels.

Why this multilayered approach? (aka why the Emperors as well?)
This way you reduce the overhead your machine will get when using bigger numbers of VMs.

# Overview 

Assuming you have the VMs ready, you can describe your desired architecture in the config.py file, and then run zelush.sh. There is a custom made shell-like environment to communicate with the VMs. 

A first step would be to deploy the underlying tech to the VMs mentioned in the config.py. Zelus uses Puppet, which is an open-source configuration tool, to set up and configure the VMs to behave as desired.

Once these are complete, you are free to deploy the desired NoSQL DBs on the VMs you specified in the config.py OR you can use machines which already have the NoSQL DBS deployed. Either option is fine, as long as the VMs are mentioned in the config.py file.

# Prerequisites

Run install.sh

# How to use

Run zelush.py

Type help

# Example

Let's assume a scenario. You want to test a Cassandra cluster comprised of three VMs. You want to test this by using three Emperors, each with five Stormtroopers. In this scenario you would need access to 21 VMs:
- 3 Emperors
- 15 Stormtroopers
- 3 Rebels

Now let's assume you have the following IPs available: 1.1.1.1 -> 1.1.1.21

You then decide that you will assign them as follows:

- 1.1.1.1 -> 1.1.1.3  -> Rebels (aka DBs)
- 1.1.1.4 -> 1.1.1.6  -> Emperors
- 1.1.1.7 -> 1.1.1.21 -> Stormtroopers

the config.py for this case can be found in the example folder.
