* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PanelChangedEventBase_1.GetPooled.html

#  [PanelChangedEventBase<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PanelChangedEventBase_1.html).GetPooled
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
public static T GetPooled([UIElements.IPanel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPanel.html) originPanel, [UIElements.IPanel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPanel.html) destinationPanel); 
### Parameters
Parameter | Description  
---|---  
originPanel | Sets the originPanel property of the event.  
destinationPanel | Sets the destinationPanel property of the event.  
### Returns
**T** An initialized event. 
### Description
Gets an event from the event pool and initializes it with the given values. Use this function instead of creating new events. Events obtained using this method need to be released back to the pool. You can use `Dispose()` to release them. 
* * *
