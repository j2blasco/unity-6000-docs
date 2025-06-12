* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Application.InvokeOnUIThread.html

#  [Application](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Application.html).InvokeOnUIThread
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
public static void InvokeOnUIThread([WSA.AppCallbackItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.AppCallbackItem.html) item, bool waitUntilDone); 
### Parameters
Parameter | Description  
---|---  
item | Item to execute.  
waitUntilDone | Wait until item is executed.  
### Description
Executes callback item on UI thread.
More information on UI and application threads can be found [here](https://docs.unity3d.com/6000.0/Documentation/Manual/windowsstore-appcallbacks.html).
* * *
