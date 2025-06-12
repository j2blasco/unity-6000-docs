* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Awaitable.FixedUpdateAsync.html

#  [Awaitable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Awaitable.html).FixedUpdateAsync
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
public static [Awaitable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Awaitable.html) FixedUpdateAsync(CancellationToken cancellationToken); 
### Description
Resumes execution on the next fixed update frame.
**Note:** This method can only be called from the main thread and always completes on main thread. Also, in the Editor, this Awaitable will only complete when the game is playing (it will never complete otherwise).
* * *
