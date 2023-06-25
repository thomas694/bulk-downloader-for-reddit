#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Optional

from praw.models import Submission

from bdfr.configuration import Configuration
from bdfr.resource import Resource
from bdfr.site_authenticator import SiteAuthenticator
from bdfr.site_downloaders.base_downloader import BaseDownloader


class Direct(BaseDownloader):
    def __init__(self, post: Submission, args: Configuration):
        super().__init__(post, args)

    def find_resources(self, authenticator: Optional[SiteAuthenticator] = None) -> list[Resource]:
        return [Resource(self.post, self.post.url, Resource.retry_download(self.post.url))]
