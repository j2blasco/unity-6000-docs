* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchAction-ctor.html

# SearchAction Constructor
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
public SearchAction(string providerId, string id, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) content); 
## Declaration
public SearchAction(string providerId, string id, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) content, Action<SearchItem[]> handler); 
## Declaration
public SearchAction(string providerId, string id, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) content, Action<SearchItem> handler); 
## Declaration
public SearchAction(string providerId, string name, [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) icon, string tooltip, Action<SearchItem[]> handler); 
## Declaration
public SearchAction(string providerId, string name, [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) icon, string tooltip, Action<SearchItem> handler); 
## Declaration
public SearchAction(string providerId, string name, [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) icon, string tooltip); 
### Parameters
Parameter | Description  
---|---  
id | Unique action id used to find it back later.  
providerId | The search provider ID that supports this action.  
content | Displays the displayname, an icon, and a tooltip when displaying the action in the Action Menu.  
handler | Handler that executes the action.  
name | Label name when displaying the action in the Action Menu.  
icon | Icon for the action in the Action Menu.  
tooltip | Tooltip associated with the action when displayed in the Action Menu.  
### Description
Default constructor to build a search action.
* * *
