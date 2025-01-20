import os
import toml


class ConfigManager:
    def __init__(self):
        self.config = None
        self.config_path = self.get_config_path()

    def get_config_path(self):
        config_dir = os.getenv("XDG_CONFIG_HOME", os.path.expanduser("~/.config"))
        app_config_dir = os.path.join(config_dir, "dotsy")
        os.makedirs(app_config_dir, exist_ok=True)
        return os.path.join(app_config_dir, "config.toml")

    @property
    def get_config(self):
        # Load the configuration lazily
        if self.config is None:
            if os.path.exists(self.config_path):
                with open(self.config_path, "r") as file:
                    self.config = toml.load(file)
            else:
                self.config = {}  # Initialize with an empty dictionary
        return self.config

    def save_config(self):
        # Ensure the configuration is loaded before saving
        if self.config is None:
            raise RuntimeError("Config has not been loaded yet. Call get_config first.")

        # Write the configuration back to the file
        with open(self.config_path, "w") as file:
            toml.dump(self.config, file)
