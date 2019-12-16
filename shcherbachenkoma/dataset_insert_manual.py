def add_info(patient, dataset):
    dataset[patient] = {"agency_name": input("agency_name:"), "average_hcc_score": float(input("average_hcc_score:")),
                        "percent_of_beneficiaries_with_asthma": int(input("percent_of_beneficiaries_with_asthma:"))}
