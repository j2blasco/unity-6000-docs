* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-giturl.html

  * [Packages and package management](https://docs.unity3d.com/6000.0/Documentation/Manual/PackagesList.html)
  * [Package management with the Package Manager window](https://docs.unity3d.com/6000.0/Documentation/Manual/managing-packages-window.html)
  * [Add and remove UPM packages or feature sets](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-actions.html)
  * Install a UPM package from a Git URL


[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-tarball.html)
Install a UPM package from a local tarball file
[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-quick.html)
Install a UPM package by name
# Install a UPM package from a Git URL
The Package Manager can load a **UPM package** A **Package** managed by the **Unity Package Manager**. Refer to **Packages**.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#UPMpackage) from a Git repository on a remote server.
## Prerequisites
  * Install the [Git client](https://git-scm.com/) (minimum version 2.14.0) on your computer.
  * On Windows, add the Git executable path to the `PATH` system environment variable.
  * If the target repository tracks files with Git LFS, install the [Git LFS client](https://git-lfs.com/) on your computer.
  * Read the information about using [Git dependencies](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-git.html)The Package Manager retrieves Git dependencies from a Git repository directly rather than from a package registry. Git dependencies use a Git URL reference instead of a version, and there’s no guarantee about the package quality, stability, validity, or even whether the version stated in its `package.json` file respects Semantic Versioning rules with regards to officially published releases of this package. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-concepts.html#Git)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Gitdependency) in your project.


## Procedure
To install a UPM package from a Git URL:
  1. Open the [Package Manager window](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-access.html), if it’s not already open.
  2. Open the **Add** (**+**) menu in the Package Manager’s toolbar.
  3. The options for installing packages appear.
![Install package from git URL button](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/upm-ui-giturl.png) Install package from git URL button
  4. Select **Install package from git URL** from the install menu. A text box and an **Install** button appear.
  5. Enter a valid Git URL in the text box. For information about how to construct a valid Git URL, refer to [Git URLs and extended syntax](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-git.html#syntax). Examples of valid Git URLs include: 
     * `https://github.example.com/myuser/myrepo.git` (if your package is in the root of the repository).
     * `https://github.example.com/myuser/myrepo.git?path=/subfolder` (if your package is in a [subfolder](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-git.html#subfolder) within the repository).
  6. Select **Install**.


If Unity was able to install the package successfully, the package now appears in the [package list](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-list.html) with the **git** label. If Unity wasn’t able to install the package, the [Unity Console](https://docs.unity3d.com/6000.0/Documentation/Manual/Console.html) displays an error message, such as:
  * [No ‘Git’ executable was found](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-errors.html#git-not-found)
  * [Git-lfs: command not found](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-errors.html#git-lfs)
  * [Repository not found](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-errors.html#bad-url)
  * [Couldn’t read Username: terminal prompts disabled](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-errors.html#prompts-disabled)


Click an error message link to get some help for it on the [Package Manager troubleshooting](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-errors.html) page.
**Tip** : If you want to check for updates and update your Git dependency to the latest version from the repository, click **Update**. You can also use the [Install package from git URL](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-giturl.html) menu item to update your Git dependency. For information on Git dependencies, refer to [Locked Git dependencies](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-git.html#git-locks).
## Additional resources
  * [Package types](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-package-types.html)
  * [Add and remove UPM packages or feature sets](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-actions.html)
  * [Add and remove asset packages](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-actions-ap.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-tarball.html)
Install a UPM package from a local tarball file
[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-quick.html)
Install a UPM package by name
