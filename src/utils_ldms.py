
def get_seniority_level(years):
    """
    Determines the seniority level based on the number of years of experience.
    
    Parameters:
        years (int): The number of years of experience.
        
    Returns:
        str: The seniority level based on the number of years of experience.
            Possible values are 'Junior', 'Mid', 'Senior', or 'Expert'.
    """
    output = 'Expert'
    if years <= 3:
        output = 'Junior'
    else:
        if years <= 5:
            output = 'Mid'
        else:
            if years <= 10:
                output = 'Senior'
    return output
