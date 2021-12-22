def predict(sports): #sports is a list of sports that user selects, atleast one
    # l1-l6 are the list of categories

    l1 = ["Agility run",
    "High knee",
    "Back kick(running)", 
    "Quick feet",
    "Side runs",
    "Plank runs",
    "Kicking back kick(static)"
    ]
    l2 = ["Single leg ankle hold", 
    "Single leg L holds",
    "Vrikshasana",
    "Single leg swings ( front and back)",
    "T balance"
    ]
    l3 = ["Rock and roll",
    "Crab walk", 
    "Frog jumps", 
    "Duck walk",
    "Gorilla walk",
    "Toe touches ( sitting)",
    "Cobra stand- To be tested",
    "Running drill(cycling)",
    "Hip flexor",
    "Hip/gluteus"]
    l4 = [
        "Frog jumps",
    "Squats", 
    "Lunges",
    "On the spot kicks",
    "Toy March-To be tested",
    "Sumo Squat",
    "Tuck jump(bringing your knees to standing and then jump)"
    ]
    l5 = ["Push ups",
    "Standing 90/90",
    "Standing overhead press",
    "Standing lateral raises"
    ]
    l6 = ["Plank", 
    "Plank  straight leg raises",
    "Crab walk",
    "Plank shoulder taps",
    "Plank arm raises",
    "Donkey kicks",
    "Crab to beast pose",
    "Frog to beast pose(animal flow)",
    "Frog to plank pose",
    "Beast leg raises (alternate hands and legs)",
    "Flutter kick- To be tested",
    "Mountain climbers",
    "Lateral kick- To be tested",
    "Standing high knee and  obliques",
    "Toy march(remove knee angle from high knee)",
    "Alternate toe touch(standing)",
    "Knee kicks(standing)",
    "Standing knee taps (straight)"
    ]

    # d is to link categories to their respective numbers
    d = {1: l1, 2: l2, 3:l3, 4:l4, 5: l5, 6: l6}

    # links connects the sports with their categories, given by vinod sir.
    links = {"Cricket":{1,2,3,6},
    "Badminton": {1,2,3,5,6},
    "Soccer": {1, 3,4,6},
    "Tennis":{1,3,4,5,6},
    "Swimming":{1,3,4,5,6},
    "Skating":{1,2,3,5,6},
     "Table tennis":{1,3,4,6},
    "Athletics":{1,2,3,4,5,6},
    "Taekwondo":{1,2,3,6},
     "Dance":{1,2,3},
    "Fencing":{1, 2,3},
    "Weight loss":{1, 2,3,4,5,6}
    }

    #if the user selects more than one sports then union of set is required to recommend
    fset = links.get(sports[0])
    for i in sports[1:]:
        fset = fset.union(links.get(i))

    # to extract the exercises based on the union of final list of categories
    flist = []
    for i in list(fset):
        flist = flist + d.get(i)
    return set(flist)

print(predict(['Cricket', 'Soccer']))