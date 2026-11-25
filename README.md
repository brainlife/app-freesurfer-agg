<h1 align="center">FreeSurfer Group Analysis</h1>

<p align="center">
  Group bar plots of FreeSurfer aseg volumes and aparc thickness, gray matter volume and surface area, aggregated across subjects.
</p>

<p align="center">
  <a href="https://github.com/brainlife/abcd-spec"><img src="https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg" alt="ABCD Spec v1.1"></a>
  <a href="https://doi.org/10.25663/bl.app.94"><img src="https://img.shields.io/badge/Brainlife-bl.app.94-blue.svg" alt="Run on brainlife.io"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-lightgrey.svg" alt="MIT license"></a>
</p>

## 🧠 At a glance

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Aggregates FreeSurfer statistics across subjects, computing group mean and standard deviation of aseg volumes and of aparc thickness, gray matter volume and surface area, and shows them as bar plots.**

Reads stats/aseg.stats and lh/rh.aparc.stats from each FreeSurfer input and writes product.json with bar plots of the across-subject mean and standard deviation per structure (voxel count, volume, normalised intensity, cortical thickness, gray matter volume and surface area). Use it for a quick visual group summary of FreeSurfer outputs on brainlife; it produces no output datasets. Needs several FreeSurfer outputs.

| | |
|---|---|
| 📥 **Inputs** | `neuro/freesurfer` |
| 🐳 **Container** | `brainlife/mcr:neurodebian1604-r2017a` |
| ⚙️ **Resources** | 1 CPUs |
| 🔗 **Run it** | [doi.org/10.25663/bl.app.94](https://doi.org/10.25663/bl.app.94) |

#### 📥 Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `freesurfer` | `neuro/freesurfer` | yes | FreeSurfer subject directories (one per subject) whose stats/aseg.stats and stats/lh\|rh.aparc.stats files are aggregated. |

<!-- brainlife-app:end -->

## 🚀 Running the App

### ☁️ On brainlife.io

Open the App at [doi.org/10.25663/bl.app.94](https://doi.org/10.25663/bl.app.94), select several `neuro/freesurfer` datasets (one per subject) from your project and press **Execute**. The App reads each subject's `stats/aseg.stats`, `stats/lh.aparc.stats` and `stats/rh.aparc.stats` and shows the group summary as plots on the task page. It archives no datasets.

### 💻 Locally

The App runs `aggregate.py` directly, so you need Python with [NumPy](https://numpy.org/); no container is used.

1. Clone this repository.
2. Create `config.json` listing the FreeSurfer subject directories to aggregate (see `config.json.sample`):

   ```json
   {
       "outputs": [
           "testdata/full/sub-0001/output",
           "testdata/take2/sub-0001/output",
           "testdata/mix2/sub-0001/output"
       ]
   }
   ```

3. Run the App:

   ```bash
   ./main
   ```

## 📦 Outputs

`product.json` holds six Plotly bar plots, each showing the across-subject mean per structure with the standard deviation as error bars:

- aseg: voxel count, volume (mm³) and normalised intensity;
- aparc, left and right hemispheres: mean cortical thickness (mm), gray matter volume (mm³) and surface area (mm²).

## 📚 Citing

> [!TIP]
> If you use this App in your work, please cite the App, the software it builds on and brainlife.io (below). GitHub's **Cite this repository** button gives the App citation in APA and BibTeX.

- Freesurfer Group Analysis. brainlife.io App. [doi:10.25663/bl.app.94](https://doi.org/10.25663/bl.app.94)
- Fischl. FreeSurfer. *NeuroImage* 62:774-781 (2012). [doi:10.1016/j.neuroimage.2012.01.021](https://doi.org/10.1016/j.neuroimage.2012.01.021)
- Hayashi S, Caron BA, Heinsfeld AS, et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. *Nature Methods* 21:809–813 (2024). [doi:10.1038/s41592-024-02237-2](https://doi.org/10.1038/s41592-024-02237-2)
- Avesani P, McPherson B, Hayashi S, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. *Scientific Data* 6:69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

## 👥 Authors

- Soichi Hayashi

## 💰 Funding

[![Wellcome-226486/Z/22/Z](https://img.shields.io/badge/Wellcome-226486%2FZ%2F22%2FZ-purple.svg)](https://wellcome.org/)
[![NIH-NINDS-U24NS140384](https://img.shields.io/badge/NIH_NINDS-U24NS140384-green.svg)](https://reporter.nih.gov/project-details/11261037)
[![NIH-NINDS-UM1NS132207](https://img.shields.io/badge/NIH_NINDS-UM1NS132207-green.svg)](https://reporter.nih.gov/project-details/11411328)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://reporter.nih.gov/project-details/10262925)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://reporter.nih.gov/project-details/10428625)
[![NIH-NIMH-R01MH126699](https://img.shields.io/badge/NIH_NIMH-R01MH126699-green.svg)](https://reporter.nih.gov/project-details/10460628)
[![NIH-NIDCD-R01DC020088](https://img.shields.io/badge/NIH_NIDCD-R01DC020088-green.svg)](https://reporter.nih.gov/project-details/11140284)
[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-2203524](https://img.shields.io/badge/NSF_BCS-2203524-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2203524)
[![NSF-IIS-1636893](https://img.shields.io/badge/NSF_IIS-1636893-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-OAC-2148729](https://img.shields.io/badge/NSF_OAC-2148729-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148729)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NSF-IIS-2148700](https://img.shields.io/badge/NSF_IIS-2148700-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148700)
[![NSF-OAC-1916518](https://img.shields.io/badge/NSF_OAC-1916518-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1916518)

<sub>brainlife.io is publicly funded, and acknowledging that support helps keep it running. This App was developed with support from Wellcome, the U.S. National Institutes of Health (including the BRAIN Initiative BRAIN CONNECTS program: The Axonal Projectome EXchange, U24NS140384, and the Center for Mesoscale Connectomics, UM1NS132207) and the U.S. National Science Foundation.</sub>

## ⚖️ License

MIT.
