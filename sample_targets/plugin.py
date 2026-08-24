"""Sample plugin registering extra targets and a theme"""


def register(api):
    # register an extra target
    api.register_target(
        "steam_store",
        type(
            "Spec",
            (object,),
            {"name": "steam_store", "sizes": [460], "formats": ["png"], "notes": "Steam store large image"},
        ),
    )
