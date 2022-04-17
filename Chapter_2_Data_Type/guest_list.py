guests = ['dad','mom','cesar','saulin', 'marilu']
message = ", I hope you are fine, I am inviting you to a dinner this night at 8pm in my home."

print (f"{guests[0].title()}{message}")
print (f"{guests[1].title()}{message}")
print (f"{guests[2].title()}{message}")
print (f"{guests[3].title()}{message}")
print (f"{guests[4].title()}{message}")

print(f"{guests[2].title()} and {guests[-1].title()} said they can't assist\n\n")

guests.remove('cesar')
guests.remove('marilu')

guests.append('pandilla')
guests.append('nicole')

print (f"{guests[0].title()}{message}")
print (f"{guests[1].title()}{message}")
print (f"{guests[2].title()}{message}")
print (f"{guests[3].title()}{message}")
print (f"{guests[4].title()}{message}")

print("\nHey, I found a bigger table, I am inviting more people\n")

guests.insert(0,'pame')
guests.insert(2, 'pancho')
guests.append('marco')

print (f"{guests[0].title()}{message}")
print (f"{guests[1].title()}{message}")
print (f"{guests[2].title()}{message}")
print (f"{guests[3].title()}{message}")
print (f"{guests[4].title()}{message}")
print (f"{guests[5].title()}{message}")
print (f"{guests[6].title()}{message}")
print (f"{guests[7].title()}{message}")

print(f"Total of guests: {len(guests)}")


print("\nSorry sir, the table wont be able on time, there is just two chairs\n")

popped_person = guests.pop()
print(f"I am so sorry, but I can't invite you to the dinner {popped_person.title()}\n")

popped_person = guests.pop()
print(f"I am so sorry, but I can't invite you to the dinner {popped_person.title()}\n")

popped_person = guests.pop()
print(f"I am so sorry, but I can't invite you to the dinner {popped_person.title()}\n")

popped_person = guests.pop()
print(f"I am so sorry, but I can't invite you to the dinner {popped_person.title()}\n")

popped_person = guests.pop()
print(f"I am so sorry, but I can't invite you to the dinner {popped_person.title()}\n")

popped_person = guests.pop()
print(f"I am so sorry, but I can't invite you to the dinner {popped_person.title()}\n")

print(f"{guests[0].title()}, you are still invited, please confirm your attendence")
print(f"{guests[1].title()}, you are still invited, please confirm your attendence")

del guests[1]
del guests[0]

print(guests)