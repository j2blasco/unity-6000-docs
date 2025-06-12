* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D-streamingMipmapsPriority.html

#  [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html).streamingMipmapsPriority
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
streamingMipmapsPriority; 
### Description
Sets the relative priority for this Texture when reducing memory size to fit within the memory budget.
When mipmap streaming is enabled, Unity automatically reduces the size of Textures until they fit into the Texture streaming memory budget. This number is roughly a mipmap offset for the memory budget code. For example, with a priority of 2, Unity tries to use a mipmap two times larger than other Textures with a priority of 0. Negative values are also valid.
* * *
