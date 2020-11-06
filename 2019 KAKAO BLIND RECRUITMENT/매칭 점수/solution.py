import enum
import re
from re import sub


def extract_page_by_tag(page, tag):
    assert tag in ['head', 'body']

    start_tag = f'<{tag}>'
    end_tag = f'</{tag}>'

    start_index = page.find(start_tag) + len(start_tag)
    end_index = page.find(end_tag)

    subpage = page[start_index:end_index]
    subpage = re.sub(r'[\s][\s]+', ' ', subpage)
    subpage = re.sub(r'^[\s]', '', subpage)
    subpage = re.sub(r'[\s]$', '', subpage)

    return subpage


def extract_link_from_head(page):
    pattern = r'<meta property="og:url" content="(https://[^\s]+)"[\s]?/>'
    matched_expression = re.search(pattern, page)
    link = matched_expression.group(1)
    return link


def extract_outer_link_from_body(page):
    pattern = r'<a href="(https://[^\s]+)"[\s]?>'
    outer_links = re.findall(pattern, page)
    return outer_links


def count_word_in_body(word, page):
    page = re.sub(r'[^a-z]', '.', page)
    return page.split('.').count(word)


def solution(word, pages):
    word = word.lower()
    head_pages = list()
    body_pages = list()
    for page in pages:
        page = page.lower()
        head_page = extract_page_by_tag(page, 'head')
        body_page = extract_page_by_tag(page, 'body')

        head_pages.append(head_page)
        body_pages.append(body_page)

    link2page = dict()
    for idx, page in enumerate(head_pages):
        link = extract_link_from_head(page)
        link2page[link] = idx

    base_scores = list()
    for page in body_pages:
        base_score = count_word_in_body(word, page)
        base_scores.append(base_score)

    scores = [score for score in base_scores]
    for idx, page in enumerate(body_pages):
        outer_links = extract_outer_link_from_body(page)
        n_links = len(outer_links)
        for outer_link in outer_links:
            if outer_link not in link2page:
                continue
            target_page = link2page[outer_link]
            scores[target_page] += (base_scores[idx] / n_links)

    max_score = max(scores)
    answer = scores.index(max_score)
    return answer


if __name__ == "__main__":
    word = "blind"
    pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
    assert solution(word, pages) == 0

    word = "Muzi"
    pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
    assert solution(word, pages) == 1
