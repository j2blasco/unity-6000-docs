* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.CreateEditorWithContext.html

#  [Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html).CreateEditorWithContext
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
public static [Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) CreateEditorWithContext(Object[] targetObjects, [Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) context, Type editorType = null); 
### Description
Make a custom editor for `targetObject` or `targetObjects` with a context object.
This method is identical to [CreateEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.CreateEditor.html) except that the [SerializedObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) will be created using the context object passed as parameter. This context object will be used to store and retrieve the value for ExposedReference types declared on the [SerializedObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html).
* * *
