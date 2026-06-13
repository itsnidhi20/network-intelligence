from pyvis.network import Network
import tempfile


def create_interactive_graph(G):

    net = Network(
        height="700px",
        width="100%",
        bgcolor="#ffffff",
        font_color="black"
    )

    net.from_nx(G)

    net.repulsion(
        node_distance=200,
        spring_length=200
    )

    temp_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".html"
    )

    net.save_graph(temp_file.name)

    return temp_file.name