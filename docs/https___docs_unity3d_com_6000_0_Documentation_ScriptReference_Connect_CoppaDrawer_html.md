* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Connect.CoppaDrawer.html

# CoppaDrawer
class in UnityEditor.Connect
Leave feedback
  

Implements interfaces:[IProjectEditorDrawer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Connect.IProjectEditorDrawer.html)
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
### Description
A container that fetches the UIElements that draw the COPPA compliance UI and subscribes to its events.
### Constructors
Constructor | Description  
---|---  
[CoppaDrawer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Connect.CoppaDrawer-ctor.html) | The default constructor for the COPPA UI drawer that subscribes to the callback events for the Cancel and Save buttons.  
### Public Methods
Method | Description  
---|---  
[Dispose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Connect.CoppaDrawer.Dispose.html) | Disposes of the UI.  
[GetVisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Connect.CoppaDrawer.GetVisualElement.html) | A method that retrieves the Coppa compliance UI.  
### Events
Event | Description  
---|---  
[exceptionCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Connect.CoppaDrawer-exceptionCallback.html) | An event that fires when an exception is thrown within the COPPA Compliance UI.  
[stateChangeButtonFired](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Connect.CoppaDrawer-stateChangeButtonFired.html) | An event that fires when any button causes a state change within the COPPA compliance UI.  
* * *
