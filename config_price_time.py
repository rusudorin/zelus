import argparse
import subprocess
import sys
import ec2_price


def create_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument("--region", type=str, help="The region of the instance")
    parser.add_argument("--cost", type=int, help="The time in which the instance will run")
    parser.add_argument("--ebs_type", type=str, help="The type of the storage")
    parser.add_argument("--time", type=int, help="The size of the EBS")

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
    ebs_type = args.ebs_type
    cost = args.cost
    exe_time = args.time

    # basic checks if parse arguments are good
    if region not in ec2_price_dict:
        print "Wrong region"
        sys.exit(1)

    if ebs_type not in ebs_price_dict:
        print "Wrong EBS type"
        sys.exit(2)

    if not cost:
        print "Cost is required"
        sys.exit(3)

    if not exe_time:
        print "Execution time is required"
        sys.exit(4)

    config_list = []
    # for every instance in the region
    for instance in ec2_price_dict[region]:

        # create script call
        script_cmd = "python calculate_price.py --region %s --instance %s --ebs_type %s --time %d --ebs_size %d" % \
                     (region, instance, ebs_type, ebs_size)

        # get the price as a float from script execution response
        price = float(subprocess.check_output(script_cmd, shell=True).strip())

        # initialize instance number count
        instance_nb = 1
        while int(cost / (price * instance_nb)) > 0:
            config_list.append([instance, instance_nb, int(args.cost / (price * instance_nb))])
            instance_nb += 1

    print config_list
    return config_list

if __name__ == "__main__":
    main()
