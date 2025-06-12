* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Highlighter.HighlightIdentifier.html

#  [Highlighter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Highlighter.html).HighlightIdentifier
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
public static void HighlightIdentifier([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, string identifier); 
### Parameters
Parameter | Description  
---|---  
position | The position to make highlightable.  
identifier | The identifier text of the rect.  
### Description
Call this method to create an identifiable rect that the Highlighter can find.
If you want a custom rect in an EditorWindow or custom Editor to be highlightable, you can call this method to specify the rect and the identifier text for that rect. That will make it possible for the Highlighter to highlight the rect.
* * *
