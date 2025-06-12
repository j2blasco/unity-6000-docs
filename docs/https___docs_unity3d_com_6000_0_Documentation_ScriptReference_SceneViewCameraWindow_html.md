* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneViewCameraWindow.html

# SceneViewCameraWindow
class in UnityEditor
/
Inherits from:[PopupWindowContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PopupWindowContent.html)
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
### Description
Use this class to instantiate a [SceneViewCameraWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneViewCameraWindow.html) window.
The [SceneViewCameraWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneViewCameraWindow.html) window displays settings for the [SceneView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html) camera.
### Constructors
Constructor | Description  
---|---  
[SceneViewCameraWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneViewCameraWindow-ctor.html) | Creates an instance of the SceneViewCameraWindow window.  
### Public Methods
Method | Description  
---|---  
[GetWindowSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneViewCameraWindow.GetWindowSize.html) | Retrieves the dimensions of the SceneViewCameraWindow window.  
[OnGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneViewCameraWindow.OnGUI.html) | A callback used for drawing the GUI controls of the SceneViewCameraWindow window.  
### Events
Event | Description  
---|---  
[additionalSettingsGui](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneViewCameraWindow-additionalSettingsGui.html) | Subscribe to this event to receive a callback when the SceneViewCameraWindow.OnGUI function is called.  
### Inherited Members
### Properties
Property | Description  
---|---  
[editorWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PopupWindowContent-editorWindow.html) | The EditorWindow that contains the popup content.  
### Public Methods
Method | Description  
---|---  
[CreateGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PopupWindowContent.CreateGUI.html) | Creates custom GUI with UI Toolkit for the popup.  
[OnClose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PopupWindowContent.OnClose.html) | Callback when the popup window is closed.  
[OnOpen](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PopupWindowContent.OnOpen.html) | Callback when the popup window is opened.  
* * *
