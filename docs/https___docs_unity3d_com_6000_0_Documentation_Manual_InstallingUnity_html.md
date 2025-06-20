* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/InstallingUnity.html

  * [Install and upgrade](https://docs.unity3d.com/6000.0/Documentation/Manual/install-and-upgrade.html)
  * [Install Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/GettingStartedInstallingUnity.html)
  * Install Unity from the command line


[](https://docs.unity3d.com/6000.0/Documentation/Manual/install-unity-with-download-assistant.html)
Install Unity using Download Assistant
[](https://docs.unity3d.com/6000.0/Documentation/Manual/DeployingUnityOffline.html)
Install Unity on offline computers
# Install Unity from the command line
If you want to automate the deployment of Unity in an organization, you can install the Unity Editor and other components from the command line. The components are normal installer executable programs and packages which you can use to automate the deployment of Unity.
To automate the Unity deployment through the command line:
  1. Download the installer files for Unity and other components to a folder on your computer. You can use individual [installer files](https://docs.unity3d.com/6000.0/Documentation/Manual/install-unity-with-installers.html), or installer files and the script generated by [Unity Download Assistant](https://docs.unity3d.com/6000.0/Documentation/Manual/install-unity-with-download-assistant.html).
  2. Copy the contents of the folder to the destination computers.
  3. If you’re using individual installer files, run the commands to install the components individually. If you’re using Download Assistant, run the install script (`install.bat` on Windows or `install.sh` on Linux or macOS) to install all downloaded items.


The following procedures use the individual installer files option for installing Unity on Windows and macOS. For information about using the Download Assistant option, refer to [Install Unity on offline computers](https://docs.unity3d.com/6000.0/Documentation/Manual/DeployingUnityOffline.html).
## Install the Unity Editor and components on Windows
Use the following command line arguments to install the Editor and other components on Windows.
**Command line argument** | **Description**  
---|---  
**/S** | Performs an installation which runs silently without any user interaction.  
**/D=PATH** | Sets the default installation directory. Use with the silent installation option. The default folder is `C:\Program Files (x86)\Unity` (32-bit) or `C:\Program Files\Unity`(64-bit).  
**Note** : Installer command line arguments are case-sensitive.
### Install the Unity Editor
To install the Editor to a specific folder location, follow this example. This example demonstrates installing a 64-bit Editor to the `E:\Development\Unity` folder:
```
UnitySetup64.exe /S /D=E:\Development\Unity

```

Running this command installs Unity silently to `E:\Development\Unity` folder, which becomes the root of the Unity installation. In this case, the command installs the Editor program file to `E:\Development\Unity\Editor\Unity.exe`.
**Note** : Specify the default installation directory path as the last argument on the command line. Don’t enclose the provided path in quotes, even if it contains spaces.
### Uninstall the Unity Editor
To perform a silent uninstall, run `Uninstall.exe /S` from the command line or a script.
**Note** : Although the process finishes right away, there’s a delay before the files are actually removed. This is because the process copies the uninstaller to a temporary location so it can remove itself. Make sure that the working directory isn’t located within the folder where you installed Unity. If it is, the uninstaller is unable to remove the folder.
### Install other Unity components
To install other Unity components such as those that provide platform build support, use the following command as an example:
```
UnitySetup-Android-Support-for-Editor-6000.0.24f1.exe /S /D=C:\Program Files\Unity 6000.0.24f1

```

**Note** : You can optionally specify the folder path in the command when installing other components. In this case, make sure you specify the installation folder path to the Unity root folder that contains the Editor folder and not the folder that contains `Unity.exe`.
## Install the Unity Editor and components on macOS
Unity provides the individual installers as `.pkg` files. You can install these by using the `installer` command.
### Install the Unity Editor
To install the Editor to the `/Applications/Unity` folder on the specified target volume, use the following command as an example:
```
sudo installer [-dumplog] -package Unity.pkg -target /

```

### Install other Unity components
To install other Unity components such as those that provide platform build support, use the following command as an example:
```
sudo installer [-dumplog] -package UnitySetup-Android-Support-for-Editor-6000.0.24f1.pkg -target /

```

## Install several Unity versions
You can install multiple versions of Unity on the same computer.
On macOS, the installer creates a folder called `Unity`, and overwrites any existing folder with this name. To install more than one version of Unity on macOS, rename the existing `Unity` folder before installing another version.
On Windows, the installation folder is always named `Unity X.Y.Z[fp]W`, where the `f` marks an official release, and `p` marks a patch release.
**Note** : If you rename a Unity folder, the recommended best practice is to name the new folder logically. For example, add the Unity version number at the end of the name. In this case, any existing shortcuts, aliases, and links to the offline documentation no longer work if they still point to the old Unity version. If your browser bookmarks to the offline documentation no longer work, check if the URL points to the correct folder name.
## Additional resources
  * [Install Unity using installer files](https://docs.unity3d.com/6000.0/Documentation/Manual/install-unity-with-installers.html)
  * [Install Unity using Download Assistant](https://docs.unity3d.com/6000.0/Documentation/Manual/install-unity-with-download-assistant.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/install-unity-with-download-assistant.html)
Install Unity using Download Assistant
[](https://docs.unity3d.com/6000.0/Documentation/Manual/DeployingUnityOffline.html)
Install Unity on offline computers
