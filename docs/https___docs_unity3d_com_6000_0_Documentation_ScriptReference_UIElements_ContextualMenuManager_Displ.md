* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ContextualMenuManager.DisplayMenuIfEventMatches.html

#  [ContextualMenuManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ContextualMenuManager.html).DisplayMenuIfEventMatches
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
public void DisplayMenuIfEventMatches([UIElements.EventBase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EventBase.html) evt, [UIElements.IEventHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IEventHandler.html) eventHandler); 
### Parameters
Parameter | Description  
---|---  
evt | The event to inspect.  
eventHandler | The element for which the menu is displayed.  
### Description
Checks if the event triggers the display of the contextual menu. This method also displays the menu. 
This is an abstract method. Each concrete implementation of the ContextualMenuManager defines the events that will display the menu. 
* * *
