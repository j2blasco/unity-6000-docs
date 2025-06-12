* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPacks.html

# AndroidAssetPacks
class in UnityEngine.Android
/
Implemented in:[UnityEngine.AndroidJNIModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.AndroidJNIModule.html)
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
Provides methods for handling Android asset packs.
Methods in this class are either direct wrappers of java APIs in Google's PlayCore plugin, or depend on values that the PlayCore API returns. Therefore to use it, the gradle project must include the "com.google.android.play:core" dependency. If your project contains custom asset packs or you enable **Split Application Binary** in Player Settings, Unity automatically adds this dependency to the unityLibrary submodule's build.gradle file. If the PlayCore plugin is missing, calling any wrapper throws an InvalidOperationException exception. Note that PlayCore APIs only work with fast-follow and on-demand delivery type asset packs, therefore methods in this class have the same limitation.
### Static Properties
Property | Description  
---|---  
[coreUnityAssetPacksDownloaded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPacks-coreUnityAssetPacksDownloaded.html) | Checks if all core Unity asset packs are downloaded.  
### Static Methods
Method | Description  
---|---  
[CancelAssetPackDownload](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPacks.CancelAssetPackDownload.html) | Cancels Android asset pack downloads.  
[DownloadAssetPackAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPacks.DownloadAssetPackAsync.html) | Downloads Android asset packs.  
[GetAssetPackPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPacks.GetAssetPackPath.html) | Gets the full path to the location where the device stores the assets for the Android asset pack.  
[GetAssetPackStateAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPacks.GetAssetPackStateAsync.html) | Queries the state of Android asset packs.  
[GetCoreUnityAssetPackNames](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPacks.GetCoreUnityAssetPackNames.html) | Gets the name of every core Unity asset pack built for this application that use either the fast-follow or on-demand delivery type.  
[RemoveAssetPack](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPacks.RemoveAssetPack.html) | Removes Android asset pack.  
[RequestToUseMobileDataAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPacks.RequestToUseMobileDataAsync.html) | Requests to use mobile data to download Android asset packs.  
* * *
