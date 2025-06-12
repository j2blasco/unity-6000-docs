* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPacks.GetAssetPackStateAsync.html

#  [AndroidAssetPacks](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPacks.html).GetAssetPackStateAsync
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
public static [Android.GetAssetPackStateAsyncOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.GetAssetPackStateAsyncOperation.html) GetAssetPackStateAsync(string[] assetPackNames); 
### Parameters
Parameter | Description  
---|---  
assetPackNames | The array of names of the Android asset packs to query the state of.  
### Returns
**GetAssetPackStateAsyncOperation** Returns an object that represents the query operation. If you yield this object inside a coroutine, the coroutine pauses until the operation is complete. 
### Description
Queries the state of Android asset packs.
This method directly wraps Google's PlayCore plugin API. If the PlayCore plugin is missing, calling this method throws an InvalidOperationException exception. Additional resources: [GetAssetPackStateAsyncOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.GetAssetPackStateAsyncOperation.html), [AndroidAssetPacks.DownloadAssetPackAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPacks.DownloadAssetPackAsync.html), [AndroidAssetPacks.GetAssetPackPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPacks.GetAssetPackPath.html).
* * *
## Declaration
public static void GetAssetPackStateAsync(string[] assetPackNames, Action<ulong,AndroidAssetPackState[]> callback); 
### Parameters
Parameter | Description  
---|---  
assetPackNames | The array of names of the Android asset packs to query the state of.  
callback | The callback method to get the result. Unity raises this callback once when the query is complete and the callback receives the state of queried Android asset packs. The callback method must have two parameters: 
  * A ulong type parameter which indicates the total size of the queried asset packs.
  * An array of AndroidAssetPackState which contains the state of each queried asset pack.

  
### Description
Queries the state of Android asset packs.
This method directly wraps Google's PlayCore plugin API. If the PlayCore plugin is missing, calling this method throws an InvalidOperationException exception. Additional resources: [AndroidAssetPackState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPackState.html), [AndroidAssetPacks.DownloadAssetPackAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPacks.DownloadAssetPackAsync.html), [AndroidAssetPacks.GetAssetPackPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPacks.GetAssetPackPath.html).
* * *
