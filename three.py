# Data points
x = [0, 1, 2, 3, 4]
y = [2, 3, 5, 4, 6]

# Number of data points
n = len(x)

# Step 1: Calculate the mean of x and y
mean_x = sum(x) / n
mean_y = sum(y) / n

# Step 2: Calculate the slope (a)
numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
denominator = sum((x[i] - mean_x) ** 2 for i in range(n))
a = numerator / denominator

# Step 3: Calculate the intercept (b)
b = mean_y - a * mean_x

# Linear regression line equation: y = ax + b
print(f"Linear regression line: y = {a}x + {b}")

# Step 4: Estimate the value of y when x = 10
x_estimate = 10
y_estimate = a * x_estimate + b
print(f"Estimated value of y when x = {x_estimate}: {y_estimate}")

# Step 5: Calculate the error (Sum of Squared Errors)
sse = sum((y[i] - (a * x[i] + b)) ** 2 for i in range(n))
print(f"Sum of Squared Errors: {sse}")
