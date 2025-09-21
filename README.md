# Rules.JSON Generator

[![License: Creator Commons](https://img.shields.io/badge/License-Creator%20Commons-blue.svg)](https://creativecommons.org/)  
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)

**Rules.JSON Generator** is a simple and powerful tool that converts GitHub raw hosts files into a structured `rules.json` file. Perfect for organizing large lists of domains into a JSON format for various applications.

---

## OS Support

| Operating System | Status |
|-----------------|--------|
| Windows         | ✅ Fully tested |
| Linux           | ⚠️ Untested |
| macOS           | ⚠️ Untested |

---

## Windows Release

For Windows users, you can download and use the **pre-built `.exe` release** for convenience:  
[Download Release](https://github.com/AirgPlays/Rules.JSON-Generator/releases/download/V1.3.0/Rules.JSON.Generator.x64.1.3.0.zip)

---

## Features

- ✅ Reads a GitHub raw hosts file directly.  
- ✅ Skips `localhost` entries and comments automatically.  
- ✅ Customizable **starting ID** (default = 1).  
- ✅ Customizable **priority** (default = 1).  
- ✅ Saves the generated `rules.json` to any location of your choice.  
- ✅ User-friendly **GUI interface**.  

---

## Installation

1. Make sure you have **Python 3.x** installed:  
   [Download Python](https://www.python.org/downloads/)  

2. Install required packages (if any, Tkinter comes pre-installed with most Python distributions).  

3. Download or clone this repository:  

```bash
git clone https://github.com/yourusername/rules-json-generator.git
cd Rules.JSON-Generator
python Rules.JSON-Generator.py

