
            computer_boat_coordinates = random.sample(range(0, 4), 2)
            if not any(np.array_equal(computer_boat_coordinates, coord) for coord in player