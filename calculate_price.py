#! /bin/python
# calculate the price of a certain instance
import argparse
import sys
import ec2_price


def create_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument("--region", type=str, help="The region of the instance")
    parser.add_argument("--instance", type=str, help="The type of the instance")
    parser.add_argument("--time", type=int, help="The time in which the instance will run")
    parser.add_argument("--ebs_type", type=str, help="The type of the storage")
    parser.add_argument("--ebs_size", type=int, help="The size of the EBS")

    return parser


def parse_arguments(arguments, parser):
    args = parser.parse_args(arguments)
    return args


def main():
    # initiate parser
    parser = create_parser()
    args = parse_arguments(sys.argv[1:], parser)

    # get prices dictionaries
    ec2_price_dict = ec2_price.ec2_price_dict
    ebs_price_dict = ec2_price.ebs_price_dict

    region = args.region
    instance = args.instance
    ebs_type = args.ebs_type
    ebs_size = args.ebs_size
    exe_time = args.time

    # basic checks if parse arguments are good
    if region not in ec2_price_dict:
        print "Wrong region"
        sys.exit(1)

    if instance not in ec2_price_dict[region]:
        print "Wrong instance"
        sys.exit(2)

    if ebs_type not in ebs_price_dict:
        print "Wrong EBS type"
        sys.exit(3)

    if not exe_time:
        print "Time is required"
        sys.exit(4)

    if not ebs_size:
        print "Size is required"
        sys.exit(5)

    # calculate ec2 price
    price = exe_time * ec2_price_dict[region][instance]

    # calculate ebs price
    price += ebs_price_dict[ebs_type] * ebs_size

    print price
    return price

if __name__ == "__main__":
    main()
