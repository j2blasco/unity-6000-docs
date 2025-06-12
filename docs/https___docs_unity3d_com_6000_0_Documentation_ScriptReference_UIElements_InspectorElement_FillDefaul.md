* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.InspectorElement.FillDefaultInspector.html

#  [InspectorElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.InspectorElement.html).FillDefaultInspector
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
public static void FillDefaultInspector([UIElements.VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) container, [SerializedObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) serializedObject, [Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) editor); 
### Parameters
Parameter | Description  
---|---  
container | The parent VisualElement  
serializedObject | The SerializedObject to inspect  
editor | The editor currently used  
### Description
Adds default inspector property fields under a container VisualElement. 
The following example shows how to fill a container with default inspector fields. For a complete example, refer to [Create a default Inspector](https://docs.unity3d.com/6000.0/Documentation/Manual/ui-systems/create-default-inspector.html). 
```
 var container = new VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html)();
 InspectorElement.FillDefaultInspector[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.InspectorElement.FillDefaultInspector.html)(container, serializedObject, editor);

```

* * *
