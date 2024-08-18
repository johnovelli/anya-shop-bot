from capture.capture_attributes import capture_claw_attributes, att_screenshot
from capture.img_to_string import imgToString
from config.get_config_values import get_params
from trade_process.item_dictionary import skills_lines, more_skill_lines, has_skill_lines


def checkClawAttributes():

    more_skill = False
    has_skill = False

    min_skill = int(get_params()['min_skill'])
    min_has_skill = int(get_params()['min_has_skill'])

    skill_range = list(range(min_skill, 4))
    has_skill_range = list(range(min_has_skill, 4))

    lines, attributes_img = imgToString(capture_claw_attributes)

    for line in lines:
        line = line.lower()

        if any(skill in line for skill in skills_lines) and '(assassin @nly)' != line:

            is_skill_range = (any(str(num) in line for num in skill_range))
            if (any(more_skill in line for more_skill in more_skill_lines)
                    and is_skill_range):
                print(f'Traps or assassin skills: {line}')
                att_screenshot('claws', attributes_img)
                more_skill = True

            is_has_skill_range = (any(str(num) in line for num in has_skill_range))
            if (any(has_skill in line for has_skill in has_skill_lines)
                    and is_has_skill_range):
                print(f'Lightning Sentry skills: {line}')
                att_screenshot('claws', attributes_img)
                has_skill = True

    if more_skill and has_skill:
        print('50x jah!')
        return True

    return False
