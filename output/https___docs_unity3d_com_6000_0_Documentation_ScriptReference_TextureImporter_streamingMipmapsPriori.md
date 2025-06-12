* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-streamingMipmapsPriority.html

#  [TextureImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.html).streamingMipmapsPriority
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html "Go to TextureImporter Component in the Manual")
streamingMipmapsPriority; 
### Description
Relative priority for this texture when reducing memory size in order to hit the memory budget.
When mipmap streaming is enabled, Unity will automatically reduce the size of textures until they fit into the texture streaming memory limits. The priority value can be thought of as a mipmap offset for the memory budget code. For example, with a priority of 2, Unity will attempt to use a mipmap two times larger than textures with a priority of 0.
* * *
