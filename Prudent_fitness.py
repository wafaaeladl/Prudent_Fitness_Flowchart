print("Welcome to the Prudent Fitness planning process!")

community_needs_gym = input(
  "Does the community need this type of gym? (yes/no): "
).strip().lower()

if community_needs_gym == "no":
  print("Ask people what they want in a gym.")
  print("Review their feedback and improve the idea.")

elif community_needs_gym == "yes":
  print("choose the gym's services and membership options.")

can_afford = input(
  "Can the business afford the location, equipment, and staff? (yes/no): "
).strip().lower()

  if can_afford == "yes":
    print("Prepare to open Prudent Fitness.")
    print("Open Prudent Fitness and welcome the members.")

  elif can_afford == "no"
    print("Look for a cheaper location, more funding, or fewer services.")
    print("Review the plan and check the costs again.")

  else:
    print("Please enter yes or no.")

else:
  print("Please enter yes or no.")

