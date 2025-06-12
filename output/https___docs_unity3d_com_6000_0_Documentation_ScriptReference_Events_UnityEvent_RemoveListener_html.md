* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEvent.RemoveListener.html

#  [UnityEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEvent.html).RemoveListener
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
public void RemoveListener([Events.UnityAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityAction.html) call); 
### Parameters
Parameter | Description  
---|---  
call | Callback function.  
### Description
Remove a non persistent listener from the UnityEvent. If you have added the same listener multiple times, this method will remove all occurrences of it.
Use this to remove a runtime callback.
* * *
