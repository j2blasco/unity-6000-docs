* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.RuntimePanelUtils.ResetDynamicAtlas.html

#  [RuntimePanelUtils](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.RuntimePanelUtils.html).ResetDynamicAtlas
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
public static void ResetDynamicAtlas([UIElements.IPanel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPanel.html) panel); 
### Description
Resets the dynamic atlas of the panel. 
Call this method to force a defragmentation of the atlas, which might reduce GPU memory usage. Use sparingly: the meshes and rendering commands of all textured elements will be released and will need to be regenerated.
* * *
