from parsl.tests.utils import get_rundir

config = {
    "sites": [
        {
            "site": "local_threads",
            "auth": {
                "channel": None
            },
            "execution": {
                "executor": "threads",
                "provider": None,
                "maxThreads": 2,
            }
        }
    ],
    "globals": {
        "lazyErrors": True,
        "memoize": True,
        'runDir': get_rundir()
    }
}
