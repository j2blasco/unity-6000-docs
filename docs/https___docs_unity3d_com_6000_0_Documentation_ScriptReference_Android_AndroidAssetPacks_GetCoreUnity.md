* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPacks.GetCoreUnityAssetPackNames.html

#  [AndroidAssetPacks](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPacks.html).GetCoreUnityAssetPackNames
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
public static string[] GetCoreUnityAssetPackNames(); 
### Returns
**string[]** Returns an array of asset pack names for core Unity asset packs with the fast-follow or on-demand delivery type. If Unity did not create any core asset packs for this application with previously mentioned delivery types, or if the PlayCore plugin is missing, this returns an empty array. 
### Description
Gets the name of every core Unity asset pack built for this application that use either the fast-follow or on-demand delivery type.
Core Unity asset packs are asset packs that Unity created automatically when it built the Android app bundle. Unity only creates core asset packages if you enable **Split Application Binary** in Player Settings. This method uses PlayCore APIs, therefore it can only return names of asset packs that use the fast-follow or on-demand delivery types. If this method returns an empty array, to differentiate between the two potential causes, call coreUnityAssetPacksDownloaded. Asset pack names returned by this method can be passed to other methods such as QueryAssetPackState or DownloadAssetPackAsync to get status information or to start the download. However calling RemoveAssetPack with the names returned by this method does nothing. Additional resources: [AndroidAssetPacks.coreUnityAssetPacksDownloaded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPacks-coreUnityAssetPacksDownloaded.html), [AndroidAssetPacks.DownloadAssetPackAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPacks.DownloadAssetPackAsync.html), [AndroidAssetPacks.GetAssetPackStateAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPacks.GetAssetPackStateAsync.html).
* * *
