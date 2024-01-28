import wikipediaapi

WIKI_DEFAULT_USER_AGENT = 'User-Agent: CoolBot/0.0 (https://example.org/coolbot/; coolbot@example.org) generic-library/0.0'


class PageObject:

    def __init__(self, title, language, sections=None, **kwargs):
        summary = kwargs.pop("summary", None)
        self.text = kwargs.pop("text", None)
        self.title = title
        self.language = language
        self.sections = sections
        self.summary = summary

    def __str__(self):
        return f"PageObject(title={self.title},text={self.text},summart={self.summary})"
class WekipediaTool:
    def __init__(self, language="zh", user_agent=WIKI_DEFAULT_USER_AGENT):
        self.handle = wikipediaapi.Wikipedia(user_agent, language='zh')

    def get_page(self, keyword):
        """
        >>> self.get_page("广东省1") is None
        :param keyword:
        :return:
        """
        page = self.handle.page(keyword)
        if not page.exists():
            return None
        return PageObject(title=page.title,
                          summary=page.summary,
                          text=page.text,
                          language=page.language
                          )
