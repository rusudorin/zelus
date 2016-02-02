# json from amazon with prices
ec2_price = {
    "vers": 0.01,
    "config": {
        "rate": "perhr",
        "valueColumns": [
            "linux"
        ],
        "currencies": [
            "USD"
        ],
        "regions": [
            {
                "region": "us-east",
                "instanceTypes": [
                    {
                        "type": "generalCurrentGen",
                        "sizes": [
                            {
                                "size": "m3.xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.450"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m3.2xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.900"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "generalPreviousGen",
                        "sizes": [
                            {
                                "size": "m1.small",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.060"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m1.medium",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.120"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m1.large",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.240"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m1.xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.480"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "computeCurrentGen",
                        "sizes": [
                            {
                                "size": "c3.large",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.150"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "c3.xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.300"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "c3.2xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.600"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "c3.4xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "1.200"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "c3.8xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "2.400"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "computePreviousGen",
                        "sizes": [
                            {
                                "size": "c1.medium",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.145"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "c1.xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.580"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "cc2.8xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "2.400"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "gpuCurrentGen",
                        "sizes": [
                            {
                                "size": "g2.2xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.650"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "gpuPreviousGen",
                        "sizes": [
                            {
                                "size": "cg1.4xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "2.100"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "hiMemCurrentGen",
                        "sizes": [
                            {
                                "size": "m2.xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.410"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m2.2xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.820"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m2.4xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "1.640"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "cr1.8xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "3.500"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "storageCurrentGen",
                        "sizes": [
                            {
                                "size": "hi1.4xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "3.100"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "hs1.8xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "4.600"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "uI",
                        "sizes": [
                            {
                                "size": "t1.micro",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.020"
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            {
                "region": "us-west-2",
                "instanceTypes": [
                    {
                        "type": "generalCurrentGen",
                        "sizes": [
                            {
                                "size": "m3.xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.450"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m3.2xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.900"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "generalPreviousGen",
                        "sizes": [
                            {
                                "size": "m1.small",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.060"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m1.medium",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.120"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m1.large",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.240"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m1.xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.480"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "computeCurrentGen",
                        "sizes": [
                            {
                                "size": "c3.large",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.150"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "c3.xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.300"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "c3.2xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.600"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "c3.4xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "1.200"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "c3.8xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "2.400"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "computePreviousGen",
                        "sizes": [
                            {
                                "size": "c1.medium",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.145"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "c1.xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.580"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "cc2.8xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "2.400"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "gpuCurrentGen",
                        "sizes": [
                            {
                                "size": "g2.2xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.650"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "hiMemCurrentGen",
                        "sizes": [
                            {
                                "size": "m2.xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.410"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m2.2xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.820"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m2.4xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "1.640"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "cr1.8xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "3.500"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "storageCurrentGen",
                        "sizes": [
                            {
                                "size": "hi1.4xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "3.100"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "hs1.8xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "4.600"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "uI",
                        "sizes": [
                            {
                                "size": "t1.micro",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.020"
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            {
                "region": "us-west",
                "instanceTypes": [
                    {
                        "type": "generalCurrentGen",
                        "sizes": [
                            {
                                "size": "m3.xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.495"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m3.2xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.990"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "generalPreviousGen",
                        "sizes": [
                            {
                                "size": "m1.small",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.065"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m1.medium",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.130"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m1.large",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.260"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m1.xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.520"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "computePreviousGen",
                        "sizes": [
                            {
                                "size": "c1.medium",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.165"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "c1.xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.660"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "gpuCurrentGen",
                        "sizes": [
                            {
                                "size": "g2.2xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.702"
                                        }
                                    }
                                ]
                            }
						]
					},
                    {
                        "type": "hiMemCurrentGen",
                        "sizes": [
                            {
                                "size": "m2.xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.460"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m2.2xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.920"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m2.4xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "1.840"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "uI",
                        "sizes": [
                            {
                                "size": "t1.micro",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.025"
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            {
                "region": "eu-ireland",
                "instanceTypes": [
                    {
                        "type": "generalCurrentGen",
                        "sizes": [
                            {
                                "size": "m3.xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.495"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m3.2xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.990"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "generalPreviousGen",
                        "sizes": [
                            {
                                "size": "m1.small",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.065"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m1.medium",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.130"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m1.large",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.260"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m1.xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.520"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "computeCurrentGen",
                        "sizes": [
                            {
                                "size": "c3.large",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.171"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "c3.xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.342"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "c3.2xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.683"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "c3.4xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "1.366"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "c3.8xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "2.732"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "computePreviousGen",
                        "sizes": [
                            {
                                "size": "c1.medium",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.165"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "c1.xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.660"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "cc2.8xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "2.700"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
    				{
                        "type": "gpuCurrentGen",
                        "sizes": [
                            {
                                "size": "g2.2xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.702"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "gpuPreviousGen",
                        "sizes": [
                            {
                                "size": "cg1.4xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "2.36"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "hiMemCurrentGen",
                        "sizes": [
                            {
                                "size": "m2.xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.460"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m2.2xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.920"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m2.4xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "1.840"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "cr1.8xlarge",
                                "valueColumns": [
                                    {
                                       "name": "linux",
                                        "prices": {
                                            "USD": "3.750"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "storageCurrentGen",
                        "sizes": [
                            {
                                "size": "hi1.4xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "3.410"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "hs1.8xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "4.900"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "uI",
                        "sizes": [
                            {
                                "size": "t1.micro",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.020"
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            {
                "region": "apac-sin",
                "instanceTypes": [
                    {
                        "type": "generalCurrentGen",
                        "sizes": [
                            {
                                "size": "m3.xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.630"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m3.2xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "1.260"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "generalPreviousGen",
                        "sizes": [
                            {
                                "size": "m1.small",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.080"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m1.medium",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.160"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m1.large",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.320"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m1.xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.640"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "computeCurrentGen",
                        "sizes": [
                            {
                                "size": "c3.large",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.189"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "c3.xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.378"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "c3.2xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.756"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "c3.4xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "1.512"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "c3.8xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "3.024"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "computePreviousGen",
                        "sizes": [
                            {
                                "size": "c1.medium",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.183"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "c1.xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.730"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "hiMemCurrentGen",
                        "sizes": [
                            {
                                "size": "m2.xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.495"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m2.2xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.990"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m2.4xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "1.980"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "storageCurrentGen",
                        "sizes": [
                            {
                                "size": "hs1.8xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "5.570"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "uI",
                        "sizes": [
                            {
                                "size": "t1.micro",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.020"
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            {
                "region": "apac-tokyo",
                "instanceTypes": [
                    {
                        "type": "generalCurrentGen",
                        "sizes": [
                            {
                                "size": "m3.xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.684"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m3.2xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "1.368"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "generalPreviousGen",
                        "sizes": [
                            {
                                "size": "m1.small",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.088"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m1.medium",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.175"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m1.large",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.350"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m1.xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.700"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "computeCurrentGen",
                        "sizes": [
                            {
                                "size": "c3.large",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.192"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "c3.xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.383"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "c3.2xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.766"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "c3.4xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "1.532"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "c3.8xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "3.064"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "computePreviousGen",
                        "sizes": [
                            {
                                "size": "c1.medium",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.185"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "c1.xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.740"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "cc2.8xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "2.960"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "hiMemCurrentGen",
                        "sizes": [
                            {
                                "size": "m2.xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.505"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m2.2xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "1.010"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m2.4xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "2.020"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "cr1.8xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "4.310"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "storageCurrentGen",
                        "sizes": [
                            {
                                "size": "hi1.4xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "3.820"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "hs1.8xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "5.670"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "uI",
                        "sizes": [
                            {
                                "size": "t1.micro",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.027"
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            {
                "region": "apac-syd",
                "instanceTypes": [
                    {
                        "type": "generalCurrentGen",
                        "sizes": [
                            {
                                "size": "m3.xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.630"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m3.2xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "1.260"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "generalPreviousGen",
                        "sizes": [
                            {
                                "size": "m1.small",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.080"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m1.medium",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.160"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m1.large",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.320"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m1.xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.640"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "computeCurrentGen",
                        "sizes": [
                            {
                                "size": "c3.large",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.189"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "c3.xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.378"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "c3.2xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.756"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "c3.4xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "1.512"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "c3.8xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "3.024"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "computePreviousGen",
                        "sizes": [
                            {
                                "size": "c1.medium",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.183"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "c1.xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.730"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "hiMemCurrentGen",
                        "sizes": [
                            {
                                "size": "m2.xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.495"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m2.2xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.990"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m2.4xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "1.980"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "storageCurrentGen",
                        "sizes": [
                            {
                                "size": "hs1.8xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "5.570"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "uI",
                        "sizes": [
                            {
                                "size": "t1.micro",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.020"
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            {
                "region": "sa-east-1",
                "instanceTypes": [
                    {
                        "type": "generalCurrentGen",
                        "sizes": [
                            {
                                "size": "m3.xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.612"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m3.2xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "1.224"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "generalPreviousGen",
                        "sizes": [
                            {
                                "size": "m1.small",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.080"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m1.medium",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.160"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m1.large",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.320"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m1.xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.640"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "computePreviousGen",
                        "sizes": [
                            {
                                "size": "c1.medium",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.200"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "c1.xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.800"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "hiMemCurrentGen",
                        "sizes": [
                            {
                                "size": "m2.xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.540"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m2.2xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "1.080"
                                        }
                                    }
                                ]
                            },
                            {
                                "size": "m2.4xlarge",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "2.160"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "uI",
                        "sizes": [
                            {
                                "size": "t1.micro",
                                "valueColumns": [
                                    {
                                        "name": "linux",
                                        "prices": {
                                            "USD": "0.027"
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    }
}

ec2_price_dict = {
    'apac-sin': {
        'm1.medium': 0.16,
        't1.micro': 0.02,
        'm3.2xlarge': 1.26,
        'c3.xlarge': 0.378,
        'm1.large': 0.32,
        'c1.xlarge': 0.73,
        'hs1.8xlarge': 5.57,
        'c3.2xlarge': 0.756,
        'm1.small': 0.08,
        'c1.medium': 0.183,
        'c3.4xlarge': 1.512,
        'm2.2xlarge': 0.99,
        'm1.xlarge': 0.64,
        'm2.xlarge': 0.495,
        'c3.8xlarge': 3.024,
        'm2.4xlarge': 1.98,
        'c3.large': 0.189,
        'm3.xlarge': 0.63
    },
    'us-west': {
        'm1.medium': 0.13,
        'm3.2xlarge': 0.99,
        'm1.large': 0.26,
        'c1.xlarge': 0.66,
        'g2.2xlarge': 0.702,
        'm1.small': 0.065,
        'c1.medium': 0.165,
        'm1.xlarge': 0.52,
        'm2.xlarge': 0.46,
        't1.micro': 0.025,
        'm2.4xlarge': 1.84,
        'm2.2xlarge': 0.92,
        'm3.xlarge': 0.495
    },
    'apac-syd': {
        'm1.medium': 0.16,
        't1.micro': 0.02,
        'm3.2xlarge': 1.26,
        'c3.xlarge': 0.378,
        'm1.large': 0.32,
        'c1.xlarge': 0.73,
        'hs1.8xlarge': 5.57,
        'c3.2xlarge': 0.756,
        'm1.small': 0.08,
        'c1.medium': 0.183,
        'c3.4xlarge': 1.512,
        'm2.2xlarge': 0.99,
        'm1.xlarge': 0.64,
        'm2.xlarge': 0.495,
        'c3.8xlarge': 3.024,
        'm2.4xlarge': 1.98,
        'c3.large': 0.189,
        'm3.xlarge': 0.63
    },
    'eu-ireland': {
        'm3.2xlarge': 0.99,
        'm1.small': 0.065,
        'c1.medium': 0.165,
        'cg1.4xlarge': 2.36,
        't1.micro': 0.02,
        'cr1.8xlarge': 3.75,
        'c3.2xlarge': 0.683,
        'c3.xlarge': 0.342,
        'm1.large': 0.26,
        'hs1.8xlarge': 4.9,
        'c3.8xlarge': 2.732,
        'c3.4xlarge': 1.366,
        'hi1.4xlarge': 3.41,
        'm2.2xlarge': 0.92,
        'c1.xlarge': 0.66,
        'g2.2xlarge': 0.702,
        'm2.xlarge': 0.46,
        'm1.medium': 0.13,
        'cc2.8xlarge': 2.7,
        'c3.large': 0.171,
        'm1.xlarge': 0.52,
        'm2.4xlarge': 1.84,
        'm3.xlarge': 0.495
    },
    'apac-tokyo': {
        'm1.medium': 0.175,
        't1.micro': 0.027,
        'm3.2xlarge': 1.368,
        'c3.xlarge': 0.383,
        'cc2.8xlarge': 2.96,
        'm1.large': 0.35,
        'c1.xlarge': 0.74,
        'hs1.8xlarge': 5.67,
        'cr1.8xlarge': 4.31,
        'c3.2xlarge': 0.766,
        'm1.small': 0.088,
        'c1.medium': 0.185,
        'c3.4xlarge': 1.532,
        'm2.2xlarge': 1.01,
        'm1.xlarge': 0.7,
        'm2.xlarge': 0.505,
        'hi1.4xlarge': 3.82,
        'c3.8xlarge': 3.064,
        'm2.4xlarge': 2.02,
        'c3.large': 0.192,
        'm3.xlarge': 0.684
    },
    'us-east': {
        'm3.2xlarge': 0.9,
        'm1.small': 0.06,
        'c1.medium': 0.145,
        'cg1.4xlarge': 2.1,
        't1.micro': 0.02,
        'cr1.8xlarge': 3.5,
        'c3.2xlarge': 0.6,
        'c3.xlarge': 0.3,
        'm1.large': 0.24,
        'hs1.8xlarge': 4.6,
        'c3.8xlarge': 2.4,
        'c3.4xlarge': 1.2,
        'hi1.4xlarge': 3.1,
        'm2.2xlarge': 0.82,
        'c1.xlarge': 0.58,
        'g2.2xlarge': 0.65,
        'm2.xlarge': 0.41,
        'm1.medium': 0.12,
        'cc2.8xlarge': 2.4,
        'c3.large': 0.15,
        'm1.xlarge': 0.48,
        'm2.4xlarge': 1.64,
        'm3.xlarge': 0.45
    },
    'us-west-2': {
        'm3.2xlarge': 0.9,
        'm1.small': 0.06,
        'c1.medium': 0.145,
        't1.micro': 0.02,
        'cr1.8xlarge': 3.5,
        'c3.2xlarge': 0.6,
        'c3.xlarge': 0.3,
        'm1.large': 0.24,
        'hs1.8xlarge': 4.6,
        'c3.8xlarge': 2.4,
        'c3.4xlarge': 1.2,
        'hi1.4xlarge': 3.1,
        'm2.2xlarge': 0.82,
        'c1.xlarge': 0.58,
        'g2.2xlarge': 0.65,
        'm2.xlarge': 0.41,
        'm1.medium': 0.12,
        'cc2.8xlarge': 2.4,
        'c3.large': 0.15,
        'm1.xlarge': 0.48,
        'm2.4xlarge': 1.64,
        'm3.xlarge': 0.45
    },
    'sa-east-1': {
        'm1.medium': 0.16,
        'm3.2xlarge': 1.224,
        'm1.large': 0.32,
        'c1.xlarge': 0.8,
        'm1.small': 0.08,
        'c1.medium': 0.2,
        'm1.xlarge': 0.64,
        'm2.xlarge': 0.54,
        't1.micro': 0.027,
        'm2.4xlarge': 2.16,
        'm2.2xlarge': 1.08,
        'm3.xlarge': 0.612
    }
}

ebs_price_dict = {
        'general': 0.100,
        'provisioned': 0.125,
        'provisioned_iops': 0.065,
        'magnetic': 0.05,
        'magnetic_io': 0.05
        }

def get_region_dict():
	# soon to be
	region_dict = {}

	# for every region
	for region in ec2_price['config']['regions']:

		# new key for every region
		region_dict[region['region']] = {}

		# for every instance type
		for instance in region['instanceTypes']:

			for size in instance['sizes']:

				region_dict[region['region']][size['size']] = float(size['valueColumns'][0]['prices']['USD'])

	return region_dict
