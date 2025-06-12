* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncInstantiateOperation.html

# AsyncInstantiateOperation
class in UnityEngine
/
Inherits from:[AsyncOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncOperation.html)
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
Asynchronous instantiate operation on UnityEngine.Object type.
The operation is used by Object.InstantiateAsync internally and usually wrapped by AsyncInstantiateOperation<T>.
### Properties
Property | Description  
---|---  
[Result](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncInstantiateOperation.Result.html) | If isDone is true, then Result contains the instantiated objects. The size of the array is the same as the 'count' argument for the InstantiateAsync call.  
### Public Methods
Method | Description  
---|---  
[Cancel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncInstantiateOperation.Cancel.html) | Method that cancels all the operations connected to the asynchronous instantiation if the operation is not done yet, that is, where isDone == false. This method deletes all the objects created so far, which are not visible to users while they're not activated, and stops all the internal jobs connected to the operation.  
[IsWaitingForSceneActivation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncInstantiateOperation.IsWaitingForSceneActivation.html) | This property can be true only if allowSceneActivation is set to false, and if the operation has already completed everything needed for object instantiation except for the main thread integrating the objects and calling their Awake methods. Users can set allowSceneActivation to true to trigger the activation or call the Cancel method to cancel instantiation.  
[WaitForCompletion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncInstantiateOperation.WaitForCompletion.html) | Blocks the current thread until this operation is done.  
### Static Methods
Method | Description  
---|---  
[GetIntegrationTimeMS](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncInstantiateOperation.GetIntegrationTimeMS.html) | Gets the target duration allowed per frame to integrate instantiated object operations, in milliseconds.  
[SetIntegrationTimeMS](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncInstantiateOperation.SetIntegrationTimeMS.html) | Sets the target duration allowed per frame to integrate instantiated object operations, in milliseconds.  
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
