#------------------------GETTING THE CATEGORIES OPTIONS------------------------------------

import requests as rp

import json 


def categories_list() -> list :
  quiz_cati = "https://opentdb.com/api_category.php"
  res = rp.get(url=quiz_cati)
  res_json = res.json()
  tri_category = res_json["trivia_categories"]
  print("Category ID  |  Category Name")
  print("-" * 30)
  for cat in tri_category:
    print(f"{cat['id']:11}  |  {cat['name']}")          



  



  
  