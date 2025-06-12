* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-stop-restart.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Assets and media](https://docs.unity3d.com/6000.0/Documentation/Manual/assets-and-media.html)
  * [Caching assets](https://docs.unity3d.com/6000.0/Documentation/Manual/importing-caching-assets.html)
  * Stop and restart Unity Accelerator


[](https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-configure.html)
Configure Unity Accelerator in the Editor
[](https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-monitor.html)
Monitor Unity Accelerator
# Stop and restart Unity Accelerator
Unity **Accelerator** The Unity Accelerator is an external tool that provides an asset cache that keeps copies of a team’s imported assets. The goal of the Accelerator is to speed up teamwork and reduce iteration time by coordinating asset sharing so that you don’t need to reimport portions of your project. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityAccelerator.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Accelerator) runs as a background process for each platform. To stop or restart Unity Accelerator for each platform, perform the following steps:
## Windows
  1. Open the **Services Panel** by searching for the term `Services` in the Settings menu, or running `services.msc` in the **Run** dialog (**Win** + **R**).
  2. Locate the `Unity Accelerator` service in the list. The option to **Stop the service** or **Restart the service** appears on the left panel.


## macOS
Run the `launchctl` command from the terminal to control the `com.unity3d.accelerator` service from the LaunchControl utility. For more information, refer to: <https://www.launchd.info/>.
## Linux
Use the `service` console utility to control the `unity-accelerator` service. For more information, refer to: <http://manpages.ubuntu.com/manpages/bionic/man8/service.8.html>.
## Maintenance
The Unity Accelerator service automatically updates itself during a maintenance period, currently set for 01:00 - 02:00 AM local time according to the machine running the accelerator. This only happens if the accelerator discovers a newer version available. You can disable automatic updates by toggling the Maintenance -> ‘Auto Updates’ button on the Configuration page of the dashboard.
The accelerator’s installation and uninstallation logs are saved in the operating system’s standard temp directory as `unity-accelerator-*install.log`. The accelerator’s logs are saved in the storage directory as `unity-accelerator.log`.
## Additional resources
  * [Monitor Unity Accelerator](https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-monitor.html)
  * [Use Unity Accelerator on the command line](https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-command-line.html)
  * [Command line arguments reference](https://docs.unity3d.com/6000.0/Documentation/Manual/EditorCommandLineArguments.html#accelerator)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-configure.html)
Configure Unity Accelerator in the Editor
[](https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-monitor.html)
Monitor Unity Accelerator
