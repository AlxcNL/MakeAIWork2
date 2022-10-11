# MakeAIWork 2

## Projects

---

## Python AI Workspace Installation
Watch [instruction videos at YouTube](https://youtube.com/playlist?list=PLf5zREwsIjUNQ2y4TGi9F0uXQZ1B08d_v)


### Clone this Git repository
To be able to use this repository and handover your code, you need to have remote access to Github.

<ol>

<li>

**Install Git**

Make sure you select "Checkout as-is, commit Unix-style line endings" during the installation process.

<ul>

<li>

[Git for Windows](https://gitforwindows.org/)

</li>

<li>

[Git for Mac](https://git-scm.com/download/mac)

</li>

</ul>

<li>

**Install [GitHub CLI](https://cli.github.com/) (MacOS and Ubuntu)**

```bash
brew install gh
```

[Installation instructions on Ubuntu](https://www.techiediaries.com/install-github-cli-ubuntu-20/ )

[Installation instructions on Ubuntu](https://www.techiediaries.com/install-github-cli-ubuntu-20/)

***NOTE***<br>
Although you could download and install GitHub CLI for Windows, I don't recommend it since it does not properly work in Git Bash.

</li>

<li>

**Install [Homebrew](https://brew.sh/) (MacOS only)**

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

</li>

<li>

**Install [iterm2](https://iterm2.com/) (MacOS)**

```bash
brew install iterm2
```

</li>

<li>

**Install zsh (MacOS and Ubuntu)**

<ul>

<li>

Install [zsh](https://www.howtogeek.com/362409/what-is-zsh-and-why-should-you-use-it-instead-of-bash/) on MacOS using

```bash
brew install zsh
```

In Ubuntu
```bash
sudo apt install zsh
```

</li>

<li>

Add iTerm2 path to zsh profile

 ```bash
echo "eval \"\$(homebrew/bin/brew shellenv)\"" >> ~/.zshrc
```

</li>

 <li>

**(Optional) Install oh-my-zsh (MacOS and Ubuntu)**

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

</li>

</ul>

</li>

<li>

**Create a fork of this repository**

Create a fork of AlxcNL/MakeAIWork2 in [GitHub](https://github.com/AlxcNL/MakeAIWork2) or
use the GitHub Client by entering the following commands in your terminal

```bash
gh repo fork https://github.com/AlxcNL/MakeAIWork2
```
</li>

<li>

**Clone your <b>fork</b>**
If you installed the GitHub client, you can authenticate with the following command in the terminal

```sh
gh repo clone git@github.com:{your_github_username}/MakeAIWork2.git
```

otherwise enter the following command in your (git)bash shell after replacing {your_github_username} with your GitHub username.
```sh
git clone git@github.com:{your_github_username}/MakeAIWork2.git
```

</li>

<li>

**Configure git**

In order to commit and push your changes, you need identitify yourself.

Open a (git)bash, enter directory MakeAIWork2 and run:
```bash
install/git_config.sh {your_github_username} {your@student.email.com}
```
This script will also set the [pull policy](https://www.git-scm.com/docs/git-pull) to rebase.

</li>

<li>

**Add upstream to original remote repository**

To be able To be able to fetch and merge changes from this repository using (bash) commands, you need to have a (second) upstream.  
If you used the GitHub client to create the fork you can <strong>skip</strong> this step, otherwise enter the following commands

```bash
git remote add AlxcNL https://github.com/AlxcNL/MakeAIWork2
```

</li>

<li>

Keep your fork repository up-todate by regularly pulling changes from the original remote repository into your local fork..

```bash
 git pull AlxcNL main
```

and push the changes to you remote fork

```bash
git push
```

</li>

</ol>


**Install python**

<ol>

<li>

Install [python](https://www.python.org/downloads/release/python-3105/)

</li>

<li>

Install Miniconda (MacOS and Linux)

Download and install [Miniconda](https://docs.conda.io/en/latest/miniconda.html)

</li>

<li>

Windows
```sh
install/init_git_bash_profile.sh
```

</li>

<li>

Create virtual Python environment 
```sh
install/create_virtual_env.sh
```

</li>

<li>

Install Python libraries

```bash
install/install_requirements.sh
```

</li>

</ol>

</li>

</li>

</ol>

### Edit with Visual Studio Code

<ol>

<li>

Install [Visual Studio Code](https://code.visualstudio.com)

</li>

<li>

**Enable VSCode to be opened from the command line (macOS only)**

In VSCode, open the Command Palette and type 'shell command' in order to select the Shell command: Install ‘code’ command in PATH

</li>

<li>

**Start vscode with command from current directory**

Start a (git) bash shell and enter directory MakeAIWork2, from there use the command <i>code</i> to start vscode.
```sh
cd MakeAIWork2
code .
```

</li>

<li>

**Install the Python extension**

Download and install the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

</li>

<li>

**Install the Git Bash plugin (Windows)**

</li>

<li>

**Install Live Share**

Follow the instructions at [Collaborate with Live Share](https://code.visualstudio.com/learn/collaboration/live-share)

</li>

</ol>

---

## Python AI Workspace Usage

---
### References
[How to Use Linux Terminal in Windows 10](https://allthings.how/how-to-use-linux-terminal-in-windows-10/)<br>
[Jupyter](https://jupyter.org/)<br>
[Running GUI's with Docker on OS X](https://www.youtube.com/watch?v=PKyj8sbZNYw&list=LL&index=4&t=6s)
