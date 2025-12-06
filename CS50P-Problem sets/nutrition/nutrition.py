dic = {"apple": 130,
       "avocado": 50,
       "banana" : 110,
       "grapefruit": 60,
       "grapes": 90,
       "kiwifruit": 90,
       "lemon": 15,
       "orange": 80,
       "pear": 100,
       "sweet cherries": 100,
}

fruit = input("Item: ").lower()
if fruit in dic:
    print(f"Calories: {dic[fruit]}")

