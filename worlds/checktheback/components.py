from worlds.LauncherComponents import Component, Type, components, launch


def run_client(*args: str) -> None:

    from .client.launch import launch_ctb_client


    launch(launch_ctb_client, name="Check The Back Client", args=args)



components.append(
    Component(
        "Check The Back Client",
        func=run_client,
        game_name="Check The Back",
        component_type=Type.CLIENT,
        supports_uri=True,
    )
)
