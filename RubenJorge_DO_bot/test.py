import sys
sys.path.append('.')
from botlib import check_service_web, check_port, check_code
import pytest


def test_check_port():
    print("Testing check_port with expected success...")
    assert check_port("http://google.com", 80) == True
    print("Success case passed.")


def test_check_port():
    print("Testing check_port with expected failure...")
    assert check_port("http://example.com", 9999) == False
    print("Failure case passed.")

def test_check_service_web():
    print("Testing check_service_web with a running service...")
    assert check_service_web("https://google.com") == True
    print("Running service case passed.")


def test_check_service_webl():
    print("Testing check_service_web with a non-running service...")
    assert check_service_web("http://0.0.0.0.com") == False



def test_check_code():
    print("Testing check_code with a status 200 response...")
    assert check_code("http://google.com") == True
    print("Status 200 case passed.")


def test_check_code():
    print("Testing is_http_200_ok with a non-200 status response...")
    assert check_code("http://example.com") == False
    print("Non-200 status case passed.")