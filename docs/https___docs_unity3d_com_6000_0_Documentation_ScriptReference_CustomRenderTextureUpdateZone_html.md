* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomRenderTextureUpdateZone.html

# CustomRenderTextureUpdateZone
struct in UnityEngine
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
### Description
Structure describing an Update Zone.
UpdateZones are used when updating the full custom render texture is not required. They are defined by a position, a size and a rotation inside the surface of the texture. Multiple Update Zones can be set up in order to update different parts of the texture at the same time. Additional resources: [CustomRenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomRenderTexture.html).
### Properties
Property | Description  
---|---  
[needSwap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomRenderTextureUpdateZone-needSwap.html) | If true, and if the texture is double buffered, a request is made to swap the buffers before the next update. Otherwise, the buffers will not be swapped.  
[passIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomRenderTextureUpdateZone-passIndex.html) | Shader Pass used to update the Custom Render Texture for this Update Zone.  
[rotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomRenderTextureUpdateZone-rotation.html) | Rotation of the Update Zone.  
[updateZoneCenter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomRenderTextureUpdateZone-updateZoneCenter.html) | Position of the center of the Update Zone within the Custom Render Texture.  
[updateZoneSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomRenderTextureUpdateZone-updateZoneSize.html) | Size of the Update Zone.  
* * *
