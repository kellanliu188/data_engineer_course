class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  def __repr__(self):
    return f"Menu: {self.name} (Available: {self.start_time} to {self.end_time})"
  def calculate_bill(self, purchased_items):
    total_bill = 0
    for i in purchased_items:
      total_bill += self.items[i]
    return total_bill

brunch = Menu('Brunch', {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}, 11, 16)

early_bird = Menu('Early Bird', {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}, 15, 18)

dinner = Menu('Dinner', {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}, 17, 23)

kids = Menu('Kids', {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}, 11, 21)

arepas_menu = Menu("Take a' Arepa", {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}, 10, 20)

print(brunch)
total = brunch.calculate_bill(['pancakes', 'home fries', 'coffee'])
print(total)
total_early = early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)'])
print(total_early)


class Franchise():
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  
  def __repr__(self):
    return self.address
  def available_menus(self, time):
    available = [menu for menu in self.menus if menu.start_time <= time <= menu.end_time]
    return available
flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])

print(flagship_store.available_menus(17))
arepas_place = Franchise("189 Fitzgerald Avenue", arepas_menu)

class Business():
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

first_buisness = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
second_business = Business("Take a' Arepa", arepas_place)