* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-install-editor.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Embedded systems](https://docs.unity3d.com/6000.0/Documentation/Manual/embedded-systems.html)
  * [QNX](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx.html)
  * [Get started with QNX](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-get-started.html)
  * Install the platform package for QNX


[](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-get-started.html)
Get started with QNX
[](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-environment-setup.html)
Set up your environment for QNX
# Install the platform package for QNX
Install the platform package for QNX on Linux, macOS, and Windows.
**Note:** The Unity Editor for QNX is available under separate terms. For licensing and download information, contact your Account Manager or the [Unity Sales](https://create.unity.com/unity-for-industries) team.
## Requirements and compatibility
  * Your system must meet the [System requirements for the Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/system-requirements.html#editor).
  * You must have the [QNX Software Center](http://www.qnx.com/download/index.html) installed.
  * Before starting the Unity Editor, make sure the QNX SDP Environment is set up correctly for the Editor to register it.


## Installation
To install the Unity Editor for QNX on your system, follow these steps:
  1. On the [Unity QNX releases page](https://share.unity.com/secure/workspace/?packageId=BAKK-NL2G&tok=ABSEtmWNjeg8_TWIzN8VAKfsuya3N5NbgA:1730216656105&enableStreamSaver=true#directory/9226e9bb-8abd-4a07-886c-f4e0e374ac11), go to **QNX builds** > **Unity 6**.  
**Note:** If you’re unable to access the QNX releases page, contact your Account Manager or the [Unity Sales](https://create.unity.com/unity-for-industries) team. 
  2. Select a Unity version and download the setup installer for your operating system. 
**Operating system** | **Installer file extension**  
---|---  
**Windows** | .exe  
**Linux** | .xz  
**macOS** | .pkg  
  3. Run the installer to install to a folder of your choice.
  4. On the [Unity download archive](https://unity.com/releases/editor/archive), install the corresponding Unity 6 Editor version in the same folder through the [Unity Hub](https://docs.unity3d.com/hub/manual/index.html).  
**Note:** The Editor version must match the setup installer version for the Editor to work correctly. 


The Editor for QNX is now installed for your Windows or Linux systems. Next, [set up your environment for QNX](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-environment-setup.html). However, if you’re using macOS, follow the steps in [Additional instructions for macOS installation](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-install-editor.html#macOS).
### Additional instructions for macOS installation
On macOS, you need to move and re-install the Editor and platform package manually because Unity installs on the wrong installation path. To make sure the Editor and platform package work correctly, follow these steps:
  1. Move the installed Editor application from `/Applications/Unity/Hub/Editor/<version>/Unity` to `/Applications/Unity/Unity`.
  2. Open the downloaded setup installer package. A dialog reads: `"UnitySetup<platform><version>.pkg can’t be opened because Apple cannot check it for malicious software."`
  3. On your computer, go to **System Settings** > **Privacy & Security** > **Security**. A dialog reads: `"UnitySetup<platform><version>.pkg was blocked from use because it is not from an identified developer."`
  4. Click **Open Anyway**.
  5. Enter your password and click **Open**.
  6. Install the package and re-enter your password.
  7. Go to the **Unity Hub** window and find the chosen version under **Installs**.
  8. Click the gear icon for the chosen version and select **Uninstall**.
  9. Click **Locate** in the Unity Hub to select the installed Editor application from the `/Applications/Unity/Unity` path.


The Unity Editor and platform package for QNX now works correctly on macOS. Next, [set up your environment for QNX](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-environment-setup.html). 
## Additional resources
  * [QNX product documentation](http://www.qnx.com/developers/docs/index.html)
  * [Build for QNX from the command line](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-build-command-line.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-get-started.html)
Get started with QNX
[](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-environment-setup.html)
Set up your environment for QNX
