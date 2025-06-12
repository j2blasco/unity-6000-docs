* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor-serializedObject.html

#  [Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html).serializedObject
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
[SerializedObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) serializedObject; 
### Description
A [SerializedObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) representing the object or objects being inspected.
Use the serializedObject inside the [OnInspectorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.OnInspectorGUI.html) function of a custom Editor, as described on the page about the [Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) class.  
  
Do not use the serializedObject inside [OnSceneGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.OnSceneGUI.html) or [OnPreviewGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.OnPreviewGUI.html). Use the target property directly in those callback functions instead.  
  
Additional resources: [Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) class, [SerializedObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) class.
* * *
