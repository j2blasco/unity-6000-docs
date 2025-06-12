* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader.OnGUI.html

#  [MultiColumnHeader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader.html).OnGUI
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
public void OnGUI([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) rect, float xScroll); 
### Parameters
Parameter | Description  
---|---  
xScroll | Horizontal scroll offset.  
rect | Rect where the MultiColumnHeader is drawn in.  
### Description
Render and handle input for the MultiColumnHeader at the given rect.
If the given `xScroll` is not 0 then the column headers will be scrolled but still clipped to the given Rect. This method can be overriden for complete custom behavior and rendering. For custom handling of indivdual column headers then see [ColumnHeaderGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader.ColumnHeaderGUI.html).
* * *
