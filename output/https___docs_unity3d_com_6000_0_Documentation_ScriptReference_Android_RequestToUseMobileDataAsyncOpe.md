* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.RequestToUseMobileDataAsyncOperation.html

# RequestToUseMobileDataAsyncOperation
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
Represents an asynchronous operation that requests to use mobile data to download Android asset packs.
[AndroidAssetPacks.RequestToUseMobileDataAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPacks.RequestToUseMobileDataAsync.html) returns an instance of this class. You can yield until the operation completes, or manually check whether it's done using isDone or keepWaiting properties. Additional resources: [AndroidAssetPacks.RequestToUseMobileDataAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPacks.RequestToUseMobileDataAsync.html).
### Properties
Property | Description  
---|---  
[isDone](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.RequestToUseMobileDataAsyncOperation-isDone.html) | Checks if the operation is finished.  
[keepWaiting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.RequestToUseMobileDataAsyncOperation-keepWaiting.html) | Checks if the operation is still running.  
[result](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.RequestToUseMobileDataAsyncOperation-result.html) | Indicates whether the end user allowed the application to use mobile data to download Android asset packs.  
### Inherited Members
### Properties
Property | Description  
---|---  
[keepWaiting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomYieldInstruction-keepWaiting.html) | Indicates if coroutine should be kept suspended.  
* * *
