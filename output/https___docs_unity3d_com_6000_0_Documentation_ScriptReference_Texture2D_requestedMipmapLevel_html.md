* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D-requestedMipmapLevel.html

#  [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html).requestedMipmapLevel
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
requestedMipmapLevel; 
### Description
The mipmap level to load.
By default, the mipmap streaming system selects which mipmap to load based on the position of all Cameras. Setting this field forces a specific mipmap to be loaded and overrides the mipmap streaming system. The mipmap level can still be modified by budgeting memory. Use the [streamingMipmapsPriority](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D-streamingMipmapsPriority.html) property to increase the chance of a particular Texture mipmap level being selected by the mipmap streaming system. The requested level is unaffected by [minimumMipmapLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D-minimumMipmapLevel.html)  
  
The value of `requestedMipmapLevel` is an exact mipmap level that ranges from 0 to the maximum mipmap level of the specific texture, or the **Max Level Reduction** value if that's lower. 0 is the highest resolution mipmap level.  
  
Additional resources: [ClearRequestedMipmapLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.ClearRequestedMipmapLevel.html), [minimumMipmapLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D-minimumMipmapLevel.html).
* * *
