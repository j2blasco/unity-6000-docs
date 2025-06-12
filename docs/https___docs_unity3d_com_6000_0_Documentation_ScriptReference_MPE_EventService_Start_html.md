* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.EventService.Start.html

#  [EventService](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.EventService.html).Start
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
public static void Start(); 
### Description
Starts the EventService so it listens to new messages.
Normally, Start is called automatically when a member of the EventService is invoked. However, you may sometimes need to call it explicitly. For example, if you called [EventService.Close](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.EventService.Close.html) you can use Start to restart the EventService.
* * *
