* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPackStatus.html

# AndroidAssetPackStatus
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
Values that indicate the status of an Android asset pack.
Unity always returns the status value and the error together in AndroidAssetPackInfo or AndroidAssetPackState objects. Unity returns these objects via callback methods after you call either AndroidAssetPacks.DownloadAssetPackAsync or AndroidAssetPacks.GetAssetPackStateAsync. When the status value is AndroidAssetPackStatus.Failed or AndroidAssetPackStatus.Unknown, the error value indicates the cause of the failure. For any other status value, the error value should always be AndroidAssetPackError.NoError. This enum directly wraps the [AssetPackStatus](https://developer.android.com/reference/com/google/android/play/core/assetpacks/model/AssetPackStatus) values in the PlayCore API. Additional resources: [AndroidAssetPackInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPackInfo.html), [AndroidAssetPacks.DownloadAssetPackAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPacks.DownloadAssetPackAsync.html), [AndroidAssetPacks.GetAssetPackStateAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPacks.GetAssetPackStateAsync.html), [AndroidAssetPackState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPackState.html).
### Properties
Property | Description  
---|---  
[Unknown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPackStatus.Unknown.html) | Indicates that the Android asset pack is not available for the application.  
[Pending](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPackStatus.Pending.html) | Indicates that the Android asset pack status should soon change.  
[Downloading](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPackStatus.Downloading.html) | Indicates that the device is downloading the Android asset pack.  
[Transferring](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPackStatus.Transferring.html) | Indicates that the device has downloaded the Android asset pack and is unpacking the asset pack to its final location.  
[Completed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPackStatus.Completed.html) | Indicates that the device has downloaded the Android asset pack and the asset pack is available to the application.  
[Failed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPackStatus.Failed.html) | Indicates that the device failed to download the Android asset pack.  
[Canceled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPackStatus.Canceled.html) | Indicates that the Android asset pack download is canceled.  
[WaitingForWifi](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPackStatus.WaitingForWifi.html) | Indicates that the device has paused the Android asset pack download until it connects to the WiFi network.  
[NotInstalled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPackStatus.NotInstalled.html) | Indicates that the Android asset pack is not installed.  
* * *
