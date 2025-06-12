* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.DownloadAssetPackAsyncOperation.html

# DownloadAssetPackAsyncOperation
class in UnityEngine.Android
/
Inherits from:[CustomYieldInstruction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomYieldInstruction.html)
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
Represents an asynchronous Android asset pack download operation. [AndroidAssetPacks.DownloadAssetPackAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPacks.DownloadAssetPackAsync.html) returns an instance of this class.
You can yield until the operation completes, or manually check whether it's done using isDone or keepWaiting properties. You can also track the progress of the operation using the progress property. Additional resources: [AndroidAssetPacks.DownloadAssetPackAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPacks.DownloadAssetPackAsync.html).
### Properties
Property | Description  
---|---  
[downloadedAssetPacks](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.DownloadAssetPackAsyncOperation-downloadedAssetPacks.html) | Gets the names of Android asset packs downloaded by this operation.  
[downloadFailedAssetPacks](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.DownloadAssetPackAsyncOperation-downloadFailedAssetPacks.html) | Gets the names of Android asset packs that failed to download.  
[isDone](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.DownloadAssetPackAsyncOperation-isDone.html) | Checks if the operation is finished.  
[keepWaiting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.DownloadAssetPackAsyncOperation-keepWaiting.html) | Checks if the operation is still running.  
[progress](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.DownloadAssetPackAsyncOperation-progress.html) | Gets the progress of the operation.  
### Inherited Members
### Properties
Property | Description  
---|---  
[keepWaiting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomYieldInstruction-keepWaiting.html) | Indicates if coroutine should be kept suspended.  
* * *
