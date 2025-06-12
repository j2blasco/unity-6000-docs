* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.CreateCachedEditor.html

#  [Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html).CreateCachedEditor
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
public static void CreateCachedEditor([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) targetObject, Type editorType, ref [Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) previousEditor); 
## Declaration
public static void CreateCachedEditor(Object[] targetObjects, Type editorType, ref [Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) previousEditor); 
### Parameters
Parameter | Description  
---|---  
obj | The object the editor is tracking.  
editorType | The requested editor type. Set to null for the default editor for the object.  
previousEditor | The previous editor for the object. After returning from CreateCachedEditor `previousEditor` is an editor for the `targetObject` or `targetObjects`.  
objects | The objects the editor is tracking.  
### Description
On return `previousEditor` is an editor for `targetObject` or `targetObjects`. The function either returns if the editor is already tracking the objects, or destroys the previous editor and creates a new one.
By default, the editor with a matching CustomEditor attribute is created. If an editorType is specified, an editor of that type is created instead. Use this if you have created multiple custom editors where each editor shows different properties of the object. previousEditor will be NULL if `objects` are of different types or if no approprate editor was found.
* * *
