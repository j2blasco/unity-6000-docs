* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.AndroidJNIModule.html

# UnityEngine.AndroidJNIModule
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
AndroidJNI module allows you to call Java code.
Additional resources: [Best practices](https://docs.unity3d.com/6000.0/Documentation/Manual/android-plugins-java-code-from-c-sharp.html#best-practices)
### Classes
Class | Description  
---|---  
[AndroidApplication](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidApplication.html) | Use this class to access the runtime data of your Android application.  
[AndroidAssetPackInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPackInfo.html) | Represents the download progress of a single Android asset pack.  
[AndroidAssetPacks](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPacks.html) | Provides methods for handling Android asset packs.  
[AndroidAssetPackState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPackState.html) | Represents the state of a single Android asset pack.  
[AndroidAssetPackUseMobileDataRequestResult](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPackUseMobileDataRequestResult.html) | Represents the choice of an end user that indicates if your application can use mobile data to download Android asset packs.  
[AndroidConfiguration](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidConfiguration.html) | Use this class to retrieve device specific configuration information.  
[AndroidDevice](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidDevice.html) | Interface into Android specific functionality.  
[AndroidGame](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidGame.html) | Provides methods and properties for accessing different Android game APIs.  
[AndroidJavaClass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaClass.html) | AndroidJavaClass is the Unity representation of a generic instance of java.lang.Class.  
[AndroidJavaObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaObject.html) | AndroidJavaObject is the Unity representation of a generic instance of java.lang.Object.  
[AndroidJavaProxy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaProxy.html) | This class can be used to implement any java interface. Any java vm method invocation matching the interface on the proxy object will automatically be passed to the c# implementation.  
[AndroidJNI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJNI.html) | 'Raw' JNI interface to Android Java VM from Unity scripting (C#).Note: Using raw JNI functions requires advanced knowledge of the Android Java Native Interface (JNI). Please take note.  
[AndroidJNIHelper](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJNIHelper.html) | Helper interface for JNI interaction; signature creation and method lookups.Note: Using raw JNI functions requires advanced knowledge of the Android Java Native Interface (JNI). Please take note.  
[AndroidLocale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidLocale.html) | Use this class to retrieve the language and region preferences set on the device.  
[ApplicationExitInfoProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.ApplicationExitInfoProvider.html) | Access point to get the list of ApplicationExitInfo records with the reasons for the most recent application terminations.  
[DiagnosticsReporting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.DiagnosticsReporting.html) | Class with options for reporting diagnostics information to the Android system.  
[DownloadAssetPackAsyncOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.DownloadAssetPackAsyncOperation.html) | Represents an asynchronous Android asset pack download operation. AndroidAssetPacks.DownloadAssetPackAsync returns an instance of this class.  
[GetAssetPackStateAsyncOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.GetAssetPackStateAsyncOperation.html) | Represents an asynchronous Android asset pack state request operation. AndroidAssetPacks.GetAssetPackStateAsync returns an instance of this class.  
[PermissionCallbacks](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.PermissionCallbacks.html) | Contains callbacks invoked when permission request is executed using Permission.RequestUserPermission.  
[RequestToUseMobileDataAsyncOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.RequestToUseMobileDataAsyncOperation.html) | Represents an asynchronous operation that requests to use mobile data to download Android asset packs.  
### Structs
Struct | Description  
---|---  
[JNINativeMethod](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JNINativeMethod.html) | Defines a single method to beregistered using AndroidJNI.RegisterNatives.  
[Permission](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.Permission.html) | Structure describing a permission that requires user authorization.  
### Enumerations
Enumeration | Description  
---|---  
[AndroidAssetPackError](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPackError.html) | Values that indicate the type of Android asset pack error when the status is either AndroidAssetPackStatus.Failed or AndroidAssetPackStatus.Unknown.  
[AndroidAssetPackStatus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPackStatus.html) | Values that indicate the status of an Android asset pack.  
[AndroidColorModeHdr](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidColorModeHdr.html) | Options to indicate whether the screen can display a wide range brightness levels.  
[AndroidColorModeWideColorGamut](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidColorModeWideColorGamut.html) | Options to indicate whether the screen can display wide range of color gamut or not.  
[AndroidGameMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidGameMode.html) | Options for the available game modes that AndroidGame.GameMode can return.  
[AndroidGameState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidGameState.html) | Options for the available game states that you can pass to AndroidGame.SetGameState or you can set as a current game state mode to be used for Automated game state hinting in Unity using AndroidGame.Automatic.SetGameState method.  
[AndroidHardwareKeyboardHidden](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidHardwareKeyboardHidden.html) | Options to indicate whether the physical keyboard is available.  
[AndroidHardwareType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidHardwareType.html) | AndroidHardwareType describes the type of Android device on which the app is running.  
[AndroidKeyboard](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidKeyboard.html) | Options to indicate the type of keyboard the device is using.  
[AndroidKeyboardHidden](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidKeyboardHidden.html) | Options to indicate whether any keyboard is available for use on the device.  
[AndroidNavigation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidNavigation.html) | Options to indicate the type of navigation methods used on the device.  
[AndroidNavigationHidden](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidNavigationHidden.html) | Options to indicate whether the 5-way or DPAD navigation methods are available on the device.  
[AndroidOrientation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidOrientation.html) | Options to indicate the orientation of the screen.  
[AndroidScreenLayoutDirection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidScreenLayoutDirection.html) | Options to indicate the screen layout direction.  
[AndroidScreenLayoutLong](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidScreenLayoutLong.html) | Options to indicate whether the aspect ratio of the screen is taller or wider than normal.  
[AndroidScreenLayoutRound](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidScreenLayoutRound.html) | Options to indicate whether the screen shape is rounded or not.  
[AndroidScreenLayoutSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidScreenLayoutSize.html) | Options to indicate the size of the device screen.  
[AndroidTouchScreen](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidTouchScreen.html) | Options to indicate whether the device supports touchscreen.  
[AndroidUIModeNight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidUIModeNight.html) | Options to indicate whether the device screen is in a special mode, such as a night mode.  
[AndroidUIModeType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidUIModeType.html) | Options to indicate the user interface mode of the device.  
[ExitReason](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.ExitReason.html) | The reason code for termination of the process.  
[ProcessImportance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.ProcessImportance.html) | Indicates the relative importance level that the system assigns to the process. These levels are represented by constants. The constants are numbered in such a way that more important values are always smaller than the less important values.  
* * *
