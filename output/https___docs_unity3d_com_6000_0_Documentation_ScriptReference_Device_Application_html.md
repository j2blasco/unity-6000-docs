* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application.html

# Application
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
Access to platform-specific application runtime data.
This class has the same functionality as [Application](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.html) and also mimics platform-specific behavior in the Unity Editor. Use it together with the Device Simulator to test platform-specific behaviors inside the Editor. Outside of the Editor, this class behaves exactly like the [Application](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.html) class. Unity strips all simulation capabilities during the build process. Use the original [Application](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.html) class if you work directly with the Unity Editor (for example, to create a custom Editor tool) and you don't need to use any simulated values.
### Static Properties
Property | Description  
---|---  
[absoluteURL](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application-absoluteURL.html) | This has the same functionality as Application.absoluteURL. At the moment, the Device Simulator doesn't support simulation of this property.  
[backgroundLoadingPriority](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application-backgroundLoadingPriority.html) | This has the same functionality as Application.backgroundLoadingPriority. At the moment, the Device Simulator doesn't support simulation of this property.  
[buildGUID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application-buildGUID.html) | This has the same functionality as Application.buildGUID. At the moment, the Device Simulator doesn't support simulation of this property.  
[cloudProjectId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application-cloudProjectId.html) | This has the same functionality as Application.cloudProjectId. At the moment, the Device Simulator doesn't support simulation of this property.  
[companyName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application-companyName.html) | This has the same functionality as Application.companyName. At the moment, the Device Simulator doesn't support simulation of this property.  
[consoleLogPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application-consoleLogPath.html) | This has the same functionality as Application.consoleLogPath. At the moment, the Device Simulator doesn't support simulation of this property.  
[dataPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application-dataPath.html) | This has the same functionality as Application.dataPath. At the moment, the Device Simulator doesn't support simulation of this property.  
[exitCancellationToken](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application-exitCancellationToken.html) | Cancellation token raised on exiting play mode (editor) or on quitting the application (Read Only).  
[genuine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application-genuine.html) | This has the same functionality as Application.genuine. At the moment, the Device Simulator doesn't support simulation of this property.  
[genuineCheckAvailable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application-genuineCheckAvailable.html) | This has the same functionality as Application.genuineCheckAvailable. At the moment, the Device Simulator doesn't support simulation of this property.  
[identifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application-identifier.html) | This has the same functionality as Application.identifier. At the moment, the Device Simulator doesn't support simulation of this property.  
[installerName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application-installerName.html) | This has the same functionality as Application.installerName. At the moment, the Device Simulator doesn't support simulation of this property.  
[installMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application-installMode.html) | This has the same functionality as Application.installMode. At the moment, the Device Simulator doesn't support simulation of this property.  
[internetReachability](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application-internetReachability.html) | This has the same functionality as Application.internetReachability and also mimics platform-specific behavior in the Unity Editor.  
[isBatchMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application-isBatchMode.html) | This has the same functionality as Application.isBatchMode. At the moment, the Device Simulator doesn't support simulation of this property.  
[isConsolePlatform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application-isConsolePlatform.html) | This has the same functionality as Application.isConsolePlatform and also mimics platform-specific behavior in the Unity Editor.  
[isEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application-isEditor.html) | This has the same functionality as Application.isEditor and also mimics platform-specific behavior in the Unity Editor.  
[isFocused](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application-isFocused.html) | This has the same functionality as Application.isFocused. At the moment, the Device Simulator doesn't support simulation of this property.  
[isMobilePlatform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application-isMobilePlatform.html) | This has the same functionality as Application.isMobilePlatform and also mimics platform-specific behavior in the Unity Editor.  
[isPlaying](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application-isPlaying.html) | This has the same functionality as Application.isPlaying. At the moment, the Device Simulator doesn't support simulation of this property.  
[persistentDataPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application-persistentDataPath.html) | This has the same functionality as Application.persistentDataPath. At the moment, the Device Simulator doesn't support simulation of this property.  
[platform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application-platform.html) | This has the same functionality as Application.platform and also mimics platform-specific behavior in the Unity Editor.  
[productName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application-productName.html) | This has the same functionality as Application.productName. At the moment, the Device Simulator doesn't support simulation of this property.  
[runInBackground](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application-runInBackground.html) | This has the same functionality as Application.runInBackground. At the moment, the Device Simulator doesn't support simulation of this property.  
[sandboxType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application-sandboxType.html) | This has the same functionality as Application.sandboxType. At the moment, the Device Simulator doesn't support simulation of this property.  
[streamingAssetsPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application-streamingAssetsPath.html) | This has the same functionality as Application.streamingAssetsPath. At the moment, the Device Simulator doesn't support simulation of this property.  
[systemLanguage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application-systemLanguage.html) | This has the same functionality as Application.systemLanguage and also mimics platform-specific behavior in the Unity Editor.  
[targetFrameRate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application-targetFrameRate.html) | This has the same functionality as Application.targetFrameRate. At the moment, the Device Simulator doesn't support simulation of this property.  
[temporaryCachePath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application-temporaryCachePath.html) | This has the same functionality as Application.temporaryCachePath. At the moment, the Device Simulator doesn't support simulation of this property.  
[unityVersion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application-unityVersion.html) | This has the same functionality as Application.unityVersion. At the moment, the Device Simulator doesn't support simulation of this property.  
[version](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application-version.html) | This has the same functionality as Application.version. At the moment, the Device Simulator doesn't support simulation of this property.  
### Static Methods
Method | Description  
---|---  
[CanStreamedLevelBeLoaded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application.CanStreamedLevelBeLoaded.html) | This has the same functionality as Application.CanStreamedLevelBeLoaded. At the moment, the Device Simulator doesn't support simulation of this method.  
[GetStackTraceLogType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application.GetStackTraceLogType.html) | This has the same functionality as Application.GetStackTraceLogType. At the moment, the Device Simulator doesn't support simulation of this method.  
[HasProLicense](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application.HasProLicense.html) | This has the same functionality as Application.HasProLicense. At the moment, the Device Simulator doesn't support simulation of this method.  
[HasUserAuthorization](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application.HasUserAuthorization.html) | This has the same functionality as Application.HasUserAuthorization. At the moment, the Device Simulator doesn't support simulation of this method.  
[IsPlaying](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application.IsPlaying.html) | This has the same functionality as Application.IsPlaying. At the moment, the Device Simulator doesn't support simulation of this method.  
[OpenURL](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application.OpenURL.html) | This has the same functionality as Application.OpenURL. At the moment, the Device Simulator doesn't support simulation of this method.  
[Quit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application.Quit.html) | This has the same functionality as Application.Quit. At the moment, the Device Simulator doesn't support simulation of this method.  
[RequestAdvertisingIdentifierAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application.RequestAdvertisingIdentifierAsync.html) | This has the same functionality as Application.RequestAdvertisingIdentifierAsync. At the moment, the Device Simulator doesn't support simulation of this method.  
[RequestUserAuthorization](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application.RequestUserAuthorization.html) | This has the same functionality as Application.RequestUserAuthorization. At the moment, the Device Simulator doesn't support simulation of this method.  
[SetStackTraceLogType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application.SetStackTraceLogType.html) | This has the same functionality as Application.SetStackTraceLogType. At the moment, the Device Simulator doesn't support simulation of this method.  
[Unload](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application.Unload.html) | This has the same functionality as Application.Unload. At the moment, the Device Simulator doesn't support simulation of this method.  
### Events
Event | Description  
---|---  
[deepLinkActivated](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application-deepLinkActivated.html) | This has the same functionality as Application.deepLinkActivated. At the moment, the Device Simulator doesn't support simulation of this event.  
[focusChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application-focusChanged.html) | This has the same functionality as Application.focusChanged. At the moment, the Device Simulator doesn't support simulation of this event.  
[logMessageReceived](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application-logMessageReceived.html) | This has the same functionality as Application.logMessageReceived. At the moment, the Device Simulator doesn't support simulation of this event.  
[logMessageReceivedThreaded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application-logMessageReceivedThreaded.html) | This has the same functionality as Application.logMessageReceivedThreaded. At the moment, the Device Simulator doesn't support simulation of this event.  
[lowMemory](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application-lowMemory.html) | This has the same functionality as Application.lowMemory and also mimics platform-specific behavior in the Unity Editor.  
[memoryUsageChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application-memoryUsageChanged.html) | This has the same functionality as Application.memoryUsageChanged.  
[onBeforeRender](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application-onBeforeRender.html) | This has the same functionality as Application.onBeforeRender. At the moment, the Device Simulator doesn't support simulation of this event.  
[quitting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application-quitting.html) | This has the same functionality as Application.quitting. At the moment, the Device Simulator doesn't support simulation of this event.  
[unloading](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application-unloading.html) | This has the same functionality as Application.unloading. At the moment, the Device Simulator doesn't support simulation of this event.  
[wantsToQuit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application-wantsToQuit.html) | This has the same functionality as Application.wantsToQuit. At the moment, the Device Simulator doesn't support simulation of this event.  
* * *
