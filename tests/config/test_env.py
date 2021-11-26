import piter.config

def test_default():
    env_config = piter.config.models.EnvConfig()
    
    for key, value in piter.config.default.DEFAULT_CONFIG_ENV.items():
        assert env_config.__getattribute__(key) == value