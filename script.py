train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1
c = 3*10**8

def f_to_c(f_temp):
    return (f_temp - 32) * 5/9
print(f_to_c(47))

def get_force(mass, acceleration):
    return mass * acceleration
train_force = get_force(train_mass, train_acceleration)
print(train_force)
print("The GE train supplies " + str(train_force) + " Newtons of force.")

def get_energy(mass, c):
    return mass * c**2
bomb_energy = get_energy(bomb_mass, c)
print(bomb_energy)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

def get_work(mass, acceleration, distance):
    