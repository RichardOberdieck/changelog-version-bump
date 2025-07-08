# Bump versions automagically
Bump versions based on changelog entries.

# Setup
This package only works together with scriv and works best if used with hatch.

In the `scriv` configuration the following is assumed:
```toml
[tool.scriv]
format = "md"
categories = [
  "Major: Feature",
  "Minor: Feature",
  "Minor: Fix", 
  "Patch: Fix", 
  "Major: Business impact",
  "Minor: Business impact"
]
```
You can adjust the categories as you like the `BUMB: ` part is what is checked for, and the bumps must be `Major, Minor, Patch`


For a nice integration in hatch use these two additional env definition blocks:
```toml
[tool.hatch.envs.changelog]
dependencies = [
  "scriv",
  "changelog-version"
]

[tool.hatch.envs.changelog.scripts]
init = "mkdir changelog.d"
new = "scriv create --edit --add"
collate = "scriv print > temp.md && hatch version $(changelog-version-bump)  && scriv collect"
```
1) Initial setup needed once is the `init` part (feel free to not bother with a seperate command).

2) In each branch you'll need to run `scriv create` or `hatch run changelog:new` to create and edit the changelog fragment for scriv.

3) The actual magic is the `collate` comand that should run in `ci/cd` when you create tags / releases.





# FAQ
Can you change the options and headings?
No. It would be easy to add configurability via the toml and a tool.changelog-version-bump section but for now I see no need, the defaults should suffice.

Could this not just be some bash?
Yes. This code was actually bash, but for distribution and later configuration, see above, python scripts are easier.

