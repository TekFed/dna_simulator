# 🧬 DNA Trait Simulator

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-success)](https://docs.python.org/3/library/tkinter.html)
[![Biopython](https://img.shields.io/badge/Biopython-1.83+-brightgreen)](https://biopython.org/)
[![py-avataaars](https://img.shields.io/badge/Avatars-py--avataaars-ff69b4)](https://pypi.org/project/py-avataaars/)

A fun and educational Python desktop application that lets you "design" a person by entering DNA codons (3-base sequences) and watch them turn into a unique cartoon avatar!

## ✨ Features

- Translate real 3-base DNA codons (A/T/C/G) into traits using **Biopython**
- 9 customizable traits: eye color, hair color & style, skin tone, height, freckles, nose size, lip fullness, body build
- Gender selection (XX = female, XY = male)
- Beautiful cartoon avatars generated with **py-avataaars**
- **Random Person** button — instantly generate a surprise character
- **Save avatar** as PNG image
- Scrollable modern Tkinter GUI
- Mutant mode: use stop codons (TAA/TAG/TGA) for funny results!

## 📸 Screenshots

| Light skin + blonde wavy hair          | Dark skin + curly red hair + muscular   | Albino + bald + violet eyes (mutant)   |
|----------------------------------------|-----------------------------------------|----------------------------------------|
| ![light blonde](https://github.com/TekFed/dna_simulator/blob/main/Screenshots/LightSkin_CurlyHair.png) | ![dark curly](Screenshots\LightSkin_CurlyHair.png)     | ![albino mutant](Screenshots\straight_hair.png) |

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Windows / macOS / Linux

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/TekFed/dna_simulator.git
cd dna_simulator

# 2. Install dependencies
pip install -r requirements.txt
```

**requirements.txt**
```text
biopython>=1.83
py-avataaars>=1.2
pillow>=10.0
```

### Run the app

```bash
python dna_simulator.py
```

## 🎮 How to Play

1. Enter **XX** or **XY** for gender
2. Type 3-letter codons (only A/T/C/G) for each trait  
   Examples:
   - ATG → Methionine → often "default" trait
   - TAA / TAG / TGA → Stop codon → mutant trait!
3. Click **Generate Person →**
4. Click **🎲 Random Person** for surprise
5. Click **💾 Save Avatar as PNG** to keep your creation

## 🧬 Codon → Trait Cheat Sheet (examples)

| Codon   | Amino Acid | Eye Color | Hair Color | Hair Style | Skin Tone | ... |
|---------|------------|-----------|------------|------------|-----------|-----|
| ATG     | M          | Hazel     | Black      | Straight   | Light     | ... |
| TAA     | * (stop)   | Violet    | White      | Bald       | Albino    | ... |
| GCA     | A          | Hazel     | Black      | Straight   | Light     | ... |
| CGA     | R          | Brown     | Black      | Straight   | Dark      | ... |

Full mapping is in the code → feel free to customize!

## 🛠️ Tech Stack

- **GUI**: Tkinter (built-in)
- **DNA translation**: Biopython
- **Avatar generation**: py-avataaars
- **Image handling**: Pillow

## ⚠️ Known Limitations

- Avatars are generated using the **py-avataaars** library, which has a fixed set of styles and does not support every possible trait combination perfectly (e.g., no direct freckles, limited nose variations, no glasses/hats).
- Hair color "White" falls back to "Blonde" because the library does not have a true white/gray option.
- Nose size and freckles are only shown in the text list (not visually reflected in the avatar due to library constraints).
- Image size is fixed by the library default (no custom width/height control in older versions).
- On Windows, temporary file handling can sometimes be slow or fail if antivirus is aggressive — restart the app if you see file access errors.
- No dark mode or theme switching yet.
- Avatars are cartoon-style only — no realistic human rendering.

## 🙌 Contributing

Pull requests are welcome!  
Ideas:

- Add more traits (beard, glasses, hat...)
- Better mutant effects
- Export all traits as text/JSON
- Theme switcher (dark mode)

Just open an issue or PR.

## 📄 License

MIT License  
Feel free to use, modify, and share!

Made with ❤️
© 2026 Collins (@tekfed_Llins)

