* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-style.html

#  [VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html).style
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
[UIElements.IStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle.html) style; 
### Description
Sets the style values on a [VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html). 
The returned style data, computed from USS files or inline styles written to this object in C#, doesn't represent the fully resolved styles, such as the final height and width of a VisualElement. To access these fully resolved styles, use resolvedStyle.   
  
For information about how to use this property and all the supported USS properties, refer to the [Apply styles in C# scripts](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-apply-styles-with-csharp.html) and [USS properties reference](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS-Properties-Reference.html) manual pages.   
  
Additional resources: [VisualElement.resolvedStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-resolvedStyle.html), [VisualElement.customStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-customStyle.html), [StyleSheet](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.StyleSheet.html)   
  

```
 // Set the background color of the element to red.
 element.style.backgroundColor = Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html);

```

* * *
