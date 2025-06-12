* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimePlatform.html

# RuntimePlatform
enumeration
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
### Description
The platform application is running. Returned by Application.platform.
**Note:** The difference between using RuntimePlatform and Platform dependent Compilation is that using RuntimePlatform is evaluated at runtime while Platform dependent Compilation is evaluated at compile time. So if you can use platform dependent compilation, don't hesitate to use it. In most cases, you can get the same functionality using both, and using the defines will produce smaller and faster code, as you don't need to check at runtime. There are some cases where RuntimePlatform is needed at runtime.
### Properties
Property | Description  
---|---  
[OSXEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimePlatform.OSXEditor.html) | In the Unity editor on macOS.  
[OSXPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimePlatform.OSXPlayer.html) | In the player on macOS.  
[WindowsPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimePlatform.WindowsPlayer.html) | In the player on Windows.  
[WindowsEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimePlatform.WindowsEditor.html) | In the Unity editor on Windows.  
[IPhonePlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimePlatform.IPhonePlayer.html) | In the player on the iPhone.  
[Android](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimePlatform.Android.html) | In the player on Android devices.  
[LinuxPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimePlatform.LinuxPlayer.html) | In the player on Linux.  
[LinuxEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimePlatform.LinuxEditor.html) | In the Unity editor on Linux.  
[WebGLPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimePlatform.WebGLPlayer.html) | In the player on WebGL  
[WSAPlayerX86](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimePlatform.WSAPlayerX86.html) | In the player on Windows Store Apps when CPU architecture is X86.  
[WSAPlayerX64](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimePlatform.WSAPlayerX64.html) | In the player on Windows Store Apps when CPU architecture is X64.  
[WSAPlayerARM](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimePlatform.WSAPlayerARM.html) | In the player on Windows Store Apps when CPU architecture is ARM.  
[PS4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimePlatform.PS4.html) | In the player on the Playstation 4.  
[XboxOne](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimePlatform.XboxOne.html) | In the player on Xbox One.  
[tvOS](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimePlatform.tvOS.html) | In the player on the Apple's tvOS.  
[Switch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimePlatform.Switch.html) | In the player on Nintendo Switch.  
[PS5](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimePlatform.PS5.html) | In the player on the Playstation 5.  
[LinuxServer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimePlatform.LinuxServer.html) | In the server on Linux.  
[WindowsServer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimePlatform.WindowsServer.html) | In the server on Windows.  
[OSXServer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimePlatform.OSXServer.html) | In the server on macOS.  
[VisionOS](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimePlatform.VisionOS.html) | In the player on visionOS.  
* * *
