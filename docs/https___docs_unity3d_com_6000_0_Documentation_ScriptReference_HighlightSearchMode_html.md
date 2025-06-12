* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HighlightSearchMode.html

# HighlightSearchMode
enumeration
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
### Description
Used to specify how to find a given element in the editor to highlight.
Let's consider various approaches to highlighting the Scale control in the Transform component.  
  
Using the [HighlightSearchMode.PrefixLabel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HighlightSearchMode.PrefixLabel.html) mode you can specify the label text "Scale" as the identifier to highlight the entire Scale control with both label and all three number fields included. This mode can't be used if you want to only highlight the X component of the Scale control. Since the label text of the X component is simply "X", you would get the X component of the Position control instead if you attempted that. The [HighlightSearchMode.PrefixLabel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HighlightSearchMode.PrefixLabel.html) mode works for any control that uses [EditorGUI.PrefixLabel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.PrefixLabel.html) or [EditorGUI.HandlePrefixLabel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.HandlePrefixLabel.html).  
  
If you use the [HighlightSearchMode.Content](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HighlightSearchMode.Content.html) mode to search for the text "Scale", only the label itself will be highlighted. This mode can highlight what corresponds to a single [GUIStyle.Draw](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.Draw.html) call and hence cannot highlight composite controls. It is particularly useful for highlighting buttons.  
  
The [HighlightSearchMode.Identifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HighlightSearchMode.Identifier.html) mode searches for rects explicitly marked to be highlightable using the [Highlighter.HighlightIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Highlighter.HighlightIdentifier.html) function. This is for example done for all controls that uses the [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) system, using the [SerializedProperty.propertyPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-propertyPath.html) as the identifier. This means you could use this mode to highlight the X component of the Scale control by searching for "m_LocalScale.x".  
  
The [HighlightSearchMode.Auto](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HighlightSearchMode.Auto.html) mode searches using all the above modes and can be used in most cases. Searching for "Scale" using this mode will highlight the entire Scale control rather than just the label, since the PrefixLabel handling is hit before the [GUIStyle.Draw](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.Draw.html) call of the label.  
  
Additional resources: [Highlighter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Highlighter.html).
### Properties
Property | Description  
---|---  
[None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HighlightSearchMode.None.html) | Highlights nothing.  
[Auto](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HighlightSearchMode.Auto.html) | Highlights the first element found using any of the search modes.  
[Identifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HighlightSearchMode.Identifier.html) | Highlights an element with a given identifier text.  
[PrefixLabel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HighlightSearchMode.PrefixLabel.html) | Highlights an entire editor control using its label text as identifier.  
[Content](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HighlightSearchMode.Content.html) | Highlights an element containing text using the text as identifier.  
* * *
