from datetime import datetime
from capture.capture_attributes import capture_claw_attributes
from capture.img_to_string import imgToString


def checkClawAttributes():
    has_more_skill = False
    has_skill = False

    lines, attributes_img = imgToString(capture_claw_attributes)
    for line in lines:
        line = line.lower()

        skills_lines = ['assassin', 'assa', 'sin', 'nly', 'll', 'skill']
        more_skill_lines = ['traps', 'skill']
        l_sentry_skill_lines = ['lightning', 'ning sentry']

        if (any(skill in line for skill in skills_lines)) and '(assassin @nly)' != line:
            if any(more_skill in line for more_skill in more_skill_lines) and ('2' in line or '3' in line):
                print(f'Skills1: {line}')
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                attributes_img.save(f'imgs/logs/claws/{timestamp}.jpg')
                has_more_skill = True

            if any(l_sentry_skill in line for l_sentry_skill in l_sentry_skill_lines) and ('2' in line or '3' in line):
                print(f'Skills2: {line}')
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                attributes_img.save(f'imgs/logs/claws/{timestamp}.jpg')
                has_skill = True

    if has_more_skill and has_skill:
        return True

    return False
