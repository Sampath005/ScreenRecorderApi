from dotenv import load_dotenv, find_dotenv
from flask import Blueprint, json, Response, url_for, render_template, redirect
from ..Core.screenshot_to_doc import ScreenshotToDoc
import threading

load_dotenv(find_dotenv())

screenshot_api = Blueprint('screenshot_api', __name__)

screenshot_to_doc = ScreenshotToDoc()


@screenshot_api.route('/start', methods=['GET'])
def start_screenshot_listener():
    if screenshot_to_doc.listener is None or not screenshot_to_doc.listener.running:
        listener_thread = threading.Thread(target=screenshot_to_doc.start())
        listener_thread.start()
        return custom_response('Screenshot listener started', 200)
    return custom_response('Screenshot listener is already running', 400)


@screenshot_api.route('/stop', methods=['GET'])
def stop_screenshot_listener():
    if screenshot_to_doc.listener is not None and screenshot_to_doc.listener.running:
        screenshot_to_doc.stop()
        screenshot_to_doc.save_and_cleanup()
        return custom_response('Screenshot listener stopped and document saved', 200)
    return custom_response('Screenshot listener is not running', 400)


@screenshot_api.route('/status', methods=['GET'])
def status():
    return custom_response('running' if screenshot_to_doc.listener.running else 'stopped', 200)


def custom_response(res, status_code):
    """
  Custom Response Function
  """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
