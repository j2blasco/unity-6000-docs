* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Connect.ProjectBindDrawer.html

# ProjectBindDrawer
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
A container that fetches the UIElements that draw the Project Binding UI, and subscribes to its events.
### Constructors
Constructor | Description  
---|---  
[ProjectBindDrawer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Connect.ProjectBindDrawer-ctor.html) | The default constructor for the Drawer that subscribes to the callback events for the Link and Create buttons.  
### Public Methods
Method | Description  
---|---  
[Dispose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Connect.ProjectBindDrawer.Dispose.html) | Disposes of the UI.  
[GetVisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Connect.ProjectBindDrawer.GetVisualElement.html) | Retrieves the ProjectBind UI.  
### Events
Event | Description  
---|---  
[exceptionCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Connect.ProjectBindDrawer-exceptionCallback.html) | An event that fires when an exception is thrown within the Project Bind UI.  
[stateChangeButtonFired](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Connect.ProjectBindDrawer-stateChangeButtonFired.html) | An event that fires when any button within the Project Bind UI causes a state change.  
* * *
