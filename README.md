# app-freesurfer-agg

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

**Aggregates FreeSurfer statistics across subjects, computing group mean and standard deviation of aseg volumes and of aparc thickness, gray matter volume and surface area, and shows them as bar plots.**

Reads stats/aseg.stats and lh/rh.aparc.stats from each FreeSurfer input and writes product.json with bar plots of the across-subject mean and standard deviation per structure (voxel count, volume, normalised intensity, cortical thickness, gray matter volume and surface area). Use it for a quick visual group summary of FreeSurfer outputs on brainlife; it produces no output datasets. Needs several FreeSurfer outputs.

Run it on brainlife.io: [https://doi.org/10.25663/bl.app.94](https://doi.org/10.25663/bl.app.94)

| Input | Datatype | Required | Description |
|---|---|---|---|
| `freesurfer` | `neuro/freesurfer` | yes | FreeSurfer subject directories (one per subject) whose stats/aseg.stats and stats/lh\|rh.aparc.stats files are aggregated. |

Runtime: container `brainlife/mcr:neurodebian1604-r2017a`; 1 CPUs.

<!-- brainlife-app:end -->

Do some basic group analysis on freesurfer output
