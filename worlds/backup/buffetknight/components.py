from worlds.LauncherComponents import Component, Type, components, launch


def run_client(*args: str) -> None:

    from .client.launch import launch_bk_client


    launch(launch_bk_client, name="Buffet Knight Client", args=args)



components.append(
    Component(
        "Buffet Knight Client",
        func=run_client,
        game_name="Buffet Knight",
        component_type=Type.CLIENT,
        supports_uri=True,
    )
)