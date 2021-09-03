from dataclasses import dataclass
import json

@dataclass(frozen = True)
class historicalObject():
    name: str
    day: int
    month: int
    year: int
    dateSource: str
    imgSource: str

    def from_json(self, json_string):
        json_dict = json.loads(json_string)
        return historicalObject(**json_dict)

# json_string = '''[{
#     "name": "Delaware",
#     "day": 7,
#     "month": 12,
#     "year": 1787,
#     "dateSource": "https://legis.delaware.gov/Resources/History",
#     "image": "https://viola.delaware.gov/files/2017/06/de-largeflag-300x200.png"
# },{
#     "name": "Pennsylvania",
#     "day": 4,
#     "month": 7,
#     "year": 1787,
#     "dateSource": "dateSourcePlaceholder",
#     "image": "imagePlaceholder"
# }]
# '''

# # state = None
# # state = historicalObject.from_json(state, json_string)
# # print(state)

# states = []
# statesJSON = json.loads(json_string)
# for state in statesJSON:
#     states.append(historicalObject.from_json(state, json_string))
# print(states)