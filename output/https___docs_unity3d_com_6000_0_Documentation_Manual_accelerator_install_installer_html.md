* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-install-installer.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Assets and media](https://docs.unity3d.com/6000.0/Documentation/Manual/assets-and-media.html)
  * [Caching assets](https://docs.unity3d.com/6000.0/Documentation/Manual/importing-caching-assets.html)
  * Install Unity Accelerator with the installer


[](https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-requirements.html)
Unity Accelerator requirements
[](https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-install-docker.html)
Install Unity Accelerator with Docker Hub
# Install Unity Accelerator with the installer
To install Unity **Accelerator** The Unity Accelerator is an external tool that provides an asset cache that keeps copies of a team’s imported assets. The goal of the Accelerator is to speed up teamwork and reduce iteration time by coordinating asset sharing so that you don’t need to reimport portions of your project. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityAccelerator.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Accelerator) through its installer, select the correct link for your operating system:
  * [Windows](https://download-accelerator.unity3d.com/latest-release/windows/unity-accelerator-app-v1.0.941+g6b39b61.exe)
  * [macOS](https://download-accelerator.unity3d.com/latest-release/mac/unity-accelerator-app-v1.0.941+g6b39b61.dmg)
  * [Linux](https://download-accelerator.unity3d.com/latest-release/linux/unity-accelerator-app-v1.0.941+g6b39b61.AppImage)


Refer to [Verify the Unity Accelerator version](https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-verify-version.html) to verify the installation on a Linux machine.
Open the installer and follow the steps to complete installation. 
![Unity Accelerator installation wizard.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/accelerator-installer.png) Unity Accelerator installation wizard.
**Important:** On the **Protocol Configuration** screen, disable the **Accelerate Unity Collaborate** checkbox. This option isn’t supported.
On the final screen, the installer displays the IP address and port number of the installed accelerator, which you can use to [configure the accelerator in the Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-configure.html).
## Run the installer on the command line
On each platform, you can run the installer from the command line. If you execute the installer with an argument of `--help`, it displays the various options available. 
To run a full install without any prompts, provide values for the following:
**Command line argument** | **Description**  
---|---  
`--storagedir` | Sets the directory for the Accelerator to store files and configurations.  
`--mode unattended` | Use for automated installations that don’t need to query anything. This uses default values, or values from other option flags provided.  
On macOS, you need to mount the disk image (.dmg) and run the binary located in the installer app’s directory located at `Contents/macOS/installbuilder.sh`.
For a full list of the command line options available, refer to the [Command line arguments reference](https://docs.unity3d.com/6000.0/Documentation/Manual/EditorCommandLineArguments.html#accelerator).
Once you’ve installed the accelerator, follow the information in [Configure the Unity Editor to use an accelerator](https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-configure.html).
## Additional resources
  * [Unity Accelerator requirements](https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-requirements.html)
  * [Install Unity Accelerator with Docker Hub](https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-install-docker.html)
  * [Verify the Unity Accelerator version](https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-verify-version.html)
  * [Configure an accelerator in the Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-configure.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-requirements.html)
Unity Accelerator requirements
[](https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-install-docker.html)
Install Unity Accelerator with Docker Hub
