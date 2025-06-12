* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.UseDefaultMargins.html

#  [Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html).UseDefaultMargins
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
public bool UseDefaultMargins(); 
### Description
Override this method in subclasses to return false if you don't want default margins.
By default, content in the Inspector has a large left margin and a small right margin. This is because the entire [Editor.OnInspectorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.OnInspectorGUI.html) callback is wrapped in a vertical group with the [EditorStyles.inspectorDefaultMargins](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorStyles-inspectorDefaultMargins.html) style. For a consistent look, these default margins should be used for most GUI with regular controls.  
  
However, some special GUI elements may benefit from occupying the full width of the Inspector, with only a small margin in both sides. To disable the default margins, override the [Editor.UseDefaultMargins](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.UseDefaultMargins.html) method in your custom Editor and make it return false. Then you can wrap your GUI content inside a vertical groups to your liking. For example, you can wrap some of the GUI inside a vertical group with the [EditorStyles.inspectorFullWidthMargins](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorStyles-inspectorFullWidthMargins.html) style and wrap other parts of the GUI inside a vertical group with the [EditorStyles.inspectorDefaultMargins](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorStyles-inspectorDefaultMargins.html) style.  
  
Additional resources: [EditorGUILayout.BeginVertical](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.BeginVertical.html), [EditorGUILayout.EndVertical](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.EndVertical.html), [EditorStyles.inspectorDefaultMargins](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorStyles-inspectorDefaultMargins.html), [EditorStyles.inspectorFullWidthMargins](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorStyles-inspectorFullWidthMargins.html).
* * *
