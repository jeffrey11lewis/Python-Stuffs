import random
random.seed()

def did_anyone_have_a_birthday_match(people_in_room):
    birthdays_in_room = []
    for index in range(people_in_room):
        my_birthday = random.randint(1, 367)
        birthdays_in_room.append(my_birthday)

    birthdays_in_room_set = set(birthdays_in_room)
    if (len(birthdays_in_room_set) != len(birthdays_in_room)):
        return True
    else:
        return False


if __name__ == '__main__':
    people_in_room = 23
    repeat_size = 6
    match_count = 0
    sample_size = 100000
    percent_list = []
    for index in range(repeat_size):
        match_count = 0
        percent_match = 0
        for index in range(sample_size):
            we_had_a_match =  did_anyone_have_a_birthday_match(people_in_room)
            if(we_had_a_match):
                match_count += 1
                percent_match = (match_count / sample_size) *100
                percent_to_average = (match_count / sample_size)
                percent_formatted = "{:.2f}".format(percent_match)
        print('out of a sample size of {}, we had {} matches, or {}% '.format(sample_size, match_count, percent_formatted))
        percent_list.append(percent_to_average)
        average_of_repeats = (sum(percent_list) / len(percent_list)) * 100
        average_of_repeats_formatted = "{:.2f}".format(average_of_repeats)
    print('the average of the {} runs is {}%'.format(repeat_size, average_of_repeats_formatted))