* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPacks.DownloadAssetPackAsync.html

#  [AndroidAssetPacks](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPacks.html).DownloadAssetPackAsync
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
## Declaration
public static [Android.DownloadAssetPackAsyncOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.DownloadAssetPackAsyncOperation.html) DownloadAssetPackAsync(string[] assetPackNames); 
### Parameters
Parameter | Description  
---|---  
assetPackNames | The array of names of Android asset packs to download.  
### Returns
**DownloadAssetPackAsyncOperation** Returns an object that represents the download operation. If you yield this object inside a coroutine, the coroutine pauses until the operation is complete. 
### Description
Downloads Android asset packs.
This method directly wraps Google's PlayCore plugin API. If the PlayCore plugin is missing, calling this method throws an InvalidOperationException exception. Additional resources: [DownloadAssetPackAsyncOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.DownloadAssetPackAsyncOperation.html), [AndroidAssetPackInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPackInfo.html), [AndroidAssetPacks.CancelAssetPackDownload](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPacks.CancelAssetPackDownload.html), [AndroidAssetPacks.GetAssetPackPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPacks.GetAssetPackPath.html), [AndroidAssetPacks.GetAssetPackStateAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPacks.GetAssetPackStateAsync.html), [AndroidAssetPacks.RemoveAssetPack](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPacks.RemoveAssetPack.html), [AndroidAssetPacks.RequestToUseMobileDataAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPacks.RequestToUseMobileDataAsync.html).
* * *
## Declaration
public static void DownloadAssetPackAsync(string[] assetPackNames, Action<AndroidAssetPackInfo> callback); 
### Parameters
Parameter | Description  
---|---  
assetPackNames | The array of names of Android asset packs to download.  
callback | The callback method to inform about download progress. It gets called multiple times for each asset pack during its download. The callback method must have a parameter of AndroidAssetPackInfo type. The default value is null.  
### Description
Downloads Android asset packs.
This method directly wraps Google's PlayCore plugin API. If the PlayCore plugin is missing, calling this method throws an InvalidOperationException exception. Additional resources: [AndroidAssetPackInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPackInfo.html), [AndroidAssetPacks.CancelAssetPackDownload](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPacks.CancelAssetPackDownload.html), [AndroidAssetPacks.GetAssetPackPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPacks.GetAssetPackPath.html), [AndroidAssetPacks.GetAssetPackStateAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPacks.GetAssetPackStateAsync.html), [AndroidAssetPacks.RemoveAssetPack](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPacks.RemoveAssetPack.html), [AndroidAssetPacks.RequestToUseMobileDataAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPacks.RequestToUseMobileDataAsync.html).
* * *
