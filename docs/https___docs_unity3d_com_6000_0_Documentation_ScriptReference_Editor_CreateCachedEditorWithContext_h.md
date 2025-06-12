* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.CreateCachedEditorWithContext.html

#  [Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html).CreateCachedEditorWithContext
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
public static void CreateCachedEditorWithContext([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) targetObject, [Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) context, Type editorType, ref [Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) previousEditor); 
## Declaration
public static void CreateCachedEditorWithContext(Object[] targetObjects, [Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) context, Type editorType, ref [Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) previousEditor); 
### Description
Creates a cached editor using a context object.
This method is similar to [CreateCachedEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.CreateCachedEditor.html) except that the [SerializedObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) is created with the context object passed as a parameter. This context object stores and retrieves the value for the ExposedReference types declared on the [SerializedObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html).
* * *
