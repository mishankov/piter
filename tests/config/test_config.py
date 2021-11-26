import piter.config

def test_default():
    config = piter.config.Config({})
    
    for key, value in piter.config.default.DEFAULT_CONFIG_PITER.items():
        assert config.__getattribute__(key) == value