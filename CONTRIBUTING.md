# How to Contribute

Thank you for either opening a pull request or an issue. I makes me feel like people like using my creations and care enough to give back! 😊

For the best chance of your contributions to make into the next release, please follow these steps for pull requests and issues respectively.

## Pull Requests

1. edit `themes/mariana-reference.json` instead of `themes/mariana-color-theme.json`
1. run build task (cmd+shift+B) or `$ python3 mariana.py` to generate `themes/mariana-color-theme.json`
1. start debug (F5) to preview your changes

> ⚠️ If you only edit `themes/mariana-color-theme.json` directly, the commit history will look unreadable.
>
> Also your changes could be overwritten the next time someone runs the build task.

In `themes/mariana-reference.json`, colour names are used instead of hex colour codes. Available colour names are listed in `colour/palette.py` in the `Mariana` class.

The build step will text generate a `themes/mariana-color-theme.json` file by replacing the colour names for hex and stripping out json whitespace.

### pull request description

Screenshots are much appriciated but not required. They are especially helpful if you make changes to token colours.

## Issues

Screenshots are much appriciated but not required.
