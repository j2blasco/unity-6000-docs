* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-resolvedStyle.html

#  [VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html).resolvedStyle
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
[UIElements.IResolvedStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IResolvedStyle.html) resolvedStyle; 
### Description
The final rendered style values of a visual element, as it's rendered in the current frame.(Read Only) 
Use `resolvedStyle` to find the actual rendered styling of a [VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) in the current frame, such as style values for width, height, and colors. You can get the resolved style value of an element to make layout decisions, troubleshoot styling issues, or ensure visual consistency across different platforms.   
  
The final rendered style is computed from applied classes, inherited styles from ancestors, and inline styles defined in UXML or C# code. Therefore, the resolved style might be different from what you set through the [VisualElement.style](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-style.html) property, depending on the other styles applied to the element.   
  
To get the resolved style when the geometry changes, register a callback to the [GeometryChangedEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.GeometryChangedEvent.html) event. If the element's geometry remains unchanged, consider adding a [scheduler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IVisualElementScheduler.html) to periodically check the element's resolved style. You can also poll the value during the [MonoBehaviour.LateUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.LateUpdate.html) phase at runtime if you have access to MonoBehaviours.   
  
For a list of all the style properties supported by UI Toolkit, refer to [USS properties reference](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS-Properties-Reference.html).   
  
For more information about how to use this property and an example of how style changes when layout updates, refer to [Apply styles in C# scripts](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-apply-styles-with-csharp.html).   
  
Additional resources: [VisualElement.style](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-style.html), [VisualElement.customStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-customStyle.html)   
  

```
 // Get the resolved width of the element.
 float width = element.resolvedStyle.width;

```

* * *
