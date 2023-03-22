train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

def f_to_c(f_temp):
    return (f_temp - 32) * 5/9
print(f_to_c(47))

def get_force(mass, acceleration):
    return mass * acceleration
train_force = get_force(train_mass, train_acceleration)
print(train_force)
print