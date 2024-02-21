# Miscellaneous functions

Annotations (1) differ from footnotes[^1] and can be used to add lil notes.
{ .annotate }

1. This is an annotation! (1)
    { .annotate }

    1. This is also an annotation 😲

[^1]: This is a footnote!

The documentation also has [some other cool useful things](https://squidfunk.github.io/mkdocs-material/reference/).

## Examples of Code
### Code blocks with syntax highlighting

```bash title="bash" linenums="1"
module load apps site/infer/easybuild/setup
module load CMake/3.15.3-GCCcore-8.3.0
module load CUDA/10.1.243-GCC-8.3.0
 
export MODULEPATH=$MODULEPATH:/projects/bevanlab/software/infer/modules/modules/infer-skylake/all
module load gromacs-v100/2020.4
```

```py title="python" linenums="1"
import matplotlib.pyplot as plt
import pandas as pd
from shapely import geometry, ops

def gather_data():
    ...

if __name__ == '__main__':
    gather_data()
```