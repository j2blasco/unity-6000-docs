* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.GetAssetPackStateAsyncOperation.html

# GetAssetPackStateAsyncOperation
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
Represents an asynchronous Android asset pack state request operation. [AndroidAssetPacks.GetAssetPackStateAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPacks.GetAssetPackStateAsync.html) returns an instance of this class.
You can yield until the operation completes, or manually check whether it's done using isDone or keepWaiting properties. Additional resources: [AndroidAssetPacks.GetAssetPackStateAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPacks.GetAssetPackStateAsync.html).
### Properties
Property | Description  
---|---  
[isDone](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.GetAssetPackStateAsyncOperation-isDone.html) | Checks if the operation is finished.  
[keepWaiting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.GetAssetPackStateAsyncOperation-keepWaiting.html) | Checks if the operation is still running.  
[size](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.GetAssetPackStateAsyncOperation-size.html) | Gets the total size in bytes of all Android asset packs that had their status checked by this operation.  
[states](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.GetAssetPackStateAsyncOperation-states.html) | Gets the states of all Android asset packs that had their status checked by this operation.  
### Inherited Members
### Properties
Property | Description  
---|---  
[keepWaiting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomYieldInstruction-keepWaiting.html) | Indicates if coroutine should be kept suspended.  
* * *
