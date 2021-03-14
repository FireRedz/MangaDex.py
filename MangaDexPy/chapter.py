class Chapter:
    __slots__ = ("id", "hash", "manga_id", "manga_title", "volume", "chapter", "title", "language", "groups",
                 "uploader", "timestamp", "thread", "views", "pages", "server", "fallback_server", "server_status",
                 "session")

    def __init__(self, data, session):
        self.id = data["id"]
        self.hash = data["hash"]
        self.manga_id = data["mangaId"]
        self.manga_title = data["mangaTitle"]
        self.volume = data["volume"]
        self.chapter = data["chapter"]
        self.title = data["title"]
        self.language = data["language"]
        self.groups = data["groups"]
        self.uploader = data["uploader"]
        self.timestamp = data["timestamp"]
        self.thread = data["threadId"]
        self.views = data["views"]
        self.pages = data["pages"]
        self.server = data["server"]
        self.fallback_server = data["serverFallback"]
        self.server_status = data["status"]
        self.session = session

    def get_page(self, page, fallback=False):
        if fallback:
            return self.fallback_server + self.hash + "/" + self.pages[page]
        else:
            return self.server + self.hash + "/" + self.pages[page]

    def format_url(self, img, fallback=False):
        if fallback:
            return self.fallback_server + self.hash + "/" + img
        else:
            return self.server + self.hash + "/" + img

    def refresh(self):
        p = {"saver": "data-saver" in self.server, "mark_read": False}
        req = self.session.get("https://api.mangadex.org/v2/chapter/{}".format(self.id), params=p)
        if req.status_code == 200:
            data = req.json()["data"]
            self.pages = data["pages"]
            self.server = data["server"]
            self.fallback_server = data["serverFallback"]