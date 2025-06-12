* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlatformIcon.SetTextures.html

#  [PlatformIcon](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlatformIcon.html).SetTextures
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
public void SetTextures(params Texture2D[] textures); 
### Parameters
Parameter | Description  
---|---  
textures | Must be an array of size [PlatformIcon.maxLayerCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlatformIcon-maxLayerCount.html).  
### Description
Assign all available icon layers.
Will overwrite all the currently set icon layers. Texture files must be stored in the project and instances obtained using [AssetDatabase.LoadAssetAtPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAssetAtPath.html).
* * *
