from random import choices, randint


rating_list = choices(range(1, 10), k=randint(0, 10))
rating_list.sort(reverse=True)

print('Current rating:', rating_list)

while (user_input := input('Input a new natural number: ')).isdigit():
    user_num = int(user_input)

    if not rating_list:
        rating_list.append(user_num)
    else:
        if rating_list[0] <= user_num:
            index = 0
        elif rating_list[-1] >= user_num:
            index = len(rating_list)
        else:
            left, right = 0, len(rating_list)
            middle = (left + right) // 2

            # `middle` will be an index to insert `user_num`,
            # so in the resulting list it will looks like
            # [.., rating_list[middle - 1], user_num, rating_list[middle], ..]

            # Do body while
            #   `user_num < rating_list[middle]`
            # or
            #   `rating_list[middle - 1] > user_num`
            # changing borders and middle point
            while True:
                if user_num > rating_list[middle - 1]:
                    right, middle = middle, (middle + left) // 2
                elif user_num < rating_list[middle]:
                    left, middle = middle, (middle + right) // 2
                else:
                    break
            index = middle

        rating_list.insert(index, user_num)

    print('\nCurrent rating:', rating_list)


# # Next code is more obvious and simple,
# # but also more expensive for a long list,
# # because of a sorting
#
# while (user_input := input('Input a new natural number: ')).isdigit():
#     user_num = int(user_input)
#
#     rating_list.append(user_num)
#     rating_list.sort(reverse=True)

