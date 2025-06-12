* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlatformIcon.SetTexture.html

#  [PlatformIcon](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlatformIcon.html).SetTexture
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
public void SetTexture([Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) texture, int layer); 
### Parameters
Parameter | Description  
---|---  
layer | Cannot be larger than [PlatformIcon.maxLayerCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlatformIcon-maxLayerCount.html).  
### Description
Assign a texture to the specified layer.
Texture file must be stored in the project and instance obtained using [AssetDatabase.LoadAssetAtPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAssetAtPath.html).
* * *
