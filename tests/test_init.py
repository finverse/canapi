
import os

import canapi as cp
from canapi.client import ClientAPI


def test_from_config():
    httpbin = cp.from_config({
        "name": "httpbin",
        "uri": "https://httpbin.org",
        "endpoints": {
            "get_anything": {
                "method": "GET",
                "path": "/anything"
            }
        }
    })
    assert httpbin


def test_polygon():
    polygon = cp.api("polygon")
    assert polygon


def test_estimize():
    estimize = cp.api("estimize")
    assert estimize


def test_iex():
    iexcloud = cp.api("iexcloud")
    assert iexcloud


def test_coinbasepro():
    cbpro = cp.api("coinbasepro")


def test_alpaca():

    live = cp.api("alpaca", version="live")
    assert live
    assert "alpaca:live" in ClientAPI.apis

    paper = cp.api("alpaca", version="paper")
    assert paper
    assert "alpaca:paper" in ClientAPI.apis
