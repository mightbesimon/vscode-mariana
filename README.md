# Mariana ![version](https://img.shields.io/visual-studio-marketplace/v/mightbesimon.mariana-sublime?label=)

[![sponsor](https://img.shields.io/github/sponsors/mightbesimon?color=red&label=Sponsor&logo=github)](https://github.com/sponsors/mightbesimon)
![downloads](https://img.shields.io/vscode-marketplace/i/mightbesimon.mariana-sublime?color=white&label=&logo=visualstudiocode&logoColor=blue)
![publish](https://github.com/mightbesimon/vscode-mariana/actions/workflows/publish.yml/badge.svg)

> I already tried the other ones so you don't need to.

Most faithful port of Sublime Mariana theme!

Wow this took way too long 😅

![preview](thumbnails/mariana.png)

# Todo List

<details>

<summary>
	<strong>click</strong> 👇 to see todo items 👉 <em>if you'd like to contribute</em> 👈
</summary>

🚧 diff editor

🚧 merge conflict

🚧 panel 50% done

🚧 menu bar

🚧 command center

🚧 notification 50% done

🚧 banner

🚧 extension 50% done

🚧 keybinding labels

🚧 keyboard shortcut table

🚧 debug colours

🚧 testing colours

🚧 welcome page

🚧 breadcrums

🚧 snippets

🚧 symbol icons

🚧 debug icons

🚧 notebook

🚧 charts

🚧 ports

🚧 extension colours

</details>

> more ideas welcome 🙂
>
> PRs welcome 👨‍🍳👌💋

# Acknowledgements

- **Mariana Theme** - Dmitri Voronianski, Sublime HQ Pty Ltd

# Contributors

- **Simon** - [mightbesimon](https://github.com/mightbesimon)
- [gijocode](https://github.com/gijocode)
- [guillemap](https://github.com/guillemap)
- 👉 you? 👈

# Colour Reference

```python
class Mariana(metaclass=enum[Colour]):
	'''	mariana theme from sublime
	'''
	MARIANA  = hsla(210, 15, 22)
	DARK_0   = MARIANA.clone(l=11)
	DARK_1   = MARIANA.clone(l=13)
	DARK_2   = MARIANA.clone(l=19)
	MEDIUM_0 = MARIANA.clone()
	MEDIUM_1 = MARIANA.clone(l=40, a=75)
	MEDIUM_2 = MARIANA.clone(l=45)
	LIGHT_0  = hsla(220, 12, 69)
	LIGHT_1  = hsla(220, 28, 88)
	RED      = hsla(357, 79, 65)
	CORAL    = hsla( 13, 93, 66)
	ORANGE   = hsla( 32, 93, 66)
	YELLOW   = hsla( 40, 94, 68)
	MINT     = hsla(114, 31, 68)
	TEAL     = hsla(180, 36, 54)
	BLUE     = hsla(210, 50, 60)
	PURPLE   = hsla(300, 30, 68)
```
