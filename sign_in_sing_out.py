logs = [
"17 20 sign-in",
"17 79 sign-out",
"15 11 sign-out",
"13 78 sign-in",
"10 120 sign-in",
"13 79 sign-out",
"10 128 sign-out",
]

expected_output = []  #["10", "13"]
# user_id time_in_seconds event
# 20 sec
diff = -1
events_dict = {}
for i in logs:
    lst = i.split()[0:2]
    # print(lst, events_dict.keys())
    if int(lst[0]) in events_dict.keys():
        diff = abs(events_dict[int(lst[0])]-int(lst[1]))
        del events_dict[int(lst[0])]
        if diff < 20:
            expected_output.append(lst[0])
    else:
        events_dict[int(lst[0])] = int(lst[1])

    # print(events_dict)
    # print(expected_output)

print(sorted(expected_output))
