try:
    from gevent import monkey

    # monkey.patch_all()
except ImportError:
    # fine if no gevent is available
    pass
