import numpy as np
import matplotlib.pyplot as plt

# Define the level of granularity or number of steps in a process/model
Volatility = 0.1

xfid = []
y1 = []
y2 = []


while Volatility < 100:


    # Define the current price of the underlying asset (e.g., a stock)
    fidelity = 256

    # Define the strike price of an option
    strike_price = 240

    # Define the total time until an event occurs (e.g., option expiration)
    # Often measured in years.
    DTE = 7

    time_to_expiry = (DTE/7)/52

    stock_price = 250



    # Define the annual risk-free interest rate
    annual_interest_rate = 0.04


    # Define the upward movement factor
    # In a binomial model, 'u' represents the factor by which the asset price
    # multiplies during an upward step. Usually u > 1.
    u = (1+Volatility)**(1/fidelity) # Example: Price goes up by 10% (1.1 times) in an upward step
    d = 1/u
    p = ((1+(annual_interest_rate*time_to_expiry/fidelity))-d)/(u-d)
    p_inv = 1-p

    Discount_Factor = (1+(annual_interest_rate*time_to_expiry/fidelity))**fidelity






    # Function to generate a single row of Pascal's Triangle
    def get_pascal_row(row_index):
        """
        Generates a list representing the row_index-th row of Pascal's Triangle.
        Row index starts at 0.
        """
        if row_index < 0:
            return "Row index cannot be negative."

        # Row 0 is the base case
        if row_index == 0:
            return [1]

        # Start with row 0
        current_row = [1]

        # Iterate to generate subsequent rows up to the desired index
        # We need to perform 'row_index' iterations to get from row 0 to row 'row_index'
        for i in range(1, row_index + 1):
            # To get the next row (row i) from the current row (row i-1):
            # - It starts with 1
            # - The middle elements are the sum of adjacent elements in the previous row
            # - It ends with 1
            next_row = [1] # Start of the next row is always 1

            # Calculate the intermediate values
            # For row i, the previous row (current_row) has i elements.
            # We need to calculate i-1 sums.
            # Iterate through the previous row's elements (except the last one)
            for j in range(len(current_row) - 1):
                # The next element is the sum of current_row[j] and current_row[j+1]
                next_value = current_row[j] + current_row[j+1]
                next_row.append(next_value) # Add the sum to the next row

            next_row.append(1) # End of the next row is always 1

            # The generated 'next_row' now becomes the 'current_row' for the next iteration
            current_row = next_row

        # After the loop, current_row holds the list for the desired row_index
        return current_row

    # --- Main part of the program ---

    # Ask the user for the fidelity (row index)
    try:

        # Get the Pascal's Triangle row
        pascal_row_values = get_pascal_row(fidelity)

        # Print the result
        if isinstance(pascal_row_values, list):
            print(f"\nPascal's Triangle Row {fidelity} (Fidelity {fidelity}):")
            print(pascal_row_values)
        else:
            print(f"\nError: {pascal_row_values}") # Handle the negative index case

    except ValueError:
        print("\nInvalid input. Please enter a whole number for the fidelity.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")


    # Define the variables (using the names from your request)
    Stock_Price = stock_price         # Initial stock price
    Fidelity = fidelity                # Number of steps/periods (corresponds to row index of Pascal's Triangle)
    annual_inr_rate = annual_interest_rate      # Annual interest rate (often needed for pricing, but not for just terminal values)                     # Upward movement factor
    Strike_Price = strike_price       # Strike price (often needed for option value, but not for just terminal values)


    # Clarification on Fidelity and Pascal's Triangle:
    # Fidelity (N) represents the number of steps.
    # A path can have anywhere from 0 upward movements (all downs) to N upward movements (all ups).
    # These correspond to the indices 0 through N of Pascal's Triangle Row N.
    # The i-th element of Pascal's Triangle Row N is the count of paths with i up moves.
    # The TERMINAL PRICE for a path with i up moves is:
    # Stock_Price * (u ^ i) * (d ^ (N - i))

    # Create an empty list to store the possible terminal values
    possible_terminal_values = []

    # Iterate through the possible number of upward movements (from 0 to Fidelity)
    # This 'i' corresponds to the 'column index' or 'number of ups'
    for i in range(Fidelity + 1):
        # The number of upward movements is 'i'
        num_up_moves = i

        # The number of downward movements is Fidelity - i
        num_down_moves = Fidelity - i

        # Calculate the terminal price using the formula: Initial_Price * (u^num_up_moves) * (d^num_down_moves)
        # We use the ** operator for exponentiation
        terminal_price_at_node = Stock_Price * (u ** num_up_moves) * (d ** num_down_moves)

        # Add the calculated terminal price to our list
        possible_terminal_values.append(terminal_price_at_node)





    # Create empty lists to store the terminal call and put values
    terminal_call_values = []
    terminal_put_values = []

    # Iterate through each possible terminal stock price
    for terminal_price in possible_terminal_values:
        # Calculate the Call Option value at this terminal price
        # Value is max(0, Stock Price - Strike Price)
        call_value = max(0, terminal_price - Strike_Price)

        # Calculate the Put Option value at this terminal price
        # Value is max(0, Strike Price - Stock Price)
        put_value = max(0, Strike_Price - terminal_price)

        # Append the calculated values to their respective lists
        terminal_call_values.append(call_value)
        terminal_put_values.append(put_value)




    prob_CV = []
    prob_PV = []
    percent = []

    x = -1
    for probability in pascal_row_values:

        x=x+1

        percent.insert(0,(((p**(fidelity-x))*((1-p)**(fidelity-(fidelity-x))))*probability))

    print("\nTotal Probabilities")
    print(percent)

    values_Calls = terminal_call_values
    values_Puts = terminal_put_values
    weights = percent

    # --- Calculation ---
    try:
        weighted_average_Call = np.average(values_Calls, weights=weights)
        weighted_average_Put = np.average(values_Puts, weights=weights)



    except ZeroDivisionError:
        print("Error: Sum of weights is zero. Cannot calculate weighted average.")
    except ValueError as e:
        # Handles cases like unequal length or weights being non-numeric
        print(f"Error calculating weighted average: {e}")


    Binomial_Call_Value = weighted_average_Call/Discount_Factor
    Binomial_Put_Value = weighted_average_Put/Discount_Factor

    Volatility = Volatility + 0.1

    xfid.append(Volatility)
    y1.append(Binomial_Call_Value)
    y2.append(Binomial_Put_Value)



# Create the plot
plt.plot(xfid, y1, label='Calls')
plt.plot(xfid, y2, label='Puts')


# Add labels and a title (optional but recommended)
plt.xlabel("volatility")
plt.ylabel("$")
plt.title("Volatility vs $")

# Display the plot
plt.legend()

plt.show()


# --- You can print the values to verify they are defined ---
print(f"Stock Price: {stock_price}")
print(f"Fidelity (Steps): {fidelity}")
print(f"VOlatility: {Volatility}")
print(f"Time to Expiry (Years): {time_to_expiry}")
print(f"Annual Interest Rate: {annual_interest_rate}")
print(f"Upward Movement Factor (u): {u}")
print(f"Downward Movement Factor (d): {d}")
print(f"Probability of an Upward Move: {p}")
print(f"Probability of a Downward Move: {p_inv}")
print(f"Discount Factor: {Discount_Factor}")
print(f"Strike Price: {strike_price}")

print(f"\nList of Possible Terminal Stock Prices after {Fidelity} steps:")
print(possible_terminal_values)

print(f"\nCorresponding Terminal Call Option Values:")
print([f"{val:.2f}" for val in terminal_call_values])

print(f"\nCorresponding Terminal Put Option Values:")
print([f"{val:.2f}" for val in terminal_put_values])


print(f"Weighted Average (NumPy): {weighted_average_Call}")
print(f"Weighted Average (NumPy): {weighted_average_Put}")


print("\n╔========")
print(f"\nBinomial Call Value: {Binomial_Call_Value}")
print(f"Binomial Put Value: {Binomial_Put_Value}")
print("\n╚========")