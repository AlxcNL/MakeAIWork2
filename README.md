# MakeAIWork 2

## Projects

### OpenGL 

For the Simulation Project you need to setup an OpenGL environment.

<ol>

<li>

**Install freeglut library (Windows only)**

<p>
Start Git Bash as Administrator an run the following command 

```bash
install/install_freeglut.sh
```
</p>

</li>

<li>

**Install XQuartz X.Org Window System (MacOS only)**
On the MacOS host, we use xquartz to provide us with a MacOS X Window System.<br>
Download and install [xquartz](https://www.xquartz.org/)<br>
Log out and Log in to activate the changes the terminal

</li>

<li>

**Configure XQuartz to allow network connections from host**

<ol>

<li>

***Get your IP address***

<p>
Run the following command in the terminal to see your IP address

```bash
ifconfig en0 | grep 'inet ' | awk '{print $2}'
```
</p>

<li>

<p>

***Start XQuartz***

```bash
open -a XQuartz
```

which will open a XQuartz terminal in which you enter

```sh
xhost {Your IP}
```

having {Your IP} replaced with your IP-address.

</p>

Click on the word 'XQuartz' on the top left of your screen (next to the Apple logo) and select <i>Preference</i>. Open the tab
<i>Security</i> and check 'Allow connections from network clients'

</li>

<li>

**Install Socat**
The graphical Python script runs with a Linux X Window System in a Docker container. To connect this to the MacOS X Window System on the host we use the [command line utility socat](https://linux.die.net/man/1/socat).

```bash
brew install socat
```

</li>

</ol>

</li>

<li>

**Generate the simulation modules**

<p>Run the following command at <i>project/simpylc</i>

``sh
./generate_simulations.sh
``

</p>

</li>

<li>

**Test the GUI**

<p>Run the following command at <i>project/simpylc</i>

``sh
./start_client.sh
``

</p>

</li>

</ol>

---

## Python AI Workspace Installation

<ol>

<li>

**Create your own repository MakeAIWork2 on Github**

<p>
Browse to <a>github.com</a> and create <u>public</u> repository MakeAIWork2.
</p>

</li>

<li>

**Share your repository with the teachers**

<p>Post the link to your remote repository MakeAIWork2 in <u>your private Teams channel</u></p>

</li>

<li>

**Clone your git repository**

<p>
Clone your git repository MakeAIWork2 from Github to <u>the parent directory of MakeAIWork</u>
</p>

</li>

<li>

**Download and copy subfolders of this repository**

<p>
Download this repository as zip-file and extract the contents (files and subdirectories) from the zip-file to your (own) local git directory MakeAIWork2.
</p>

</li>

<li>

**Add and commit copied contents**

<p>

Add and commit the contents to your (own) remote github repository

Run the following commands from your MakeAIWork2 directory

```sh
git add .
git commit -m "Added contents for MakeAIWork2"
git push
```

</p>

</li>

<li>

**Configure git**

<p>Deselect the options <i>Start Docker Desktop when you log in</i> and <i>Use Virtualization framework</i>

</li>


</ol>

**Python (virtual) workspace**

<ol>

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

*Install Docker Desktop*
To facilitate you with a managed portable [isolated](https://learndocker.online/introduction/the-whats-and-whys/what-are-containers/) [Development Environment]((https://learndocker.online/introduction/the-whats-and-whys/why-docker-for-devs)), we provide a Docker image in which all dependencies are preinstalled. We prefer Docker for isolation since it is a much lighter solution than [Virtual Machine](https://learndocker.online/introduction/the-whats-and-whys/containers-vs-vms/).

<ol>

<li>

**Download and install [Docker Desktop](https://www.docker.com/get-started)**

[Download for Mac with Apple M* chip](https://docs.docker.com/desktop/mac/apple-silicon/)

<li>

**Configure Docker Desktop**

Open Docker Desktop, go to settings and select <i>Start when you login</i>

In Windows you can a script to enable Docker Desktop to start directly after you start Git Bash:

```bash
sh/git_bash_profile.sh
```

this script will also navigate automatically to the MakeAIWork directory.

### Visual Studio Code Configuration

<ol>

**Install Python extensions**

<li>

Install the [Git Easy extension](https://marketplace.visualstudio.com/items?itemName=bibhasdn.git-easy)

</li>

<li>

Install the [Mermaid extension](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid)

</li>

<li>

Install the [Docker extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker
)

</li>

<li>

Install the [MongoDB extension](https://marketplace.visualstudio.com/items?itemName=mongodb.mongodb-vscode) (Periode 3)

</li>

</ol>

---
### References
[How to Use Linux Terminal in Windows 10](https://allthings.how/how-to-use-linux-terminal-in-windows-10/)<br>
[Jupyter](https://jupyter.org/)<br>
[Running GUI's with Docker on OS X](https://www.youtube.com/watch?v=PKyj8sbZNYw&list=LL&index=4&t=6s)
