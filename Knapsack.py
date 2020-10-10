# 0-1 Knapsack Problem solved using Genetic Algorithms
# Sai Vikram Patnaik


import random

class Item(object):
    def __init__(self, v, w):
        self.value = v 
        self.weight = w 



ITEMS = [Item(random.randint(0,30),random.randint(0,30)) for x in range (0,30)]


CAPACITY = 10*len(ITEMS)


POP_SIZE = 30


GEN_MAX = 10


def fitness(target):
    """
    fitness(target) will return the fitness value of permutation named "target".
    Higher scores are better and are equal to the total value of items in the permutation.
    If total_weight is higher than the capacity, return 0 because the permutation cannot be used.
    """
    total_value = 0
    total_weight = 0
    index = 0
    for i in target:        
        if index >= len(ITEMS):
            break
        if (i == 1):
            total_value += ITEMS[index].value
            total_weight += ITEMS[index].weight
        index += 1
        
    
    if total_weight > CAPACITY:
        return 0
    else:
        return total_value

def spawn_starting_population(amount):
    return [spawn_individual() for x in range (0,amount)]

def spawn_individual():
    return [random.randint(0,1) for x in range (0,len(ITEMS))]

def mutate(target):
    """
    Changes a random element of the permutation array from 0 -> 1 or from 1 -> 0.
    """ 
    r = random.randint(0,len(target)-1)
    if target[r] == 1:
        target[r] = 0
    else:
        target[r] = 1

def evolve_population(pop):
    parent_eligibility = 0.2
    mutation_chance = 0.08
    parent_lottery = 0.05

    parent_length = int(parent_eligibility*len(pop))
    parents = pop[:parent_length]
    nonparents = pop[parent_length:]

    # Parent Selection (Random)
    for np in nonparents:
        if parent_lottery > random.random():
            parents.append(np)

    # Mutation (Random)
    for p in parents:
        if mutation_chance > random.random():
            mutate(p)

    # Crossover
    children = []
    desired_length = len(pop) - len(parents)
    while len(children) < desired_length :
        male = pop[random.randint(0,len(parents)-1)]
        female = pop[random.randint(0,len(parents)-1)]        
        half = int(len(male)/2)
        child = male[:half] + female[half:] # from start to half from father, from half to end from mother
        if mutation_chance > random.random():
            mutate(child)
        children.append(child)

    parents.extend(children)
    return parents

def main():
    print("Capacity:",CAPACITY ,"\nOriginal values :\n")
    print("value-------weight")
    for i in ITEMS:
        print("(",i.value,"  ,  ",i.weight,')')
    print("\n\n")
    generation = 1
    population = spawn_starting_population(POP_SIZE)
    for g in range(0,GEN_MAX):
        print ("Generation %d with %d" % (generation,len(population)))
        population = sorted(population, key=lambda x: fitness(x), reverse=True)
        for i in population:        
            print ("%s, fit: %s" % (str(i), fitness(i)))        
        population = evolve_population(population)
        generation += 1

if __name__ == "__main__":
    main()
