* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PanelSettings-vertexBudget.html

#  [PanelSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PanelSettings.html).vertexBudget
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
vertexBudget; 
### Description
The expected number of vertices that will be used by this panel. 
A value of 0 means that the UI renderer will use its own default. If this hint is set too high, extra CPU and GPU memory may be allocated without actually being used. If set too low, more vertex buffers may be required, which may increase the number of draw calls and hinder performance. Changing this setting after initialization should be avoided because it resets the UI renderer. 
* * *
