#! /usr/bing/env python 3

ingredients=input[["soap, "bleach", "sponges"], ["milk, "beer", "tobasco"], ["sugar", "vanilla", "cocoa"]]
measurements =input["3 cups", "2 tablespoons", "1/2 teaspoon"]

print(f"Pour {measurements[0]} {ingredients[1][0]} into blender. Add in {measurements[1]} {ingredients[2][2]}, {measurements[1]} {ingredients[2][0]}, and {measurements[2]} {ingredients[2][1]}. Blend all ingredients until fully incorporated.")
