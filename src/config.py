def config_params(config_type="dev"):
    
    if config_type == "dev":
        params = {}

        params["W_button"] = 0
        params["H_button"] = 125

        params["font_name"] = "calibre"
        params["font_size"] = 10
        params["font_type"] = "normal"

        params["x_entry_offset"] = 230
        params["y_entry_offset"] = 25
        params["x_entry_button_offset"] = 80
        params["y_entry_button_offset"] = 22

        params["x_button_offset"] = 70
        params["y_button_offset"] = 22

    return params
