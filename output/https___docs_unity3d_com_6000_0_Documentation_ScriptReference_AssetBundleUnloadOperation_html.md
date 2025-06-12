* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleUnloadOperation.html

# AssetBundleUnloadOperation
class in UnityEngine
/
Inherits from:[AsyncOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncOperation.html)
/
Implemented in:[UnityEngine.AssetBundleModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.AssetBundleModule.html)
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
Async unload operation for an [AssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html).
### Public Methods
Method | Description  
---|---  
[WaitForCompletion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleUnloadOperation.WaitForCompletion.html) | Synchronously waits for the operation to complete.  
### Inherited Members
### Properties
Property | Description  
---|---  
[allowSceneActivation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncOperation-allowSceneActivation.html) | Allow Scenes to be activated as soon as it is ready.  
[isDone](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncOperation-isDone.html) | Has the operation finished? (Read Only)  
[priority](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncOperation-priority.html) | Priority lets you tweak in which order async operation calls will be performed.  
[progress](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncOperation-progress.html) | What's the operation's progress. (Read Only)  
### Events
Event | Description  
---|---  
[completed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncOperation-completed.html) | Event that is invoked upon operation completion. An event handler that is registered in the same frame as the call that creates it will be invoked next frame, even if the operation is able to complete synchronously. If a handler is registered after the operation has completed and has already invoked the complete event, the handler will be called synchronously.  
* * *
