import matplotlib.pyplot as plt
import random

def isValidCharge(distance, M, swifstride=False, waaagh=False, reroll=False):
    # Log the initial parameters
    print(f"Attempting charge with distance: {distance}, M: {M}, swifstride: {swifstride}, waaagh: {waaagh}, reroll: {reroll}")

    # Calculate base charge
    charge = M + max(random.randint(1, 6), random.randint(1, 6))

    # Apply Swifstride bonus
    if swifstride:
        charge += random.randint(1, 6)
        print("Swifstride bonus applied.")

    # Apply Waaagh bonus
    if waaagh:
        charge += random.randint(1, 3)
        print("Waaagh bonus applied.")

    # Check if charge is successful
    if charge <= distance:
        print("Charge successful!")
        return True

    # If reroll is true, attempt a reroll
    if reroll:
        print("Rerolling charge...")
        return isValidCharge(distance, M, swifstride, waaagh, reroll=False)

    # If reroll is false and charge is unsuccessful, return false
    print("Charge failed.")
    return False


def simulation():
    M = 7
    swifstride = True
    waaagh = True
    reroll = True
    num_trials = 10000

    distances = range(12, 25)
    percentages = []

    for distance in distances:
        valid_count = 0

        for _ in range(num_trials):
            if isValidCharge(distance, M, swifstride, waaagh, reroll):
                valid_count += 1

        percentage_valid = (valid_count / num_trials) * 100
        percentages.append(percentage_valid)

    return distances, percentages

distances, percentages = simulation()

plt.plot(distances, percentages, marker='o')
plt.title('Percentage of Valid Charges')
plt.xlabel('Distance')
plt.ylabel('Percentage')
plt.xticks(range(12, 25))
plt.grid(True)
plt.show()