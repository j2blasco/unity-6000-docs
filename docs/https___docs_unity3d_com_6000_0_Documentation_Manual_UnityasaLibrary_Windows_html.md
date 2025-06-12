* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UnityasaLibrary-Windows.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Windows](https://docs.unity3d.com/6000.0/Documentation/Manual/Windows.html)
  * Integrating Unity into Windows applications


[](https://docs.unity3d.com/6000.0/Documentation/Manual/windows-requirements-and-compatibility.html)
Windows requirements and compatibility
[](https://docs.unity3d.com/6000.0/Documentation/Manual/playersettings-windows.html)
Windows Player settings
# Integrating Unity into Windows applications
You can use the Unity as a Library feature to integrate the Unity Runtime Library in Windows applications.
This feature enables you to include Unity-powered features in your application, such as: 
  * 3D/2D Real-Time Rendering
  * **AR** Augmented Reality [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AROverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AR) Experience
  * 3D model interaction
  * 2D mini-games


The Unity Runtime Library exposes controls to manage when and how to load, activate, and unload content within the application.
On Windows, you can embed a Unity build into your application in the following ways:
  * Launch Unity as an external build from your application and specify a window in which Unity will initialize and render with the `-parentHWND` [command line argument](https://docs.unity3d.com/6000.0/Documentation/Manual/PlayerCommandLineArguments.html). This is the easier option.
  * Embed Unity within your existing operating system process. To do this, call into `UnityPlayer.dll`, which any Win32 application can load directly. The entry point signature is:
`extern "C" UNITY_API int UnityMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPWSTR lpCmdLine, int nShowCmd);`


Use `lpCmdLine` to pass any command line arguments to Unity, for example, to control resolution, job threads or parent HWND. This enables you to run Unity within your process. For other valid Unity player command line arguments you can use, see [Unity Standalone Player command line arguments](https://docs.unity3d.com/6000.0/Documentation/Manual/PlayerCommandLineArguments.html).
## Additional resources:
  * [Using Unity as a Library in other applications](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityasaLibrary.html)
  * [Unity Standalone Player command line arguments](https://docs.unity3d.com/6000.0/Documentation/Manual/PlayerCommandLineArguments.html)


* * *
  * Unity as a Library added in [2019.3](https://docs.unity3d.com/Manual/30_search.html?q=newin20193).


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/windows-requirements-and-compatibility.html)
Windows requirements and compatibility
[](https://docs.unity3d.com/6000.0/Documentation/Manual/playersettings-windows.html)
Windows Player settings
