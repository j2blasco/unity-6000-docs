* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D-minimumMipmapLevel.html

#  [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html).minimumMipmapLevel
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
minimumMipmapLevel; 
### Description
Restricts the mipmap streaming system to a minimum mip level for this Texture.
When this field is not set, the mipmap streaming system selects which mipmap to load based on the position of all Cameras. Setting this field limits the loaded mipmap level and Unity only uses the calculated mipmap streaming system value when it is larger than the minimum level selected. The mipmap level can still be modified by budgeting memory. Use the [streamingMipmapsPriority](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D-streamingMipmapsPriority.html) property to increase the chance of a particular Texture mipmap level being selected by the mipmap streaming system.  
  
Additional resources: [ClearMinimumMipmapLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.ClearMinimumMipmapLevel.html), [requestedMipmapLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D-requestedMipmapLevel.html).
* * *
