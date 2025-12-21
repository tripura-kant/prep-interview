city_wise_data = {
    "Delhi": {
        "population_lakh": 450,
        "avg_temp_c": 30,
        "metro": True
    },
    "Mumbai": {
        "population_lakh": 400,
        "avg_temp_c": 32,
        "metro": True
    },
    "Bengaluru": {
        "population_lakh": 325,
        "avg_temp_c": 26,
        "metro": True
    }
}


# print(city_wise_data["Bengaluru"]["population_lakh"])

a=city_wise_data.get("Mumbai")("metro")
print(a)