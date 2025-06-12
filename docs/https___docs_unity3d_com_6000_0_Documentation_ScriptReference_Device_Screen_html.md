* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Screen.html

# Screen
class in UnityEngine.Device
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
Access platform-specific display information.
This class has the same functionality as [Screen](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen.html) and also mimics platform-specific behavior in the Unity Editor. Use it together with the Device Simulator to test platform-specific behaviors inside the Editor. Outside of the Editor, this class behaves exactly like the [Screen](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen.html) class. Unity strips all simulation capabilities during the build process. Use the original [Screen](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen.html) class if you work directly with the Unity Editor (for example, to create a custom Editor tool) and you don't need to use any simulated values.
### Static Properties
Property | Description  
---|---  
[autorotateToLandscapeLeft](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Screen-autorotateToLandscapeLeft.html) | This has the same functionality as Screen.autorotateToLandscapeLeft and also mimics platform-specific behavior in the Unity Editor.  
[autorotateToLandscapeRight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Screen-autorotateToLandscapeRight.html) | This has the same functionality as Screen.autorotateToLandscapeRight and also mimics platform-specific behavior in the Unity Editor.  
[autorotateToPortrait](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Screen-autorotateToPortrait.html) | This has the same functionality as Screen.autorotateToPortrait and also mimics platform-specific behavior in the Unity Editor.  
[autorotateToPortraitUpsideDown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Screen-autorotateToPortraitUpsideDown.html) | This has the same functionality as Screen.autorotateToPortraitUpsideDown and also mimics platform-specific behavior in the Unity Editor.  
[brightness](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Screen-brightness.html) | This has the same functionality as Screen.brightness. At the moment, the Device Simulator doesn't support simulation of this property.  
[currentResolution](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Screen-currentResolution.html) | This has the same functionality as Screen.currentResolution and also mimics platform-specific behavior in the Unity Editor.  
[cutouts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Screen-cutouts.html) | This has the same functionality as Screen.cutouts and also mimics platform-specific behavior in the Unity Editor.  
[dpi](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Screen-dpi.html) | This has the same functionality as Screen.dpi and also mimics platform-specific behavior in the Unity Editor.  
[fullScreen](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Screen-fullScreen.html) | This has the same functionality as Screen.fullScreen and also mimics platform-specific behavior in the Unity Editor.  
[fullScreenMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Screen-fullScreenMode.html) | This has the same functionality as Screen.fullScreenMode and also mimics platform-specific behavior in the Unity Editor.  
[height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Screen-height.html) | This has the same functionality as Screen.height and also mimics platform-specific behavior in the Unity Editor.  
[mainWindowDisplayInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Screen-mainWindowDisplayInfo.html) | The Device Simulator doesn't simulate this property.  
[mainWindowPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Screen-mainWindowPosition.html) | The Device Simulator doesn't simulate this property.  
[msaaSamples](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Screen-msaaSamples.html) | This has the same functionality as Screen.msaaSamples and also mimics platform-specific behavior in the Unity Editor.  
[orientation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Screen-orientation.html) | This has the same functionality as Screen.orientation and also mimics platform-specific behavior in the Unity Editor.  
[resolutions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Screen-resolutions.html) | This has the same functionality as Screen.resolutions and also mimics platform-specific behavior in the Unity Editor.  
[safeArea](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Screen-safeArea.html) | This has the same functionality as Screen.safeArea and also mimics platform-specific behavior in the Unity Editor.  
[sleepTimeout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Screen-sleepTimeout.html) | This has the same functionality as Screen.sleepTimeout. At the moment, the Device Simulator doesn't support simulation of this property.  
[width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Screen-width.html) | This has the same functionality as Screen.width and also mimics platform-specific behavior in the Unity Editor.  
### Static Methods
Method | Description  
---|---  
[GetDisplayLayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Screen.GetDisplayLayout.html) | The Device Simulator doesn't simulate this property.  
[MoveMainWindowTo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Screen.MoveMainWindowTo.html) | The Device Simulator doesn't simulate this method.  
[SetMSAASamples](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Screen.SetMSAASamples.html) | This has the same functionality as Screen.SetMSAASamples and also mimics platform-specific behavior in the Unity Editor.  
[SetResolution](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Screen.SetResolution.html) | This has the same functionality as Screen.SetResolution and also mimics platform-specific behavior in the Unity Editor.  
* * *
