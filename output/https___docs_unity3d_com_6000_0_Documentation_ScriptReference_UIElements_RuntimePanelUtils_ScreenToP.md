* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.RuntimePanelUtils.ScreenToPanel.html

#  [RuntimePanelUtils](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.RuntimePanelUtils.html).ScreenToPanel
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
public static [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) ScreenToPanel([UIElements.IPanel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPanel.html) panel, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) screenPosition); 
### Parameters
Parameter | Description  
---|---  
panel | The local coordinates reference panel.  
screenPosition | The screen position to transform.  
### Returns
**Vector2** A position in panel coordinates that corresponds to the provided screen position. 
### Description
Transforms a screen absolute position to its equivalent local coordinate on given panel. 
* * *
