* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IVisualElementScheduler.Execute.html

#  [IVisualElementScheduler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IVisualElementScheduler.html).Execute
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
public [UIElements.IVisualElementScheduledItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IVisualElementScheduledItem.html) Execute(Action<TimerState> timerUpdateEvent); 
### Parameters
Parameter | Description  
---|---  
timerUpdateEvent | The action to be executed.  
### Returns
**IVisualElementScheduledItem** Reference to the scheduled action. 
### Description
Schedule this action to be executed later. 
* * *
## Declaration
public [UIElements.IVisualElementScheduledItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IVisualElementScheduledItem.html) Execute([Unity.Android.Gradle.Manifest.Action](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) updateEvent); 
### Parameters
Parameter | Description  
---|---  
updateEvent | The action to be executed.  
### Returns
**IVisualElementScheduledItem** Reference to the scheduled action. 
### Description
Schedule this action to be executed later. 
* * *
