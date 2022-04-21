def run():
    
    # WELL DONE, YOU SON OF A SISTER IN CHRIST :D
    dynamic_dict = {
        i: i**3 
        for i in range(1, 101)
        if i % 3 != 0
    }

    print(dynamic_dict)


if __name__ == "__main__":
    run()