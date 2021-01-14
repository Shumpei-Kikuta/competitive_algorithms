def pytest_addoption(parser):
    parser.addoption("--file", action="store")
    parser.addoption("--range", action="store")
