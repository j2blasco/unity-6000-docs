* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor-target.html

#  [Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html).target
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
target; 
### Description
The object being inspected.
For editors that support multi-object editing, the target property should not be used inside [OnInspectorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.OnInspectorGUI.html) since it only refers to the first of the edited objects. It should still be used in [OnSceneGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.OnSceneGUI.html) and [OnPreviewGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.OnPreviewGUI.html), which will be called once for each of the selected objects with the target property referring to each of them in turn.  
  
Additional resources: [targets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor-targets.html), [serializedObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor-serializedObject.html), [Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) class.
* * *
