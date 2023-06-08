#!/usr/bin/env python3

import webview
from server import app

import os
import multiprocessing

from arknights_mower.utils.conf import load_conf, save_conf


def start_server(app, port):
    app.run(host="127.0.0.1", port=port)


def on_resized(w, h):
    global width
    global height

    width = w
    height = h


if __name__ == "__main__":
    multiprocessing.freeze_support()

    conf = load_conf()

    port = conf["webview"]["port"]

    global width
    global height

    width = conf["webview"]["width"]
    height = conf["webview"]["height"]

    window = webview.create_window(
        "Mower Web UI in WebView (尚不完善，测试用途，谨慎使用)",
        f"http://127.0.0.1:{port}",
        width=width,
        height=height,
    )

    window.events.resized += on_resized

    webview.start(start_server, (app, port))


    conf = load_conf()
    conf["webview"]["width"] = width
    conf["webview"]["height"] = height
    save_conf(conf)

    os._exit(0)
