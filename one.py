import csv
import math
import pprint
from collections import defaultdict
from itertools import chain, combinations

# Data from the table
data = [
    {'Outlook': 'Sunny', 'Temperature': 'Hot', 'Humidity': 'High', 'Wind': 'Weak', 'PlayTennis': 'No'},
    {'Outlook': 'Sunny', 'Temperature': 'Hot', 'Humidity': 'High', 'Wind': 'Strong', 'PlayTennis': 'No'},
    {'Outlook': 'Overcast', 'Temperature': 'Hot', 'Humidity': 'High', 'Wind': 'Weak', 'PlayTennis': 'Yes'},
    {'Outlook': 'Rain', 'Temperature': 'Mild', 'Humidity': 'High', 'Wind': 'Weak', 'PlayTennis': 'Yes'},
    {'Outlook': 'Rain', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Wind': 'Weak', 'PlayTennis': 'Yes'},
    {'Outlook': 'Rain', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Wind': 'Strong', 'PlayTennis': 'No'},
    {'Outlook': 'Overcast', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Wind': 'Strong', 'PlayTennis': 'Yes'},
    {'Outlook': 'Sunny', 'Temperature': 'Mild', 'Humidity': 'High', 'Wind': 'Weak', 'PlayTennis': 'No'},
    {'Outlook': 'Sunny', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Wind': 'Weak', 'PlayTennis': 'Yes'},
    {'Outlook': 'Rain', 'Temperature': 'Mild', 'Humidity': 'Normal', 'Wind': 'Weak', 'PlayTennis': 'Yes'},
    {'Outlook': 'Sunny', 'Temperature': 'Mild', 'Humidity': 'Normal', 'Wind': 'Strong', 'PlayTennis': 'Yes'},
    {'Outlook': 'Overcast', 'Temperature': 'Mild', 'Humidity': 'High', 'Wind': 'Strong', 'PlayTennis': 'Yes'},
    {'Outlook': 'Overcast', 'Temperature': 'Hot', 'Humidity': 'Normal', 'Wind': 'Weak', 'PlayTennis': 'Yes'},
    {'Outlook': 'Rain', 'Temperature': 'Mild', 'Humidity': 'High', 'Wind': 'Strong', 'PlayTennis': 'No'}
]

# Save the dataset as CSV
csv_file = 'play_tennis.csv'
csv_columns = data[0].keys()

try:
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
except IOError:
    print("I/O error")

# Read the dataset from CSV
def read_csv(file):
    dataset = []
    with open(file, mode='r') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            dataset.append(row)
    return dataset

data = read_csv(csv_file)

# Helper function to calculate entropy
def entropy(s):
    label_counts = defaultdict(int)
    for entry in s:
        label = entry['PlayTennis']
        label_counts[label] += 1

    total_entries = len(s)
    ent = 0.0
    for label in label_counts:
        prob = label_counts[label] / total_entries
        ent -= prob * math.log2(prob)
    return ent

# Helper function to calculate information gain
def info_gain(s, attribute):
    base_entropy = entropy(s)

    subsets = defaultdict(list)
    for entry in s:
        key = entry[attribute]
        subsets[key].append(entry)

    total_entries = len(s)
    subset_entropy = 0.0
    for key in subsets:
        prob = len(subsets[key]) / total_entries
        subset_entropy += prob * entropy(subsets[key])

    return base_entropy - subset_entropy

# Function to choose the best attribute to split on
def choose_best_attribute(s, attributes):
    best_gain = 0.0
    best_attr = None
    for attribute in attributes:
        gain = info_gain(s, attribute)
        if gain > best_gain:
            best_gain = gain
            best_attr = attribute
    return best_attr

# Recursive function to build the decision tree
def build_tree(s, attributes):
    labels = [entry['PlayTennis'] for entry in s]
    if labels.count(labels[0]) == len(labels):
        return labels[0]

    if not attributes:
        return max(set(labels), key=labels.count)

    best_attr = choose_best_attribute(s, attributes)

    tree = {best_attr: {}}

    unique_values = set(entry[best_attr] for entry in s)

    remaining_attrs = [attr for attr in attributes if attr != best_attr]

    for value in unique_values:
        subset = [entry for entry in s if entry[best_attr] == value]
        subtree = build_tree(subset, remaining_attrs)
        tree[best_attr][value] = subtree

    return tree

# List of attributes
attributes = ['Outlook', 'Temperature', 'Humidity', 'Wind']

# Build the decision tree
decision_tree = build_tree(data, attributes)

# Print the decision tree
pprint.pprint(decision_tree)
