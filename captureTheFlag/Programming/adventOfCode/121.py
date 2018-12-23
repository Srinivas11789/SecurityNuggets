def generation(initial_state, notes_):
    initial_state = list("..."+initial_state+"...........")
    n = len(initial_state)
    for i in range(1):
        j = 0
        new_state = []
        while j < n:
            select = "".join(initial_state[j:j+5])
            #print initial_state, select
            if select in notes_:
               select = list(".."+notes_[select]+"..")
               #print select
               initial_state[j:j+5] = select
               j += 2
            else:
                j+= 1
            print "".join(initial_state)

            #initial_state[j:j+5] = list(select)
            #new_state.extend(list(select))
            #print "".join(initial_state)
        #initial_state = new_state

    return "".join(initial_state)

def main():
    # Fetch input from url
    import requests, sys
    # Sent the cookie set through the environment variable to get this
    #input = requests.get("https://adventofcode.com/2018/day/8/input")

    # Hard Coded inputs
    input = open("121.example","r").read()
    input = input.split("\n")
    generation_one = input[0].strip("initial state:").strip()
    notes = input[2:]
    notes_ = {}
    for note in notes:
        if note:
            note = note.split("=>")
            notes_[note[0].strip()] = note[1].strip()
    #print generation_one, notes_
    print generation(generation_one, notes_)
    #print "Day 12: Part 1 answer is --> " + str(count)
    #print "Day 12: Part 2 answer is --> " + id

main()
