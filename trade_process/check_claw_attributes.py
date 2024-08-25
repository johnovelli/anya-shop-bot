from capture.capture_attributes import capture_claw_attributes, att_screenshot
from capture.img_to_string import imgToString
from config.get_config_values import get_params
from trade_process.item_dictionary import skills_lines, more_skill_lines, has_skill_lines


#  Checks if the claw attributes meet the criteria for purchase.
def checkClawAttributes():

    more_skill = False
    has_skill = False

    # Get minimum skill and has-skill parameters from configuration
    min_skill = int(get_params()['min_skill'])
    min_has_skill = int(get_params()['min_has_skill'])

    # Define the ranges for skill levels and presence of skills
    skill_range = list(range(min_skill, 4))
    has_skill_range = list(range(min_has_skill, 4))

    # Convert claw attributes image to a list of text lines
    lines, attributes_img = imgToString(capture_claw_attributes)

    # Iterate over each line of attributes
    for line in lines:
        line = line.lower()  # Convert the line to lowercase

        # Check if the line contains any skill information, excluding certain cases
        if any(skill in line for skill in skills_lines) and '(assassin @nly)' != line:
            # Check if the skill level is within the desired range
            is_skill_range = (any(str(num) in line for num in skill_range))
            if (any(more_skill in line for more_skill in more_skill_lines)
                    and is_skill_range):
                print('')
                print(f'Traps or assassin skills: {line}')  # Message indicating the presence of relevant skills
                att_screenshot('claws', attributes_img)  # Capture a screenshot of the attributes
                more_skill = True

            # Check if the has-skill level is within the desired range
            is_has_skill_range = (any(str(num) in line for num in has_skill_range))
            if (any(has_skill in line for has_skill in has_skill_lines)
                    and is_has_skill_range):
                print('')
                print(f'Lightning Sentry skills: {line}')  # Message indicating the presence of Lightning Sentry skills
                att_screenshot('claws', attributes_img)  # Capture a screenshot of the attributes
                has_skill = True

    # Return True if both criteria (more skill and has skill) are met
    if more_skill and has_skill:
        print('')
        print('50x jah!')
        return True

    return False