* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.RuntimePanelUtils.SetTextureDirty.html

#  [RuntimePanelUtils](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.RuntimePanelUtils.html).SetTextureDirty
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
public static void SetTextureDirty([UIElements.IPanel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPanel.html) panel, [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) texture); 
### Parameters
Parameter | Description  
---|---  
panel | The current panel  
texture | The texture whose content has changed.  
### Description
Notifies the dynamic atlas of the panel that the content of the provided texture has changed. If the dynamic atlas contains the texture, it will update it. 
* * *
