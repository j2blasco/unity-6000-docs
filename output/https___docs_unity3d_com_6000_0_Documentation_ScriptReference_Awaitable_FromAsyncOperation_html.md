* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Awaitable.FromAsyncOperation.html

#  [Awaitable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Awaitable.html).FromAsyncOperation
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
public static [Awaitable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Awaitable.html) FromAsyncOperation([AsyncOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncOperation.html) op, CancellationToken cancellationToken); 
### Parameters
Parameter | Description  
---|---  
op | Async operation object.  
cancellationToken | Optional cancellation token.  
### Description
Creates an Awaitable from an existing [AsyncOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncOperation.html) object.
* * *
