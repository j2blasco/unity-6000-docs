* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView-duringSceneGui.html

#  [SceneView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html).duringSceneGui
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
### Parameters
Parameter | Description  
---|---  
value | The Scene view invoking this callback.  
### Description
Subscribe to this event to receive a callback whenever the Scene view calls the OnGUI method.
Use this event to implement custom handles and user interface. If you want to draw elements in the Scene view, for instance by using `Graphics.DrawMeshNow`, only do so during [EventType.Repaint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.Repaint.html).   
  

* * *
