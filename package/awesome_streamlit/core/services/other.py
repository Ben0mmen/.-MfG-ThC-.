"""Organizes and shares business logic, data and functions with different
pages of the Streamlit App.

  - Database interactions: Select, Insert, Update, Delete
  - REST API interactions, get, post, put, delete
  - Pandas transformations
"""
import logging
import urllib.request
from typing import Optional

import streamlit as st


@st.cache
def get_file_content_as_string(url: str) -> str:
    """The url content as a string

    Arguments:
        url {str} -- The url to request

    Returns:
        str -- The text of the url
    """
    data = urllib.request.urlopen(url).read()
    return data.decode("utf-8")


@st.cache
def set_logging_format(
    logging_formatter: Optional[str] = "%(asctime)s %(name)s: %(message)s"
) -> bool:
    """Sets the format of all 'streamlit' loggers

    Keyword Arguments:
        format {object} -- The formatter to apply (default: {"%(asctime)s %(name)s: %(message)s"})

    Returns:
        bool -- True
    """
    loggers = [
        name
        for name in logging.root.manager.loggerDict  # type: ignore
        if name.startswith("streamlit")
    ]
    formatter = logging.Formatter(logging_formatter)
    for name in loggers:
        logger = logging.getLogger(name)
        for handler in logger.handlers:
            handler.setFormatter(formatter)
    return True
