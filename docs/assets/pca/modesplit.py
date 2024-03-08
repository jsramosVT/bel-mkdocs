## Revised by Jay McDonald-Ramos (March 2024)

## This script is meant to be used in PyMOL.
## This script requires modevectors.py, which you can retrieve from http://www.pymolwiki.org/index.php/Modevectors
## You can run this script via File > Run Script and navigating to modesplit.py OR by entering the following in the PyMOL terminal: run modesplit.py
import pymol

# Preset for ray-traced visualization - OPTIONAL.
cmd.set("ray_trace_mode", "1")
cmd.set("ray_shadow", "0")
cmd.set("fog", "0.5")

# CHAINS - Define protein subunits here. Minimum 1 required.
chains = [
    {
        "id" : "A",
        "start_index" : 1, # Index of first ATOM (not amino acid)
        "end_index" : 1191 # Index of last ATOM (not amino acid)
    },
    {
        "id" : "B",
        "start_index" : 1195,
        "end_index" : 2383
    },
    {
        "id" : "C",
        "start_index" : 2392,
        "end_index" : 3582
    }
]

# Split frames and hide original object
cmd.do("split_states all")
cmd.disable("*_ev")

for chain in chains:
    # Selects residues in first frame
    cmd.select("sele", selection = f"index {chain['start_index']}-{chain['end_index']} and *ev_0001")
    cmd.create(f"f1{chain['id']}","%sele")

    # Selects residues in second frame
    cmd.select("sele", selection = f"index {chain['start_index']}-{chain['end_index']} and *ev_0002")
    cmd.create(f"f2{chain['id']}","%sele")

    # Run modevectors.py and group frames
    cmd.do("run modevectors.py")
    cmd.do(f"modevectors f1{chain['id']},f2{chain['id']}, skip=0, headrgb=(1.0,1.0,1.0), tailrgb=(1.0,1.0,1.0)") # Parameters for modevectors viz - see http://www.pymolwiki.org/index.php/Modevectors for more info
    cmd.show(representation="cartoon",selection = f"f2{chain['id']}")

    # Rename modevectors object and groups related chain objects
    try:
        cmd.set_name("modevectors", f"mv{chain['id']}")
    except:
        pass # If no modevectors object, do not attempt to rename
    cmd.group(f"ch{chain['id']}", members = f"*{chain['id']}")

cmd.ungroup("%sele") # Final atom selection will sometimes be grouped by accident