* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/windowsstore-deviceportal.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Universal Windows Platform](https://docs.unity3d.com/6000.0/Documentation/Manual/WindowsStore.html)
  * [Build and deliver for Universal Windows Platform](https://docs.unity3d.com/6000.0/Documentation/Manual/uwp-building-and-delivering.html)
  * Deploy a Windows or UWP app with the Windows Device Portal


[](https://docs.unity3d.com/6000.0/Documentation/Manual/windowsstore-deployment.html)
Deploy a UWP application
[](https://docs.unity3d.com/6000.0/Documentation/Manual/visionOS.html)
visionOS
# Deploy a Windows or UWP app with the Windows Device Portal
You can use the [Windows Device Portal](https://learn.microsoft.com/en-us/windows/uwp/debug-test-perf/device-portal) to build and run Windows or Universal Windows Platform (UWP) applications to a remote Windows 10+ device directly from the Unity Editor, alleviating the need to generate a Visual Studio project. Being connected remotely to a remote Windows device allows you to make faster iterations for testing your Unity Project.
## Set up the Device Portal
Before you set up the Device Portal in Unity, make sure that you [enable Developer Mode and Device Portal on your Windows device](https://learn.microsoft.com/en-us/windows/uwp/debug-test-perf/device-portal) using the **For Developer** section in Settings (Settings > Privacy & security > For developers).
To access the Device Portal settings for your Unity project:
  1. Go to **File** > **Build Profiles**.
  2. From the list of platforms in the **Platforms** panel, select **Universal Windows Platform** or [create a build profile](https://docs.unity3d.com/6000.0/Documentation/Manual/create-build-profile.html) for the **Universal Windows Platform**.
  3. Set **Build and Run on** as **Remote Device (via Device Portal)**.
  4. Fill in the following fields that appear.

**Setting** | **Description**  
---|---  
**Device Portal Address** | Enter the IP address and port number for the Device Portal. On Windows, locate the address in **Privacy & security** > **For Developers** > **Device Portal** > **Connect using**.  
**Device Portal Username** | Enter the username for the Device Portal. This is optional if you [enable WDP authentication](https://learn.microsoft.com/en-us/windows/uwp/debug-test-perf/device-portal).  
**Device Portal Password** | Enter the password for the Device Portal. This is optional if you [enable WDP authentication](https://learn.microsoft.com/en-us/windows/uwp/debug-test-perf/device-portal).  
Unity saves the **Device Portal Address** and **Device Portal Username** fields in ****Project settings** A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/comp-ManagerGroup.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ProjectSettings)**. For security purposes, Unity doesn’t save your Device Portal password, so you might need to re-enter your password when you restart the Editor or load a new project.
**Tip:** You can also use the Executable Only build type with Device Portal deployment for **UWP**. This makes iteration times faster on devices like HoloLens.
## Run your app on the remote device
When you have completed the setup for the Device Portal, select **Build and Run**. This builds the UWP/Windows app, deploys it to the remote device, and then launches it.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/windowsstore-deployment.html)
Deploy a UWP application
[](https://docs.unity3d.com/6000.0/Documentation/Manual/visionOS.html)
visionOS
