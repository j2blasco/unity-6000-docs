* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Awaitable.WaitForSecondsAsync.html

#  [Awaitable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Awaitable.html).WaitForSecondsAsync
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
public static [Awaitable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Awaitable.html) WaitForSecondsAsync(float seconds, CancellationToken cancellationToken); 
### Parameters
Parameter | Description  
---|---  
seconds | Seconds to wait for.  
cancellationToken | Optional cancellation token.  
### Description
Resumes execution after the specified number of seconds.
**Note:** This method can only be called from the main thread and always completes on main thread.
```
async Awaitable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Awaitable.html) Foo(){
  await Awaitable.WaitForSecondsAsync[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Awaitable.WaitForSecondsAsync.html)(2);
  // Do something
  await Awaitable.WaitForSecondsAsync[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Awaitable.WaitForSecondsAsync.html)(2);
  // Do something else
}

```

* * *
