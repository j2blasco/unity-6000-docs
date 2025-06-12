* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPackError.html

# AndroidAssetPackError
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
Values that indicate the type of Android asset pack error when the status is either AndroidAssetPackStatus.Failed or AndroidAssetPackStatus.Unknown.
Unity always returns the error value and the status together in AndroidAssetPackInfo or AndroidAssetPackState objects. Unity returns these objects via callback methods after you call either AndroidAssetPacks.DownloadAssetPackAsync or AndroidAssetPacks.GetAssetPackStateAsync. When the status value is AndroidAssetPackStatus.Failed or AndroidAssetPackStatus.Unknown, the error value indicates the cause of the failure. For any other status value, the error value should always be AndroidAssetPackError.NoError. This enum directly wraps the [AssetPackErrorCode](https://developer.android.com/reference/com/google/android/play/core/assetpacks/model/AssetPackErrorCode) values in the PlayCore API. Additional resources: [AndroidAssetPackInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPackInfo.html), [AndroidAssetPacks.DownloadAssetPackAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPacks.DownloadAssetPackAsync.html), [AndroidAssetPacks.GetAssetPackStateAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPacks.GetAssetPackStateAsync.html), [AndroidAssetPackState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPackState.html).
### Properties
Property | Description  
---|---  
[NoError](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPackError.NoError.html) | Indicates that there is no error.  
[AppUnavailable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPackError.AppUnavailable.html) | Indicates that this application is unavailable in the Google's Play Store.  
[PackUnavailable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPackError.PackUnavailable.html) | Indicates that the requested Android asset pack is not available in the Google Play Store.  
[InvalidRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPackError.InvalidRequest.html) | Indicates that the request was invalid.  
[DownloadNotFound](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPackError.DownloadNotFound.html) | Indicates that the requested download is not found.  
[ApiNotAvailable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPackError.ApiNotAvailable.html) | Indicates that the Asset Delivery API is not available.  
[NetworkError](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPackError.NetworkError.html) | Indicates that the Android asset pack is not accessible because there was an error related to the network connection.  
[AccessDenied](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPackError.AccessDenied.html) | Indicates that the application does not have permission to download asset packs under the current device circumstances.  
[InsufficientStorage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPackError.InsufficientStorage.html) | Indicates that there is not enough storage space on the device to download the Android asset pack.  
[PlayStoreNotFound](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPackError.PlayStoreNotFound.html) | Indicates that the device does not have the Play Store application installed or has an unofficial version.  
[NetworkUnrestricted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPackError.NetworkUnrestricted.html) | Indicates that the app requested to use mobile data while there were no Android asset packs waiting for WiFi.  
[AppNotOwned](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPackError.AppNotOwned.html) | Indicates that the end user does not own the application on the device.  
[InternalError](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPackError.InternalError.html) | Indicates that unknown error occured while downloading an asset pack.  
* * *
