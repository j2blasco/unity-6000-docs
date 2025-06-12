* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProposition-ctor.html

# SearchProposition Constructor
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
public SearchProposition(string label, string replacement, string help, int priority, [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) icon, object data, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) color); 
## Declaration
public SearchProposition(string category, string label, string replacement, string help, int priority, [Search.TextCursorPlacement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.TextCursorPlacement.html) moveCursor, [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) icon, Type type, object data, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) color); 
## Declaration
public SearchProposition(string label, string replacement, string help, int priority, [Search.TextCursorPlacement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.TextCursorPlacement.html) moveCursor, [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) icon, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) color); 
### Parameters
Parameter | Description  
---|---  
category | Category text used to group propositions together in query builder mode.  
label | Display text of the proposition.  
replacement | Text used to auto-complete the query when selected.  
help | Help text used to display additional information about the search proposition.  
priority | Value used to sort the propositions among other search propositions when displaying choices to the user.  
moveCursor | Indicates when the text cursor should be moved when auto-completing the query with the selected proposition.  
icon | Icon used to display the proposition.  
color | Color used in query builder mode to draw the block using a specific color.  
data | User data that the user can retrieve later to determine the nature of the proposition.  
type | Type of search proposition value. This information is used in the query builder mode.  
### Description
Create a new search proposition.
Used with [SearchProvider.fetchPropositions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-fetchPropositions.html).
* * *
