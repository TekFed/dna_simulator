import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from Bio.Seq import Seq
from py_avataaars import PyAvataaar, AvatarStyle, SkinColor, HairColor, TopType, EyesType, MouthType, ClotheType
from PIL import Image, ImageTk
import random
import tempfile
import os

# Trait maps
eye_color_map = {
    'A': 'Hazel', 'C': 'Brown', 'D': 'Brown', 'E': 'Blue',
    'F': 'Green', 'G': 'Hazel', 'H': 'Brown', 'I': 'Blue',
    'K': 'Green', 'L': 'Hazel', 'M': 'Brown', 'N': 'Blue',
    'P': 'Green', 'Q': 'Hazel', 'R': 'Brown', 'S': 'Blue',
    'T': 'Green', 'V': 'Hazel', 'W': 'Brown', 'Y': 'Blue', '*': 'Violet'
}

hair_color_map = {
    'A': 'Black', 'C': 'Brown', 'D': 'Black', 'E': 'Brown',
    'F': 'Red', 'G': 'Blonde', 'H': 'Brown', 'I': 'Blonde',
    'K': 'Red', 'L': 'Brown', 'M': 'Black', 'N': 'Blonde',
    'P': 'Red', 'Q': 'Brown', 'R': 'Black', 'S': 'Auburn',
    'T': 'Blonde', 'V': 'Auburn', 'W': 'Red', 'Y': 'Auburn', '*': 'White'
}

hair_curl_map = {
    'A': 'Straight', 'C': 'Wavy', 'D': 'Straight', 'E': 'Curly',
    'F': 'Wavy', 'G': 'Straight', 'H': 'Curly', 'I': 'Straight',
    'K': 'Wavy', 'L': 'Curly', 'M': 'Straight', 'N': 'Wavy',
    'P': 'Curly', 'Q': 'Straight', 'R': 'Wavy', 'S': 'Straight',
    'T': 'Curly', 'V': 'Wavy', 'W': 'Straight', 'Y': 'Curly', '*': 'Bald'
}

height_map = {
    'A': 'Short', 'C': 'Average', 'D': 'Short', 'E': 'Tall',
    'F': 'Average', 'G': 'Short', 'H': 'Tall', 'I': 'Average',
    'K': 'Tall', 'L': 'Average', 'M': 'Average', 'N': 'Short',
    'P': 'Short', 'Q': 'Tall', 'R': 'Tall', 'S': 'Short',
    'T': 'Average', 'V': 'Average', 'W': 'Tall', 'Y': 'Average', '*': 'Giant'
}

skin_tone_map = {
    'A': 'Light', 'C': 'Medium', 'D': 'Dark', 'E': 'Dark',
    'F': 'Light', 'G': 'Light', 'H': 'Dark', 'I': 'Light',
    'K': 'Dark', 'L': 'Medium', 'M': 'Medium', 'N': 'Light',
    'P': 'Light', 'Q': 'Dark', 'R': 'Dark', 'S': 'Light',
    'T': 'Medium', 'V': 'Light', 'W': 'Dark', 'Y': 'Medium', '*': 'Albino'
}

freckles_map = {
    'A': 'No', 'C': 'No', 'D': 'No', 'E': 'No',
    'F': 'Yes', 'G': 'No', 'H': 'No', 'I': 'No',
    'K': 'No', 'L': 'No', 'M': 'No', 'N': 'Yes',
    'P': 'No', 'Q': 'No', 'R': 'No', 'S': 'Yes',
    'T': 'No', 'V': 'No', 'W': 'Yes', 'Y': 'Yes', '*': 'Yes'
}

nose_size_map = {
    'A': 'Small', 'C': 'Medium', 'D': 'Small', 'E': 'Medium',
    'F': 'Large', 'G': 'Small', 'H': 'Medium', 'I': 'Small',
    'K': 'Large', 'L': 'Large', 'M': 'Medium', 'N': 'Small',
    'P': 'Small', 'Q': 'Large', 'R': 'Medium', 'S': 'Small',
    'T': 'Medium', 'V': 'Large', 'W': 'Large', 'Y': 'Medium', '*': 'Huge'
}

lip_fullness_map = {
    'A': 'Thin', 'C': 'Full', 'D': 'Thin', 'E': 'Full',
    'F': 'Full', 'G': 'Thin', 'H': 'Full', 'I': 'Thin',
    'K': 'Full', 'L': 'Thin', 'M': 'Full', 'N': 'Thin',
    'P': 'Full', 'Q': 'Thin', 'R': 'Full', 'S': 'Thin',
    'T': 'Full', 'V': 'Thin', 'W': 'Full', 'Y': 'Thin', '*': 'Pouty'
}

body_build_map = {
    'A': 'Slim', 'C': 'Average', 'D': 'Slim', 'E': 'Average',
    'F': 'Muscular', 'G': 'Slim', 'H': 'Average', 'I': 'Slim',
    'K': 'Muscular', 'L': 'Average', 'M': 'Average', 'N': 'Slim',
    'P': 'Slim', 'Q': 'Muscular', 'R': 'Muscular', 'S': 'Slim',
    'T': 'Average', 'V': 'Average', 'W': 'Muscular', 'Y': 'Average', '*': 'Super'
}

class DNASimulatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DNA Trait Simulator - Collins Edition (Stable)")
        self.root.geometry("1080x740")
        self.root.minsize(1000, 650)

        self.last_gender = None
        self.last_traits = None
        self.current_photo = None

        # Left panel (scrollable)
        self.left_frame = ttk.Frame(root, padding=12)
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y, expand=False)

        self.canvas_left = tk.Canvas(self.left_frame, width=360)
        self.scrollbar = ttk.Scrollbar(self.left_frame, orient="vertical", command=self.canvas_left.yview)
        self.scrollable_frame = ttk.Frame(self.canvas_left)
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas_left.configure(scrollregion=self.canvas_left.bbox("all")))
        self.canvas_left.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas_left.configure(yscrollcommand=self.scrollbar.set)
        self.canvas_left.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        ttk.Label(self.scrollable_frame, text="DNA Trait Simulator", font=("Arial", 16, "bold")).pack(pady=(10, 15))

        hint_text = "Enter 3 letters from A T C G\nExamples: ATG  TAA  GCA  TTT\nTip: Stop codons = funny mutants! 😄"
        ttk.Label(self.scrollable_frame, text=hint_text, justify="left", wraplength=340, foreground="#444").pack(anchor="w", pady=(0, 20))

        ttk.Label(self.scrollable_frame, text="Chromosomes (XX = Female, XY = Male):").pack(anchor="w")
        self.gender_entry = ttk.Entry(self.scrollable_frame, width=30)
        self.gender_entry.pack(fill=tk.X, pady=(4, 14))

        self.codon_entries = {}
        self.traits_config = [
            ('eye color', eye_color_map), ('hair color', hair_color_map), ('hair curliness', hair_curl_map),
            ('height', height_map), ('skin tone', skin_tone_map), ('freckles', freckles_map),
            ('nose size', nose_size_map), ('lip fullness', lip_fullness_map), ('body build', body_build_map)
        ]

        for trait_name, _ in self.traits_config:
            ttk.Label(self.scrollable_frame, text=f"{trait_name.capitalize()} (3 bases):").pack(anchor="w")
            entry = ttk.Entry(self.scrollable_frame, width=30)
            entry.pack(fill=tk.X, pady=(4, 14))
            self.codon_entries[trait_name] = entry

        btn_frame = ttk.Frame(self.scrollable_frame)
        btn_frame.pack(pady=15)
        ttk.Button(btn_frame, text="Generate Person →", command=self.generate_person).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="🎲 Random Person", command=self.random_person).pack(side=tk.LEFT, padx=5)

        self.save_btn = ttk.Button(self.scrollable_frame, text="💾 Save Avatar as PNG", command=self.save_avatar, state="disabled")
        self.save_btn.pack(pady=8)

        self.trait_display_frame = ttk.LabelFrame(self.scrollable_frame, text="Your Person's Traits", padding=10)
        self.trait_display_frame.pack(fill=tk.X, pady=10)
        self.trait_labels = []

        self.canvas = tk.Canvas(root, width=640, height=640, bg="#F0F8FF", highlightthickness=0)
        self.canvas.pack(side=tk.RIGHT, padx=20, pady=20, fill=tk.BOTH, expand=True)

    def get_trait_from_codon(self, codon, trait_map):
        codon = codon.upper().strip()
        if len(codon) != 3 or not all(b in 'ATCG' for b in codon):
            raise ValueError(f"Invalid codon: '{codon}'\nMust be exactly 3 letters from A, T, C, G.")
        seq = Seq(codon)
        aa = str(seq.translate())
        return trait_map[aa]

    def random_person(self):
        bases = 'ATCG'
        for trait_name, _ in self.traits_config:
            codon = ''.join(random.choice(bases) for _ in range(3))
            self.codon_entries[trait_name].delete(0, tk.END)
            self.codon_entries[trait_name].insert(0, codon)
        self.gender_entry.delete(0, tk.END)
        self.gender_entry.insert(0, random.choice(["XX", "XY"]))
        self.generate_person()

    def generate_person(self):
        try:
            chrom = self.gender_entry.get().upper().strip()
            gender = "Female" if chrom == "XX" else "Male" if chrom == "XY" else None
            if not gender:
                raise ValueError("Please enter XX or XY.")

            traits = {}
            for trait_name, trait_map in self.traits_config:
                codon = self.codon_entries[trait_name].get()
                traits[trait_name.replace(' ', '_')] = self.get_trait_from_codon(codon, trait_map)

            for lbl in self.trait_labels: lbl.destroy()  # noqa: E701
            self.trait_labels = []
            texts = [f"Gender: {gender}"]
            for k, v in traits.items():
                if k == 'hair_curliness':
                    texts.append(f"Hair: {traits['hair_color']}, {v}")
                elif k != 'hair_color':
                    texts.append(f"{k.replace('_', ' ').title()}: {v}")
            for text in texts:
                lbl = ttk.Label(self.trait_display_frame, text=text, font=("Arial", 10))
                lbl.pack(anchor="w", pady=3)
                self.trait_labels.append(lbl)

            self.last_gender = gender
            self.last_traits = traits.copy()
            self.save_btn.config(state="normal")

            self.generate_avatar(gender, traits)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def generate_avatar(self, gender, traits):
        hair_col_map = {
            'Black': HairColor.BLACK, 'Brown': HairColor.BROWN, 'Blonde': HairColor.BLONDE,
            'Red': HairColor.RED, 'Auburn': HairColor.AUBURN, 'White': HairColor.BLONDE
        }

        hair_style_map = {
            'Straight': TopType.LONG_HAIR_STRAIGHT if gender == "Female" else TopType.SHORT_HAIR_THE_CAESAR_SIDE_PART,
            'Wavy': TopType.LONG_HAIR_CURVY if gender == "Female" else TopType.SHORT_HAIR_THE_CAESAR_SIDE_PART,
            'Curly': TopType.LONG_HAIR_CURLY if gender == "Female" else TopType.SHORT_HAIR_CURLY,
            'Bald': TopType.NO_HAIR
        }

        mouth_map = {'Thin': MouthType.SERIOUS, 'Full': MouthType.SMILE, 'Pouty': MouthType.SMILE}

        clothe_type = ClotheType.HOODIE if traits['body_build'] in ['Slim', 'Average'] else ClotheType.BLAZER_SWEATER

        avatar = PyAvataaar(
            style=AvatarStyle.CIRCLE,
            skin_color=SkinColor.LIGHT if traits['skin_tone'] in ['Light', 'Albino'] else
                      SkinColor.YELLOW if traits['skin_tone'] == 'Medium' else SkinColor.BROWN,
            hair_color=hair_col_map.get(traits['hair_color'], HairColor.BLACK),
            top_type=hair_style_map.get(traits['hair_curliness'], TopType.LONG_HAIR_STRAIGHT),
            eye_type=EyesType.DEFAULT,
            mouth_type=mouth_map.get(traits['lip_fullness'], MouthType.SMILE),
            clothe_type=clothe_type
        )

        fd, tmp_path = tempfile.mkstemp(suffix=".png")
        os.close(fd)

        try:
            avatar.render_png_file(tmp_path)
            img = Image.open(tmp_path)
            photo = ImageTk.PhotoImage(img)
        finally:
            try:
                os.unlink(tmp_path)
            except:  # noqa: E722
                pass

        self.canvas.delete("all")
        self.canvas.create_image(320, 320, image=photo)
        self.current_photo = photo

    def save_avatar(self):
        if not self.last_gender or not self.last_traits:
            return
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png")],
            title="Save Avatar"
        )
        if file_path:
            avatar = PyAvataaar(
                style=AvatarStyle.CIRCLE,
                skin_color=SkinColor.LIGHT if self.last_traits['skin_tone'] in ['Light', 'Albino'] else
                          SkinColor.YELLOW if self.last_traits['skin_tone'] == 'Medium' else SkinColor.BROWN,
                hair_color=HairColor.BLONDE if self.last_traits['hair_color'] == 'White' else HairColor.BLACK,
                top_type=TopType.LONG_HAIR_STRAIGHT,
                eye_type=EyesType.DEFAULT,
                mouth_type=MouthType.SMILE,
                clothe_type=ClotheType.HOODIE
            )
            avatar.render_png_file(file_path)
            messagebox.showinfo("Saved ✓", f"Avatar saved successfully!\n{file_path}")

if __name__ == "__main__":
    root = tk.Tk()
    style = ttk.Style()
    style.configure("Accent.TButton", font=("Arial", 11, "bold"))
    app = DNASimulatorApp(root)
    root.mainloop()