* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/device-simulator-simulated-classes.html

  * [The Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-editor.html)
  * [Unity's interface](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheEditor.html)
  * [Device Simulator](https://docs.unity3d.com/6000.0/Documentation/Manual/device-simulator.html)
  * Simulated classes


[](https://docs.unity3d.com/6000.0/Documentation/Manual/device-simulator-view.html)
The Simulator view
[](https://docs.unity3d.com/6000.0/Documentation/Manual/device-simulator-adding-a-device.html)
Adding a device
# Simulated classes
The Device Simulator provides simulated classes, which you can use to test code that responds to device-specific behaviors in the Device Simulator.
The following simulated classes are in the UnityEngine.Device namespace:
  * [Application](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application.html)
  * [Screen](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Screen.html)
  * [SystemInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo.html)


These simulated classes have the same members as their regular UnityEngine namespace counterparts. You can use them anywhere in your codebase where you would normally use the regular classes. There is no performance impact, and you can use them in release builds.
In the Editor, when the Device Simulator is [active](https://docs.unity3d.com/6000.0/Documentation/Manual/device-simulator-introduction.html#limitations), the simulated classes mimic the platform-specific behaviors of the simulated device; for example, [Device.SystemInfo.operatingSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-operatingSystem.html) returns the Android or iOS version of the simulated device.
In a built application, or when the Device Simulator isn’t active, the simulated classes have the same behavior as their counterparts in the UnityEngine namespace.
Although the simulated classes have the same members as the regular classes, the Device Simulator doesn’t simulate every behavior. In the UnityEditor, members that the Device Simulator doesn’t simulate have the same behavior as their UnityEngine equivalent, which isn’t platform-dependent. For example, the Device Simulator doesn’t simulate [Device.Screen.brightness](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Screen-brightness.html). This means this member has the same in-Editor behavior as [UnityEngine.Screen.brightness](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-brightness.html), which always returns `1`. For information on which members the Device Simulator simulates, see the API documentation for:
  * [Device.Application](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application.html)
  * [Device.Screen](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Screen.html)
  * [Device.SystemInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo.html)


## Updating your scripts to use simulated classes
If you want to convert existing code to use classes from the UnityEngine.Device namespace, it’s best practice to use [alias directives](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/using-directive). For example:
```
using Screen = UnityEngine.Device.Screen;
using Application = UnityEngine.Device.Application;
using SystemInfo = UnityEngine.Device.SystemInfo;

```

This way you can change which class the entire file uses and not change every API call.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/device-simulator-view.html)
The Simulator view
[](https://docs.unity3d.com/6000.0/Documentation/Manual/device-simulator-adding-a-device.html)
Adding a device
