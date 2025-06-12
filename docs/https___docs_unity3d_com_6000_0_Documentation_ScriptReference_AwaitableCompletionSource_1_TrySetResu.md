* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AwaitableCompletionSource_1.TrySetResult.html

#  [AwaitableCompletionSource<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AwaitableCompletionSource_1.html).TrySetResult
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
public bool TrySetResult(ref T value); 
### Parameters
Parameter | Description  
---|---  
value | Value to pass to the awaitable continuation.  
### Returns
**bool** Indicates if the completion was successfully raised. 
### Description
Raise the awaitable completion.
* * *
