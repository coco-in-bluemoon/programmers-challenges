import re


def extract_page_by_tag(page, tag):
    start_tag = f'<{tag}>'
    end_tag = f'</{tag}>'

    start_index = page.find(start_tag) + len(start_tag)
    end_index = page.find(end_tag)

    page_by_tag = page[start_index:end_index]
    page_by_tag = re.sub(r'[\s][\s]+', '', page_by_tag)
    page_by_tag = re.sub(r'^[\s]', '', page_by_tag)
    page_by_tag = re.sub(r'[\s]$', '', page_by_tag)

    return page_by_tag


def extract_link_from_head(page):
    pattern = r'<meta property="og:url" content="(https://.*?)"'
    link = re.search(pattern, page)
    return link.group(1)


def calculate_base_score(word, page):
    return re.sub(r'[^a-z]', '.', page).split('.').count(word)


def extract_outer_links(page):
    pattern = r'<a href="(https://.*?)"'
    outer_links = re.findall(pattern, page)
    return outer_links


def solution(word, pages):
    head_pages = list()
    body_pages = list()

    for page in pages:
        page = page.lower()
        page_head = extract_page_by_tag(page, 'head')
        page_body = extract_page_by_tag(page, 'body')

        head_pages.append(page_head)
        body_pages.append(page_body)

    link2page = dict()
    for page_id, page in enumerate(head_pages):
        link = extract_link_from_head(page)
        link2page[link] = page_id

    base_scores = list()
    word = word.lower()
    for page in body_pages:
        base_score = calculate_base_score(word, page)
        base_scores.append(base_score)

    scores = [score for score in base_scores]
    for page_id, page in enumerate(body_pages):
        outer_links = extract_outer_links(page)
        n_links = len(outer_links)
        for outer_link in outer_links:
            if outer_link in link2page:
                target_page_id = link2page[outer_link]
                scores[target_page_id] += (base_scores[page_id] / n_links)
    max_score = max(scores)
    return scores.index(max_score)


if __name__ == "__main__":
    word = "blind"
    pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
    assert solution(word, pages) == 0

    word = "Muzi"
    pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
    assert solution(word, pages) == 1
