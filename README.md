# MaxetUI

A modern, reusable terminal UI template built with Python and **Blessed**. MaxetUI provides a clean full-screen interface with responsive layouts, sidebar navigation, dynamic panels, and keyboard controls—making it an excellent starting point for dashboards, CLI tools, admin panels, and terminal applications.

## ✨ Features

* 🎨 Modern full-screen terminal interface
* 📋 Sidebar navigation
* 🧩 Dynamic, customizable content panels
* ⌨️ Keyboard-driven controls
* 📏 Automatic terminal resize handling
* ⏰ Live footer with real-time clock
* 🖥️ Built-in system information demo
* ⚡ Lightweight and easy to extend

## 📸 Preview

> Add a screenshot or GIF here.

```
┌──────────────────────────────────────────────────────────────┐
│                         MaxetUI                              │
├──────────────────────────────────────────────────────────────┤
│ Menu                  │ Details                             │
│                       │                                      │
│ 1. System Status      │ Python Version: 3.x                 │
│ 2. Environment Info   │ Platform: Windows/Linux             │
│ 3. Quick Demo         │ Resize terminal to adapt            │
│                       │                                      │
└──────────────────────────────────────────────────────────────┘
```

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/Maxetow/MaxetUI.git
cd MaxetUI
```

Install the required dependency:

```bash
pip install blessed
```

Or:

```bash
pip install -r requirements.txt
```

## 🚀 Usage

Run the application:

```bash
python main.py
```

### Controls

| Key   | Action                |
| ----- | --------------------- |
| **1** | Open System Status    |
| **2** | Open Environment Info |
| **3** | Open Quick Demo       |
| **Q** | Quit                  |

## 🛠️ Creating Your Own Panels

Register new panels with:

```python
app.register_panel(
    "4",
    "My Panel",
    "Panel description",
    lambda message: [
        message,
        "",
        "Custom content goes here."
    ],
)
```

## 📁 Project Structure

```
MaxetUI/
├── main.py
├── README.md
├── LICENSE
└── requirements.txt
```

## 💡 Perfect For

* CLI Applications
* Dashboards
* Admin Panels
* System Monitors
* Developer Tools
* Terminal Utilities
* Python Projects

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request to improve MaxetUI.

## 📄 License

This project is licensed under the **MIT License**.

---

Made with ❤️ using Python and Blessed.
