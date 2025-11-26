def filtering_proccess(domain_for_filter, keywords_list_for_check):
    is_match = False
    match_list = []
    for keyword in keywords_list_for_check:
        if domain_for_filter in keyword:
            is_match = True
            match_list.append(keyword)

    return is_match, match_list
