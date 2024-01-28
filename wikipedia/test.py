import os
# os.environ["http_proxy"] = "http://127.0.0.1:10080"
# os.environ["https_proxy"] = "http://127.0.0.1:10080"

import wikipediaapi
# wiki_wiki = wikipediaapi.Wikipedia('zh')

wiki_wiki = wikipediaapi.Wikipedia('User-Agent: CoolBot/0.0 (https://example.org/coolbot/; coolbot@example.org) generic-library/0.0', language='zh')
print(wiki_wiki.language)
a =wiki_wiki.page("广东省1")
print(f"Data is exist: {a.exists()}")
print(a.summary)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
