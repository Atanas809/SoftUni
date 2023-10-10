from django.core.exceptions import ValidationError


def possible_relations(animal_type):
    if animal_type.animal_set.count() > 2:
        raise ValidationError(f'Type {animal_type.name} cannot have more than 2 relations')
