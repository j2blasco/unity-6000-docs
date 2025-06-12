* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/deep-linking-universal-windows-platform.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Universal Windows Platform](https://docs.unity3d.com/6000.0/Documentation/Manual/WindowsStore.html)
  * [Develop for Universal Windows Platform](https://docs.unity3d.com/6000.0/Documentation/Manual/uwp-developing.html)
  * Use deep linking on UWP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/uwp-developing.html)
Develop for Universal Windows Platform
[](https://docs.unity3d.com/6000.0/Documentation/Manual/windowsstore-profiler.html)
Connect the profiler to UWP
# Use deep linking on UWP
Deep links are URL links outside of your application that direct users to a location in your application. When the user clicks a deep link for an application, the operating system opens the Unity application at a specified place (for example, a specific scene). You can enable deep linking for Universal Windows Platform (UWP) applications. For more information about deep links and how to use them, refer to [Deep links](https://docs.unity3d.com/6000.0/Documentation/Manual/deep-linking.html).
## Enable deep linking for UWP applications
Before you can process deep links, you need to configure your application to react to them by adding a custom URI scheme.
To add a custom URI scheme, perform the following steps:
  1. Go to **Edit** > **Project Settings** > **Player Settings**.
  2. Select UWP to open the [UWP Player Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsWSA.html) window.
  3. Select **Publishing Settings** > **Protocol**.
  4. In the **Name** field, enter the URI to associate with your application. For example, `unitydl`.


Your UWP application now opens when the device processes any link that starts with `unitydl://`.
## Use deep linking on UWP
After you enable deep links for Universal Windows Platform, the way that you use them is platform-agnostic. For information on how to handle deep links when your application opens, refer to [Using deep links](https://docs.unity3d.com/6000.0/Documentation/Manual/deep-linking.html#using-deep-links).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/uwp-developing.html)
Develop for Universal Windows Platform
[](https://docs.unity3d.com/6000.0/Documentation/Manual/windowsstore-profiler.html)
Connect the profiler to UWP
