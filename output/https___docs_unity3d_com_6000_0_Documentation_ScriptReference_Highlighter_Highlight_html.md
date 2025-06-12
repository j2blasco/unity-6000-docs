* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Highlighter.Highlight.html

#  [Highlighter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Highlighter.html).Highlight
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
public static bool Highlight(string windowTitle, string text); 
## Declaration
public static bool Highlight(string windowTitle, string text, [HighlightSearchMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HighlightSearchMode.html) mode); 
### Parameters
Parameter | Description  
---|---  
windowTitle | The title of the window the element is inside.  
text | The text to identify the element with.  
mode | Optional mode to specify how to search for the element.  
### Returns
**bool** `true` if the requested element was found; otherwise `false`. 
### Description
Highlights an element in the editor.
This function will highlight the specified element in the specified window. If the element could not be found, the function returns false. If the element is inside a scrollview and is not currently visible, the scrollview will first automatically scroll to reveal the element and then highlight it.  
  
Once the element is highlighted it will stay highlighted until either the [Highlighter.Stop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Highlighter.Stop.html) function is called, or the element disappears from view. The element could disappear from view if the user scrolls away from it, the window is closed, the section of the GUI with the element in it is collapsed or otherwise hidden, or when starting or stopping Play Mode.  
  
Most EditorGUI controls can be highlighted using their label as identifier.  
  
Any control that uses the [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) system can be highlighted using its [SerializedProperty.propertyPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-propertyPath.html).  
  
Any element with text in it can be highlighted using that text as identifier, which is for example useful for buttons.  
  
See the [HighlightSearchMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HighlightSearchMode.html) enum for more details on identifying elements.  
  
Additional resources: [Highlighter.Stop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Highlighter.Stop.html), [Highlighter.HighlightIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Highlighter.HighlightIdentifier.html).
* * *
