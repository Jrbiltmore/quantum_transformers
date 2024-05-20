import yaml

def load_config(config_file='config/config.yaml'):
    """
    Load configuration from a YAML file.

    Args:
        config_file (str): Path to the config file.

    Returns:
        dict: Configuration dictionary.
    """
    try:
        with open(config_file, 'r') as file:
            config = yaml.safe_load(file)
        return config
    except Exception as e:
        print(f"Failed to load configuration: {e}")
        return None

# END