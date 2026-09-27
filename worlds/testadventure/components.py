from worlds.LauncherComponents import Component, Type, components, launch


def run_client(*args: str) -> None:

    from .client.launch import launch_ta_client


    launch(launch_ta_client, name="Test Adventure Client", args=args)



components.append(
    Component(
        "Test Adventure Client",
        func=run_client,
        game_name="Test Adventure",
        component_type=Type.CLIENT,
        supports_uri=True,
    )
)