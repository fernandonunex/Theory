def build_profile(first, last, **user_info):
    """Build a dictionary containin everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('Fer', 'Nunex',
                              eyes_color = 'Brown',
                              laptop = 'OMEN HP',
                              drink = 'Red Bull')

print(user_profile)

