from src.app import ColorWheel
from src.config import config_params

if __name__ == '__main__':

    params = config_params(config_type="dev")
    ColorWheel(params).run()
