* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.html

# Application
class in UnityEngine
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
Provides access to application runtime data.
This class contains static methods for looking up information about and controlling the runtime data.
### Static Properties
Property | Description  
---|---  
[absoluteURL](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-absoluteURL.html) | The URL of the document. For WebGL, this is a web URL. For Android, iOS, or Universal Windows Platform (UWP) this is a deep link URL (Read Only).  
[backgroundLoadingPriority](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-backgroundLoadingPriority.html) | Priority of background loading thread.  
[buildGUID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-buildGUID.html) | Returns a GUID for this build (Read Only).  
[cloudProjectId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-cloudProjectId.html) | A unique cloud project identifier. It is unique for every project (Read Only).  
[companyName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-companyName.html) | Returns application company name (Read Only).  
[consoleLogPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-consoleLogPath.html) | Returns the path to the console log file, or an empty string if the current platform does not support log files.  
[dataPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-dataPath.html) | Contains the path to the game data folder on the target device (Read Only).  
[exitCancellationToken](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-exitCancellationToken.html) | Cancellation token raised on exiting Play mode (Editor) or on quitting the application (Read Only).  
[genuine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-genuine.html) | Returns false if application is altered in any way after it was built.  
[genuineCheckAvailable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-genuineCheckAvailable.html) | Returns true if application integrity can be confirmed.  
[identifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-identifier.html) | Returns the application identifier at runtime.   
[installerName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-installerName.html) | Returns the name of the store or package that installed the application (Read Only).  
[installMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-installMode.html) | Returns application install mode (Read Only).  
[internetReachability](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-internetReachability.html) | Returns the type of internet reachability currently possible on the device.  
[isBatchMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-isBatchMode.html) | Returns true when Unity is launched with the -batchmode flag from the command line (Read Only).  
[isConsolePlatform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-isConsolePlatform.html) | Is the current Runtime platform a known console platform.  
[isEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-isEditor.html) | Whether the game is running inside the Unity Editor (Read Only).  
[isFocused](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-isFocused.html) | Whether the Player currently has focus (Read Only).  
[isMobilePlatform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-isMobilePlatform.html) | Identifies whether the current Runtime platform is a known mobile platform.  
[isPlaying](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-isPlaying.html) | Returns true when called in any kind of built Player, or when called in the Editor in Play mode (Read Only).  
[persistentDataPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-persistentDataPath.html) | Contains the path to a persistent data directory (Read-only).  
[platform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-platform.html) | Returns the platform the game is running on (Read Only).  
[productName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-productName.html) | Returns application product name (Read Only).  
[runInBackground](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-runInBackground.html) | Determines whether the Player should run when the application is in the background  
[sandboxType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-sandboxType.html) | Returns application running in a sandbox environment (Read-only).  
[streamingAssetsPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-streamingAssetsPath.html) | The path to the StreamingAssets folder (Read Only).  
[systemLanguage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-systemLanguage.html) | The language in which the user's operating system is running in.  
[targetFrameRate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-targetFrameRate.html) | Specifies the target frame rate at which Unity tries to render your game.  
[temporaryCachePath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-temporaryCachePath.html) | Contains the path to a temporary data / cache directory (Read Only).  
[unityVersion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-unityVersion.html) | The version of the Unity runtime used to play the content.  
[version](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-version.html) | Returns application version number (Read Only).  
### Static Methods
Method | Description  
---|---  
[CanStreamedLevelBeLoaded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.CanStreamedLevelBeLoaded.html) | Checks if the streamed level can be loaded.  
[GetStackTraceLogType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.GetStackTraceLogType.html) | Get stack trace logging options. The default value is StackTraceLogType.ScriptOnly.  
[HasProLicense](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.HasProLicense.html) | Is Unity activated with the Pro license?  
[HasUserAuthorization](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.HasUserAuthorization.html) | Check if the user has authorized use of the webcam or microphone on iOS and WebGL.  
[IsPlaying](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.IsPlaying.html) | Returns true if the given object is part of the playing world either in any kind of built Player or in Play Mode.  
[OpenURL](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.OpenURL.html) | Opens the URL specified, subject to the permissions and limitations of your app’s current platform and environment.   
[Quit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.Quit.html) | Quits the player application.  
[RequestAdvertisingIdentifierAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.RequestAdvertisingIdentifierAsync.html) | Request an advertising ID for iOS and UWP.  
[RequestUserAuthorization](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.RequestUserAuthorization.html) | Request authorization to use the webcam or microphone on iOS, and the webcam only on WebGL.  
[SetStackTraceLogType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.SetStackTraceLogType.html) | Set stack trace logging options. The default value is StackTraceLogType.ScriptOnly.  
[Unload](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.Unload.html) | Unloads the Unity Player.  
### Events
Event | Description  
---|---  
[deepLinkActivated](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-deepLinkActivated.html) | This event is raised when an application running on Android, iOS, or the Universal Windows Platform (UWP) is activated using a deep link URL.  
[focusChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-focusChanged.html) | Defines the delegate to use to register for events in which the focus gained or lost.  
[logMessageReceived](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-logMessageReceived.html) | Event that is fired if a log message is received.  
[logMessageReceivedThreaded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-logMessageReceivedThreaded.html) | Event that is fired if a log message is received.  
[lowMemory](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-lowMemory.html) | The Application._lowMemory event occurs when your application receives a low-memory notification from the device it is running on.   
[memoryUsageChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-memoryUsageChanged.html) | Informs about significant changes in the application's memory usage.  
[onBeforeRender](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-onBeforeRender.html) | A delegate method used to register for Just Before Render input updates for VR devices.  
[quitting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-quitting.html) | Unity raises this event when the Player application is quitting.  
[unloading](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-unloading.html) | Unity raises this event when the Player is unloading.  
[wantsToQuit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-wantsToQuit.html) | Unity raises this event when the Player application wants to quit.  
### Delegates
Delegate | Description  
---|---  
[AdvertisingIdentifierCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.AdvertisingIdentifierCallback.html) | Delegate method for fetching advertising ID.  
[LogCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.LogCallback.html) | Use this delegate type with Application.logMessageReceived or Application.logMessageReceivedThreaded to monitor what gets logged.  
[LowMemoryCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.LowMemoryCallback.html) | This is the delegate function when a mobile device notifies of low memory.  
[MemoryUsageChangedCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.MemoryUsageChangedCallback.html) | A delegate for the Application.memoryUsageChanged vent.  
* * *
