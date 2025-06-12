* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/android-API.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android.html)
  * [Developing for Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-developing.html)
  * Android mobile scripting


[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-developing.html)
Developing for Android
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-input.html)
Input for Android devices
# Android mobile scripting
For cross-platform Projects, use the `UNITY_ANDROID` define directive to conditionally compile Android-specific C# code. For more information, refer to [Platform dependent compilation](https://docs.unity3d.com/6000.0/Documentation/Manual/platform-dependent-compilation.html).
## Access device-specific features and properties
Applications can access most features of an Android device through the [Input](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.html) and [Handheld](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handheld.html) classes. For more information, see:
  * [Mobile device input](https://docs.unity3d.com/6000.0/Documentation/Manual/MobileInput.html)
  * [Mobile keyboard](https://docs.unity3d.com/6000.0/Documentation/Manual/MobileKeyboard.html)


### Vibration support
To trigger a vibration, call [Handheld.Vibrate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handheld.Vibrate.html). Devices without vibration hardware ignore this call.
### Activity indicator
Mobile operating systems have built-in activity indicators your application can use during slow operations. For more information, refer to [Handheld.StartActivityIndicator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handheld.StartActivityIndicator.html).
To access device-specific properties, use these APIs:
**Script** | **Device property**  
---|---  
[SystemInfo.deviceUniqueIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-deviceUniqueIdentifier.html) | Always returns the md5 of `ANDROID_ID`. For more information, see Android developer documentation on [ANDROID_ID](https://developer.android.com/reference/android/provider/Settings.Secure.html#ANDROID_ID).  
[SystemInfo.deviceName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-deviceName.html) | Returns the device name. For Android devices, Unity tries to read `device_name` and `bluetooth_name` from secure system settings. If these strings have no values, Unity returns `<unknown>`.  
[SystemInfo.deviceModel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-deviceModel.html) | Returns the device model. This often includes the manufacturer name and model number (for example, “LGE Nexus 5 or ”SAMSUNG-SM-G900A").  
[SystemInfo.operatingSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-operatingSystem.html) | Returns the operating system name and version.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-developing.html)
Developing for Android
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-input.html)
Input for Android devices
