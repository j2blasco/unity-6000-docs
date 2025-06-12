* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.UpdateExternalTexture.html

#  [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html).UpdateExternalTexture
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
public void UpdateExternalTexture(IntPtr nativeTex); 
### Parameters
Parameter | Description  
---|---  
nativeTex | Native 2D texture object.  
### Description
Updates Unity texture to use different native texture object.
This function is mostly useful for [native code plugins](https://docs.unity3d.com/6000.0/Documentation/Manual/native-plugin-interface.html) that create platform specific texture objects outside of Unity, and need to use these textures in Unity Scenes. For a texture created with [CreateExternalTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.CreateExternalTexture.html), this function switches to another underlying texture object if/when it changes.  
  
Additional resources: [CreateExternalTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.CreateExternalTexture.html).
* * *
