* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AwaitableCompletionSource_1.html

# AwaitableCompletionSource<T0>
class in UnityEngine
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
Objects allowing to control completion of an Awaitable object from user code.
### Properties
Property | Description  
---|---  
[Awaitable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AwaitableCompletionSource_1.Awaitable.html) | Get the awaitable controlled by the completion source.  
### Public Methods
Method | Description  
---|---  
[Reset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AwaitableCompletionSource_1.Reset.html) | Reset the completion source (this will set the Awaitable property to a new Awaitable object).  
[SetCanceled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AwaitableCompletionSource_1.SetCanceled.html) | Raise cancellation.  
[SetException](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AwaitableCompletionSource_1.SetException.html) | Raise completion with an exception.  
[SetResult](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AwaitableCompletionSource_1.SetResult.html) | Raise completion.  
[TrySetCanceled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AwaitableCompletionSource_1.TrySetCanceled.html) | Raise cancellation (returns false if the awaitable was already completed or canceled).  
[TrySetException](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AwaitableCompletionSource_1.TrySetException.html) | Raise completion with an exception.  
[TrySetResult](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AwaitableCompletionSource_1.TrySetResult.html) | Raise the awaitable completion.  
* * *
