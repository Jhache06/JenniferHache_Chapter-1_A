def pre_sell_ticket():
    # Assign variables for total tickets allowed and buyers
    max_tickets = 20
    max_buyers = 0

    # Create loop for number of tickets up to 4 per buyer
    while max_tickets > 0:
        try:
            # Ask user how many tickets they want to purchase
            tickets_requested = int(input("Please enter the number of tickets you want to purchase: "))

            # Check to see if user entered correct number of ticket purchased
            if tickets_requested < 1 or tickets_requested > 4:
                print("You can only purchase between 1 and 4 tickets.")
                continue

            # Check to see if remaining tickets can complete requested purchase
            if tickets_requested > max_tickets:
                print(f"Only {max_tickets} tickets remain. Please enter a valid number.")
                continue

            # Subtract the max allowed tickets purchased from max available
            max_tickets -= tickets_requested
            # Increase the count of the buyer by 1
            max_buyers += 1
            # Tell user how many tickets remain
            print(f"Tickets purchased: {tickets_requested}. Tickets remaining: {max_tickets}.")

        except ValueError:
            # Add entry that tells user if they entered an incorrect number
            print("Invalid entry. Please enter a number.")

    # Print total buyers
    print(f"All tickets are sold. Total number of buyers: {max_buyers}")

# Run the function for ticket sell
pre_sell_ticket()
