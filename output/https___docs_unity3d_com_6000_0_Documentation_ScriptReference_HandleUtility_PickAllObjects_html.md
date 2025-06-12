* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.PickAllObjects.html

#  [HandleUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.html).PickAllObjects
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
public static void PickAllObjects([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) position, List<Object> results); 
### Parameters
Parameter | Description  
---|---  
position | The position in screen coordinates. The top-left of the window is (0,0), and the bottom-right is (Screen.width, Screen.height).  
results | The output list to populate with all GameObjects at the specified position.  
### Description
Creates a list of all GameObjects under the specified position in screen coordinates.
`HandleUtility.PickAllObjects` must not be called during a repaint. In most cases, it is appropriate to call during [EventType.MouseDown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.MouseDown.html) or [EventType.MouseUp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.MouseUp.html). A common use would be to pick all GameObjects at the current cursor position.
* * *
