#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # getting the Keys from the KEY::VALUE pairs
    current_recipe = set(recipe.keys())
    print(current_recipe)  # printing the keys
    if current_recipe.intersection(ingredients.keys()) != current_recipe:
          # if they keys in current recipe and the keys in ingredients dont match...
          # .intersection() finds matching values within two lists of things. nifty find
        return 0

    ingredients_needed = {key: ingredients[key]
                          for key in ingredients if key in recipe}
    # ingredients_needed sets up a new set of ingredients if both
    # keys are found in ingredients and recipe

    batches = 999999999  # as many batches as we might need
    for value in ingredients_needed:
      # for every value in ingredients_needed
        if ingredients[value] // recipe[value] < batches:
          # if when we perform floor division (lowest whole number)
          # to the values of ingredients and recipes and the result is
          # less than the values in batches
            batches = ingredients[value] // recipe[value]
            # create a new number of batches that equals the total number of batches possible.

    return batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 1, 'butter': 5, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
